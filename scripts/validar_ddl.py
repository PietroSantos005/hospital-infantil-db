#!/usr/bin/env python3
"""Revisao estatica do subconjunto de DDL gerado para este projeto.

Nao executa SQL nem substitui o parser Oracle. Aceita CREATE TABLE com as
colunas simples NUMBER(p), VARCHAR2(n), DATE e CLOB, constraints por ALTER
TABLE e indices explicitos. Estilo diferente exige revisar o verificador.
"""
import argparse
import collections
import json
from pathlib import Path
import re
import sys


def inspect_ddl(path):
    sql = path.read_text(encoding="utf-8-sig")
    clean = re.sub(r"--[^\n]*", "", sql)
    errors = []
    tables = {}
    table_names = []
    for match in re.finditer(r"CREATE TABLE\s+(\w+)\s*\((.*?)\)\s*;", clean, re.S | re.I):
        table = match[1].upper()
        table_names.append(table)
        columns = {}
        for line in match[2].splitlines():
            line = line.strip().rstrip(",").strip()
            if not line:
                continue
            col = re.fullmatch(r"(\w+)\s+(NUMBER\s*\(\s*\d+\s*\)|VARCHAR2\s*\(\s*\d+\s*\)|DATE|CLOB)(?:\s+(NOT NULL))?", line, re.I)
            if not col:
                errors.append(f"Coluna fora do formato suportado: {table}: {line}")
                continue
            name = col[1].upper()
            if name in columns:
                errors.append(f"Coluna duplicada: {table}.{name}")
            columns[name] = {"type": re.sub(r"\s+", "", col[2].upper()), "required": bool(col[3])}
        tables[table] = columns
    pks = list(re.finditer(r"ALTER TABLE\s+(\w+)\s+ADD CONSTRAINT\s+(\w+)\s+PRIMARY KEY\s*\(([^)]+)\)", clean, re.S | re.I))
    fks = list(re.finditer(r"ALTER TABLE\s+(\w+)\s+ADD CONSTRAINT\s+(\w+)\s+FOREIGN KEY\s*\(([^)]+)\)\s+REFERENCES\s+(\w+)\s*\(([^)]+)\)", clean, re.S | re.I))
    unique = list(re.finditer(r"ALTER TABLE\s+(\w+)\s+ADD CONSTRAINT\s+(\w+)\s+UNIQUE\s*\(([^)]+)\)", clean, re.S | re.I))
    indexes = list(re.finditer(r"CREATE\s+(UNIQUE\s+)?INDEX\s+(\w+)\s+ON\s+(\w+)\s*\(([^)]+)\)", clean, re.S | re.I))
    checks = list(re.finditer(r"ALTER TABLE\s+(\w+)\s+ADD CONSTRAINT\s+(\w+)\s+CHECK\s*\(([^)]+)\)", clean, re.S | re.I))
    constraints = re.findall(r"ADD CONSTRAINT\s+(\w+)", clean, re.I)
    index_names = [m[2].upper() for m in indexes]
    for label, names in [("Tabela", table_names), ("Constraint", [n.upper() for n in constraints]), ("Indice", index_names)]:
        errors.extend(f"{label} duplicado: {n}" for n, count in collections.Counter(names).items() if count > 1)
    all_names = table_names + constraints + index_names + [c for cols in tables.values() for c in cols]
    errors.extend(f"Identificador acima de 30 bytes: {n}" for n in all_names if len(n.encode("utf-8")) > 30)
    primary = {}
    for m in pks:
        table, name = m[1].upper(), m[2]
        columns = tuple(c.strip().upper() for c in m[3].split(","))
        if len(columns) != 1:
            errors.append(f"PK composta: {name}")
        if table in primary:
            errors.append(f"Mais de uma PK: {table}")
        primary[table] = columns
        for column in columns:
            info = tables.get(table, {}).get(column)
            if not info or not info["required"]:
                errors.append(f"PK inexistente ou sem NOT NULL: {name}.{column}")
    for table in tables:
        if table not in primary:
            errors.append(f"Tabela sem PK: {table}")
    for m in fks:
        child, name, column, parent, target = m[1].upper(), m[2], m[3].strip().upper(), m[4].upper(), m[5].strip().upper()
        ci = tables.get(child, {}).get(column)
        pi = tables.get(parent, {}).get(target)
        if not ci or not pi:
            errors.append(f"Referencia inexistente: {name}")
            continue
        if ci["type"] != pi["type"]:
            errors.append(f"Tipos diferentes na FK: {name}")
        if not ci["required"]:
            errors.append(f"FK opcional nesta versao: {name}")
        if primary.get(parent) != (target,):
            errors.append(f"FK nao aponta para PK simples: {name}")
    for m in unique:
        for column in m[3].split(","):
            if column.strip().upper() not in tables.get(m[1].upper(), {}):
                errors.append(f"Coluna inexistente no UNIQUE: {m[2]}")
    for m in indexes:
        for column in m[4].split(","):
            name = re.sub(r"\s+(ASC|DESC)\s*$", "", column.strip(), flags=re.I).upper()
            if name not in tables.get(m[3].upper(), {}):
                errors.append(f"Coluna inexistente no indice: {m[2]}")
    for m in checks:
        if m[1].upper() not in tables:
            errors.append(f"Tabela inexistente no CHECK: {m[2]}")
    if re.search(r"\bUNKNOWN\b|\bDROP\b", clean, re.I):
        errors.append("UNKNOWN ou DROP encontrado")
    if re.search(r"--\s*ERROR\s*:", sql, re.I):
        errors.append("Comentario de erro de geracao encontrado")
    if len(tables) != 12 or len(pks) != 12 or len(fks) != 12:
        errors.append("Esta versao espera 12 tabelas, 12 PKs e 12 FKs")
    return {"tables": len(tables), "columns": sum(map(len, tables.values())), "primary_keys": len(pks), "foreign_keys": len(fks), "not_null_columns": sum(c["required"] for cols in tables.values() for c in cols.values()), "unique_constraints": len(unique), "explicit_unique_indexes": sum(bool(m[1]) for m in indexes), "check_constraints": len(checks), "max_identifier_bytes": max((len(n.encode("utf-8")) for n in all_names), default=0), "errors": errors, "execution_in_oracle": "not_performed"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", type=Path, default=Path(__file__).resolve().parents[1] / "sql/01_schema.sql")
    args = parser.parse_args()
    try:
        result = inspect_ddl(args.path)
    except (OSError, UnicodeError) as error:
        print(f"Erro ao ler DDL: {error}", file=sys.stderr)
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if result["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())

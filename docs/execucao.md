# Explorar e executar

## Consulta dos modelos

Os PDFs e os Markdown podem ser abertos sem banco Oracle. Para editar o desenho nativo, adicionar o `.dmd` e sua pasta associada conforme [modelos/README.md](../modelos/README.md).

## Revisão local do DDL

Requer Python 3, sem bibliotecas externas:

```bash
python scripts/validar_ddl.py
```

O verificador inspeciona o formato de DDL usado neste projeto. Ele confere referências, tipos, obrigatoriedade, PKs, índices e nomes, mas não substitui o parser ou a execução do Oracle.

## Criação das tabelas em Oracle

O script foi gerado para Oracle Database 11g. A conexão com o banco e um usuário com privilégios/quota para criar tabelas e índices devem ser preparados no ambiente de execução.

1. Abra o SQL Developer e conecte-se ao usuário do projeto.
2. Use um schema destinado a testes em que as tabelas deste projeto ainda não existam.
3. Abra `sql/01_schema.sql` e associe a worksheet à conexão correta.
4. Use **Run Script (F5)** e confira toda a saída em **Script Output**.
5. Execute `sql/03_verificar_estrutura.sql` e compare os objetos com [Validação](validacao.md).
6. Registre a versão do banco, a data e os resultados quando concluir a execução.

O script cria objetos e não contém `DROP`. DDL Oracle pode confirmar transações e deixar objetos criados antes de um erro; uma falha exige revisar a saída e o estado do schema antes de repetir o script. A execução em outros SGBDs exige adaptar os tipos e a sintaxe.

## Consultas de demonstração

`sql/02_consultas.sql` apresenta cinco consultas com `JOIN`, `LEFT JOIN`, agregação e ordenação. Elas não alteram dados. Em um banco recém-criado, sem registros, não haverá conteúdo clínico ou operacional para exibir.

Não há carga de dados no pacote. Os identificadores precisam ser fornecidos explicitamente, pois esta versão não declara sequência ou geração automática de IDs.

## Regras a validar depois da criação

| Cenário | Resultado esperado no schema |
|---|---|
| Atendimento apontando para paciente inexistente | Rejeição por FK |
| Campo obrigatório sem valor | Rejeição por `NOT NULL` |
| CPF de colaborador repetido | Rejeição pelo índice único |
| Duas contas com o mesmo colaborador | Rejeição pelo índice único |
| Login, CNPJ ou patrimônio repetido | Rejeição por `UNIQUE` |
| Quantidade negativa em estoque/EPI/equipamento | Rejeição por `CHECK` |
| Requisição com quantidade zero | Rejeição por `CHECK` |

Estes são resultados esperados das regras declaradas. Ainda não constituem testes executados em Oracle.

Referências: [SQL Developer — Worksheet](https://docs.oracle.com/en/database/oracle/sql-developer/24.3/rptug/sql-developer-concepts-usage.html) e [Oracle — COMMIT e DDL](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/COMMIT.html).

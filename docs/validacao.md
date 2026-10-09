# Validação da versão

Revisão estática concluída em **9 de outubro de 2026**.

| Verificação | Resultado |
|---|---|
| Tabelas | 12 |
| Colunas | 102 |
| PKs simples | 12 |
| FKs obrigatórias | 12 |
| Colunas NOT NULL | 62 |
| Constraints UNIQUE | 3 |
| Índices únicos explícitos | 2 |
| CHECKs de quantidade | 4 |
| Maior identificador | 30 bytes |
| Referências e tipos das FKs | Conferidos no DDL |
| Comentários de erro, UNKNOWN ou DROP | Ausentes no SQL executável |
| Erros encontrados pelo verificador | 0 |
| Execução em Oracle | Pendente |

## Reproduzir a revisão

Na raiz do repositório, execute:

```bash
python scripts/validar_ddl.py
```

O comando encerra com código zero quando passa nas verificações suportadas. A saída registrada está em [validacao.json](validacao.json). O verificador foi escrito para o formato deste export; não é um analisador geral de SQL. Ele não verifica permissões, quotas, disponibilidade do banco, planos de execução ou a correção clínica dos dados.

SHA-256 de `sql/01_schema.sql` nesta revisão:

```text
d3600d51e8438feb64df3a8e18748121483973bc4c245495e2b79c4bdf09af22
```

## Arquivos e rastreabilidade

O schema foi obtido do export do Data Modeler de 7 de outubro de 2026, mantendo suas definições e convertendo apenas as quebras de linha para LF. O próprio resumo do export informa zero erros e zero avisos; isso não equivale a uma execução bem-sucedida no banco.

Os três PDFs são as exportações fornecidas para esta versão; as imagens PNG são renderizações desses mesmos PDFs. A documentação declara as regras de unicidade que ficaram ocultas na apresentação lógica.

O dicionário de dados foi extraído do schema incluído, com 102 colunas, tipos e regras correspondentes. As consultas ilustrativas foram conferidas quanto aos nomes de tabelas e colunas; sua execução em Oracle está pendente.

O pacote de portfólio reúne esses arquivos e a documentação atualizada. Os rascunhos, capturas de configuração e relatórios anteriores não foram incluídos, pois contêm propostas de campos e tipos que já evoluíram.

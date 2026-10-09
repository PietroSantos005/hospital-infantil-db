# Contexto e modelagem

## Objetivo do negócio

O projeto propõe uma base centralizada para um sistema interno de gestão de um hospital infantil. O público previsto são profissionais de saúde, equipe administrativa e demais colaboradores autorizados. O modelo reúne cadastros, registros clínicos e informações sobre recursos hospitalares.

A implementação atual compreende os modelos de dados e o DDL. Telas, serviços web, autenticação e movimentação automática de estoque fazem parte de evoluções da aplicação.

## Três apresentações do modelo

| Apresentação acadêmica | Conteúdo | Arquivo |
|---|---|---|
| Conceitual | Entidades e relacionamentos com cardinalidades | [PDF conceitual](diagramas/modelo-conceitual.pdf) |
| Lógica | Tabelas, colunas e chaves, sem tipos Oracle | [PDF lógico](diagramas/modelo-logico.pdf) |
| Física | Tabelas, colunas, chaves, índices, tipos e tamanhos Oracle | [PDF físico](diagramas/modelo-fisico.pdf) |

Os três PDFs foram exportados do Data Modeler. A apresentação conceitual simplifica o modelo de entidades; a lógica e a física usam apresentações do modelo relacional. No Data Modeler, o modelo físico específico do SGBD fica na árvore de objetos e fornece as opções usadas na geração do DDL.

Na exportação lógica recebida, os índices únicos não estão visíveis. A unicidade de CPF e do vínculo entre usuário e colaborador está no DDL, no dicionário e no PDF físico. Na atualização dessa imagem, ativar **View Details → Indexes**. O conceitual também pode ser compactado e ter os relacionamentos nomeados sem alterar as regras.

## Relacionamentos e cardinalidades

`0..N` permite zero ou vários dependentes. `0..1` permite zero ou um. Em todos os casos, o dependente exige exatamente um registro principal, pois a FK é `NOT NULL`.

| Principal | Dependente | Dependentes por principal | Interpretação |
|---|---|---|---|

| `PACIENTE` | `ACOMPANHANTE` | 0..N | Paciente possui acompanhantes cadastrados. |
| `PACIENTE` | `DOCUMENTACAO` | 0..N | Paciente possui documentos. |
| `PACIENTE` | `ATENDIMENTO` | 0..N | Paciente recebe atendimentos. |
| `PACIENTE` | `REGISTRO_MEDICACAO` | 0..N | Paciente possui registros de aplicação de medicação. |
| `COLABORADOR` | `USUARIO` | 0..1 | Colaborador pode possuir uma conta. |
| `COLABORADOR` | `ATENDIMENTO` | 0..N | Colaborador é associado ao atendimento. |
| `COLABORADOR` | `REGISTRO_MEDICACAO` | 0..N | Colaborador é associado à aplicação registrada. |
| `COLABORADOR` | `REQUISICAO_DE_MATERIAIS` | 0..N | Colaborador solicita materiais. |
| `FORNECEDOR` | `ESTOQUE` | 0..N | Fornecedor é associado ao item cadastrado. |
| `FORNECEDOR` | `EPI` | 0..N | Fornecedor é associado ao EPI cadastrado. |
| `FORNECEDOR` | `EQUIPAMENTO` | 0..N | Fornecedor é associado ao equipamento cadastrado. |
| `ESTOQUE` | `REQUISICAO_DE_MATERIAIS` | 0..N | Item pode constar de várias requisições. |

## Decisões e integridade

As relações usam FKs separadas dos identificadores próprios das tabelas. O relacionamento colaborador–usuário é limitado por um índice único sobre `USUARIO.COLABORADOR_id_colaborador`. As demais referências não exigem que o registro principal já possua dependentes.

| Regra | Mecanismo no DDL |
|---|---|
| Identificar cada registro | Uma PK simples por tabela |
| Impedir referência a registro inexistente | 12 FKs obrigatórias |
| Impedir CPF de colaborador repetido | `COLABORADOR_CPF_UK`, índice único |
| Impedir duas contas para o mesmo colaborador | `USUARIO__IDX`, índice único |
| Impedir login, CNPJ e patrimônio repetidos | Três constraints `UNIQUE` |
| Impedir quantidades negativas | Três `CHECK (quantidade >= 0)` |
| Impedir requisição com quantidade zero ou negativa | `CHECK (quantidade > 0)` |

As FKs não declaram exclusão em cascata. A política de retenção e exclusão dos registros precisa ser definida na aplicação e nos procedimentos do hospital.

## Limites do domínio e próximas decisões

1. **Acompanhantes:** uma linha pertence a um paciente; a mesma pessoa acompanhando várias crianças pode ter seus dados repetidos. Uma evolução pode separar a pessoa do vínculo. Grau de parentesco não comprova representação legal.
2. **Documentação:** armazena tipo, número, emissão e observação. Arquivos digitalizados e prova de responsabilidade legal precisam de estrutura específica se entrarem no escopo.
3. **Medicação:** a aplicação está vinculada ao paciente e colaborador; não há FK para um atendimento nem catálogo de medicamentos.
4. **Estoque e requisições:** os valores são registros informados. Uma requisição não reduz o estoque automaticamente. Entregas, devoluções e concorrência precisam de regras e transações próprias.
5. **Equipamentos:** há patrimônio único e quantidade na mesma linha. Antes de ampliar o projeto, definir se cada linha representa um bem individual ou um conjunto.
6. **Fornecedores:** cada recurso aponta para um fornecedor. Compras históricas ou múltiplos fornecedores por item exigem novas relações.
7. **Contas:** `nivel_acesso`, `status` e `senha_hash` são colunas; não representam um serviço de autenticação ou autorização já implementado.
8. **Validações:** o DDL não impõe idade infantil, formatos de documentos, domínios de status ou cronologia clínica.

## Legenda dos diagramas

| Símbolo | Significado |
|---|---|
| `P` | Coluna de chave primária |
| `F` | Coluna de chave estrangeira |
| `U` | Coluna indicada como única por constraint na apresentação |
| `*` | Coluna obrigatória |
| Extremidade com “pé de galinha” | Multiplicidade de vários registros |

A notação visual varia entre os modelos lógico e relacional do Oracle. A tabela de cardinalidades acima declara explicitamente a opcionalidade adotada; os índices únicos também devem ser considerados na interpretação.

Referência: [Oracle — Data Modeler Concepts and Usage](https://docs.oracle.com/en/database/oracle/sql-developer-data-modeler/24.3/dmdug/data-modeler-concepts-usage.html).

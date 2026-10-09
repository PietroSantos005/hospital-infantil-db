# Dicionário de dados

Extraído do DDL de `sql/01_schema.sql`. Os nomes, tipos e regras abaixo refletem o script incluído neste repositório.

`PK` = chave primária; `FK` = chave estrangeira. A unicidade por constraint e por índice é identificada separadamente.

## PACIENTE

Cadastro do paciente e informações gerais de acompanhamento.

| Coluna | Tipo Oracle | Obrigatória | Regras |
|---|---|---|---|
| `id_paciente` | `NUMBER(10)` | Sim | PK |
| `nome` | `VARCHAR2(120)` | Sim | — |
| `nome_social` | `VARCHAR2(120)` | Não | — |
| `genero` | `VARCHAR2(30)` | Não | — |
| `data_nascimento` | `DATE` | Sim | — |
| `tipo_sanguineo` | `VARCHAR2(3)` | Não | — |
| `endereco` | `VARCHAR2(250)` | Não | — |
| `complemento` | `VARCHAR2(100)` | Não | — |
| `telefone` | `VARCHAR2(20)` | Não | — |
| `telefone_fixo` | `VARCHAR2(20)` | Não | — |
| `email` | `VARCHAR2(254)` | Não | — |
| `condicao` | `CLOB` | Não | — |
| `observacao` | `CLOB` | Não | — |

## ACOMPANHANTE

Cadastro do acompanhante vinculado a um paciente.

| Coluna | Tipo Oracle | Obrigatória | Regras |
|---|---|---|---|
| `id_acompanhante` | `NUMBER(10)` | Sim | PK |
| `nome` | `VARCHAR2(120)` | Sim | — |
| `data_nascimento` | `DATE` | Não | — |
| `tipo_sanguineo` | `VARCHAR2(3)` | Não | — |
| `cpf` | `VARCHAR2(11)` | Não | — |
| `endereco` | `VARCHAR2(250)` | Não | — |
| `telefone` | `VARCHAR2(20)` | Não | — |
| `telefone_fixo` | `VARCHAR2(20)` | Não | — |
| `email` | `VARCHAR2(254)` | Não | — |
| `grau_parentesco` | `VARCHAR2(40)` | Sim | — |
| `PACIENTE_id_paciente` | `NUMBER(10)` | Sim | FK → `PACIENTE.id_paciente` |

## DOCUMENTACAO

Identificação dos documentos associados ao paciente; não armazena arquivos digitalizados.

| Coluna | Tipo Oracle | Obrigatória | Regras |
|---|---|---|---|
| `id_documentacao` | `NUMBER(10)` | Sim | PK |
| `tipo_documento` | `VARCHAR2(80)` | Sim | — |
| `numero_documento` | `VARCHAR2(50)` | Sim | — |
| `data_emissao` | `DATE` | Não | — |
| `observacao` | `CLOB` | Não | — |
| `PACIENTE_id_paciente` | `NUMBER(10)` | Sim | FK → `PACIENTE.id_paciente` |

## COLABORADOR

Cadastro dos profissionais e demais colaboradores do hospital.

| Coluna | Tipo Oracle | Obrigatória | Regras |
|---|---|---|---|
| `id_colaborador` | `NUMBER(10)` | Sim | PK |
| `nome` | `VARCHAR2(120)` | Sim | — |
| `cpf` | `VARCHAR2(11)` | Sim | UNIQUE index |
| `departamento` | `VARCHAR2(100)` | Sim | — |
| `cargo` | `VARCHAR2(100)` | Sim | — |
| `especialidade` | `VARCHAR2(100)` | Não | — |
| `crm` | `VARCHAR2(20)` | Não | — |
| `telefone` | `VARCHAR2(20)` | Não | — |
| `telefone_fixo` | `VARCHAR2(20)` | Não | — |
| `cidade` | `VARCHAR2(100)` | Não | — |
| `email` | `VARCHAR2(254)` | Não | — |
| `turno` | `VARCHAR2(30)` | Não | — |

## USUARIO

Dados de uma conta vinculada ao colaborador; o DDL não implementa login ou autorização.

| Coluna | Tipo Oracle | Obrigatória | Regras |
|---|---|---|---|
| `id_usuario` | `NUMBER(10)` | Sim | PK |
| `login` | `VARCHAR2(80)` | Sim | UNIQUE constraint |
| `senha_hash` | `VARCHAR2(255)` | Sim | — |
| `nivel_acesso` | `VARCHAR2(30)` | Sim | — |
| `status` | `VARCHAR2(30)` | Sim | — |
| `COLABORADOR_id_colaborador` | `NUMBER(10)` | Sim | FK → `COLABORADOR.id_colaborador`; UNIQUE index |

## ATENDIMENTO

Registro do atendimento e de seu conteúdo clínico, vinculado ao paciente e colaborador.

| Coluna | Tipo Oracle | Obrigatória | Regras |
|---|---|---|---|
| `id_atendimento` | `NUMBER(10)` | Sim | PK |
| `motivo` | `VARCHAR2(500)` | Sim | — |
| `data_atendimento` | `DATE` | Sim | — |
| `hora_atendimento` | `VARCHAR2(8)` | Sim | — |
| `historico_paciente` | `CLOB` | Não | — |
| `historico_familiar` | `CLOB` | Não | — |
| `prescricao` | `CLOB` | Não | — |
| `diagnostico` | `CLOB` | Não | — |
| `situacao_paciente` | `VARCHAR2(50)` | Sim | — |
| `PACIENTE_id_paciente` | `NUMBER(10)` | Sim | FK → `PACIENTE.id_paciente` |
| `COLABORADOR_id_colaborador` | `NUMBER(10)` | Sim | FK → `COLABORADOR.id_colaborador` |

## REGISTRO_MEDICACAO

Registro de aplicação de medicação ao paciente por um colaborador.

| Coluna | Tipo Oracle | Obrigatória | Regras |
|---|---|---|---|
| `id_registro_medicacao` | `NUMBER(10)` | Sim | PK |
| `nome` | `VARCHAR2(120)` | Sim | — |
| `fabricante` | `VARCHAR2(120)` | Não | — |
| `lote` | `VARCHAR2(50)` | Não | — |
| `dose` | `VARCHAR2(60)` | Sim | — |
| `data_aplicacao` | `DATE` | Sim | — |
| `observacao` | `CLOB` | Não | — |
| `PACIENTE_id_paciente` | `NUMBER(10)` | Sim | FK → `PACIENTE.id_paciente` |
| `COLABORADOR_id_colaborador` | `NUMBER(10)` | Sim | FK → `COLABORADOR.id_colaborador` |

## FORNECEDOR

Cadastro de fornecedores dos recursos hospitalares.

| Coluna | Tipo Oracle | Obrigatória | Regras |
|---|---|---|---|
| `id_fornecedor` | `NUMBER(10)` | Sim | PK |
| `razao_social` | `VARCHAR2(150)` | Sim | — |
| `cnpj` | `VARCHAR2(14)` | Sim | UNIQUE constraint |
| `localidade` | `VARCHAR2(150)` | Não | — |
| `contato` | `VARCHAR2(120)` | Não | — |
| `email` | `VARCHAR2(254)` | Não | — |
| `telefone` | `VARCHAR2(20)` | Não | — |

## ESTOQUE

Cadastro do item e de sua quantidade atual informada.

| Coluna | Tipo Oracle | Obrigatória | Regras |
|---|---|---|---|
| `id_item` | `NUMBER(10)` | Sim | PK |
| `nome_item` | `VARCHAR2(120)` | Sim | — |
| `categoria` | `VARCHAR2(60)` | Sim | — |
| `quantidade` | `NUMBER(10)` | Sim | CHECK `quantidade >= 0` |
| `validade` | `DATE` | Não | — |
| `localizacao` | `VARCHAR2(100)` | Sim | — |
| `FORNECEDOR_id_fornecedor` | `NUMBER(10)` | Sim | FK → `FORNECEDOR.id_fornecedor` |

## EPI

Cadastro de equipamentos de proteção individual e quantidade informada.

| Coluna | Tipo Oracle | Obrigatória | Regras |
|---|---|---|---|
| `id_epi` | `NUMBER(10)` | Sim | PK |
| `nome` | `VARCHAR2(120)` | Sim | — |
| `tipo` | `VARCHAR2(60)` | Sim | — |
| `quantidade` | `NUMBER(10)` | Sim | CHECK `quantidade >= 0` |
| `validade` | `DATE` | Não | — |
| `FORNECEDOR_id_fornecedor` | `NUMBER(10)` | Sim | FK → `FORNECEDOR.id_fornecedor` |

## EQUIPAMENTO

Cadastro de equipamentos com número de patrimônio único.

| Coluna | Tipo Oracle | Obrigatória | Regras |
|---|---|---|---|
| `id_equipamento` | `NUMBER(10)` | Sim | PK |
| `nome` | `VARCHAR2(120)` | Sim | — |
| `tipo` | `VARCHAR2(60)` | Sim | — |
| `numero_patrimonio` | `VARCHAR2(50)` | Sim | UNIQUE constraint |
| `quantidade` | `NUMBER(10)` | Sim | CHECK `quantidade >= 0` |
| `estado_conservacao` | `VARCHAR2(40)` | Sim | — |
| `FORNECEDOR_id_fornecedor` | `NUMBER(10)` | Sim | FK → `FORNECEDOR.id_fornecedor` |

## REQUISICAO_DE_MATERIAIS

Pedido de uma quantidade de um item por um colaborador.

| Coluna | Tipo Oracle | Obrigatória | Regras |
|---|---|---|---|
| `id_requisicao` | `NUMBER(10)` | Sim | PK |
| `data_requisicao` | `DATE` | Sim | — |
| `quantidade` | `NUMBER(10)` | Sim | CHECK `quantidade > 0` |
| `status` | `VARCHAR2(20)` | Sim | — |
| `observacao` | `CLOB` | Não | — |
| `COLABORADOR_id_colaborador` | `NUMBER(10)` | Sim | FK → `COLABORADOR.id_colaborador` |
| `ESTOQUE_id_item` | `NUMBER(10)` | Sim | FK → `ESTOQUE.id_item` |

## Semântica dos tipos e validações complementares

- `NUMBER(10)` possui precisão de 10 dígitos e escala zero. Não impõe sinal positivo; os `CHECK` de quantidade definem o sinal aceito.
- `VARCHAR2(n)` limita texto. Como o DDL não especifica `BYTE` ou `CHAR`, a semântica de tamanho depende da sessão Oracle que criar as colunas. Não se deve interpretar todo `n` como quantidade garantida de caracteres.
- `DATE` pode armazenar data e horário até segundos. `hora_atendimento` permanece como `VARCHAR2(8)` no modelo atual.
- `CLOB` armazena texto longo, sem um tamanho `n` declarado neste modelo.
- CPF e CNPJ são armazenados como texto. O schema não valida dígitos verificadores, formato ou existência cadastral.
- Status, nível de acesso, tipo sanguíneo e horário não têm domínio ou validação de formato no DDL atual.
- IDs não têm sequência, trigger ou geração automática; devem ser fornecidos explicitamente na inserção.

Referência: [Oracle — Data Types](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/Data-Types.html).

# Segurança e privacidade

## O que existe e o que está proposto

| Aspecto | Estado nesta versão |
|---|---|
| PKs, FKs, campos obrigatórios e limites de quantidade | Declarados no DDL; execução Oracle pendente |
| Coluna `senha_hash` e campos de perfil/status | Declarados; autenticação e autorização pendentes |
| Criptografia, auditoria, backups e controle de sessões | Medidas propostas; não implementadas neste repositório |
| Certificação de conformidade ou uso hospitalar real | Não realizada |

## Aplicação da LGPD ao domínio

A Lei nº 13.709/2018 distingue dados pessoais e dados pessoais sensíveis, incluindo informações de saúde (art. 5º). O projeto reúne cadastros identificáveis e conteúdo clínico; o art. 14 exige considerar o melhor interesse de crianças e adolescentes. A base legal de cada tratamento deve ser definida conforme sua finalidade e os arts. 7º e 11, sem assumir que consentimento resolve todas as situações. O art. 46 exige medidas de segurança desde a concepção.

Na análise do projeto, separar cadastro, conteúdo clínico e contas de acesso; limitar os campos à finalidade; documentar acesso, retenção e exercício de direitos. O cadastro de acompanhante não comprova responsabilidade legal nem consentimento. A conformidade exige processos e controles além do schema.

Fonte: [LGPD — texto oficial](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm). Consulta: 9 de outubro de 2026.

## Classificação aplicada ao modelo

| Dados | Exemplos no projeto | Tratamento proposto |
|---|---|---|
| Cadastro identificável | Nome, CPF, contatos, endereço e nascimento | Acesso conforme função e coleta limitada à finalidade |
| Conteúdo de saúde | Diagnóstico, históricos, prescrição, condição e aplicação de medicação | Restringir acesso clínico e registrar consultas/alterações |
| Conta de acesso | Login, hash, nível de acesso e status | Restringir administração de contas e proteger segredos |
| Recursos e fornecedores | Quantidades, patrimônio, razão social e CNPJ | Integridade operacional; contatos podem conter dados pessoais |

## Controles previstos para uma aplicação

- **Autenticação:** gerar e verificar hashes de senha com mecanismo adequado e salt; proteger sessões e oferecer autenticação reforçada para funções sensíveis.
- **Autorização:** aplicar permissões no servidor. A equipe de almoxarifado, por exemplo, não precisa visualizar diagnósticos para atender uma requisição.
- **Confidencialidade:** proteger conexões, armazenamento e backups; manter chaves e credenciais fora do repositório.
- **Integridade:** usar constraints, validações de negócio, consultas parametrizadas e transações para movimentações de estoque.
- **Rastreabilidade:** registrar quem acessou ou alterou informações sensíveis e quando, protegendo também os registros de auditoria.
- **Disponibilidade:** planejar backups, testar restaurações e definir recuperação após falhas.

São propostas de engenharia para evolução do projeto; não estão implementadas pelo simples fato de existir uma coluna ou tabela.

## Contexto de inteligência artificial

Não há componente de IA neste schema. O PL nº 2.338/2023 foi consultado em 9 de outubro de 2026 e consta na Câmara como aguardando parecer na Comissão Especial; é apresentado aqui como projeto de lei, não como lei vigente. Se houver uma futura função de IA clínica, seu desenho precisará ser analisado quanto a dados utilizados, supervisão humana, transparência e riscos.

Fonte: [Câmara dos Deputados — PL 2.338/2023](https://www.camara.leg.br/proposicoesWeb/fichadetramitacao?idProposicao=2487262).

## Conteúdo deste repositório

O schema e os diagramas descrevem a estrutura dos dados. Não foram incluídos cadastros reais, credenciais, dumps de banco, arquivos de conexão nem bases de teste com pessoas identificáveis. Demonstrações futuras devem usar dados inteiramente fictícios.

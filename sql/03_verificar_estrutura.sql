-- Consultas de verificacao pos-execucao, no usuario dono das tabelas.
-- Nao foram executadas nesta revisao. Nao altera dados.

-- 1. As 12 tabelas do projeto.
SELECT table_name
FROM user_tables
WHERE table_name IN ('PACIENTE', 'ACOMPANHANTE', 'DOCUMENTACAO', 'COLABORADOR', 'USUARIO', 'ATENDIMENTO', 'REGISTRO_MEDICACAO', 'FORNECEDOR', 'ESTOQUE', 'EPI', 'EQUIPAMENTO', 'REQUISICAO_DE_MATERIAIS')
ORDER BY table_name;

-- 2. Constraints e estado. Tipos: P=PK, R=FK, U=UNIQUE, C=CHECK/NOT NULL.
SELECT table_name, constraint_name, constraint_type, status, validated
FROM user_constraints
WHERE table_name IN ('PACIENTE', 'ACOMPANHANTE', 'DOCUMENTACAO', 'COLABORADOR', 'USUARIO', 'ATENDIMENTO', 'REGISTRO_MEDICACAO', 'FORNECEDOR', 'ESTOQUE', 'EPI', 'EQUIPAMENTO', 'REQUISICAO_DE_MATERIAIS')
ORDER BY table_name, constraint_type, constraint_name;

-- 3. Os dois indices unicos explicitos. Indices de PK/UK podem aparecer
-- em outras consultas; aqui filtramos apenas os dois declarados no script.
SELECT table_name, index_name, uniqueness, status
FROM user_indexes
WHERE index_name IN ('COLABORADOR_CPF_UK', 'USUARIO__IDX')
ORDER BY table_name, index_name;

-- 4. Tipos, obrigatoriedade e semantica real de comprimento apos a criacao.
SELECT table_name, column_name, data_type, data_precision, data_scale,
       char_length, char_used, nullable
FROM user_tab_columns
WHERE table_name IN ('PACIENTE', 'ACOMPANHANTE', 'DOCUMENTACAO', 'COLABORADOR', 'USUARIO', 'ATENDIMENTO', 'REGISTRO_MEDICACAO', 'FORNECEDOR', 'ESTOQUE', 'EPI', 'EQUIPAMENTO', 'REQUISICAO_DE_MATERIAIS')
ORDER BY table_name, column_id;

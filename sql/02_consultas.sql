-- Consultas ilustrativas para Oracle. Nao executadas nesta revisao.
-- Executar depois da criacao do schema. Sem dados, as consultas retornam
-- resultados vazios ou contagens zero. Nao altera registros.

-- 1. Quantidade de atendimentos por paciente, incluindo quem nao tem nenhum.
SELECT p.id_paciente,
       p.nome,
       COUNT(a.id_atendimento) AS quantidade_atendimentos
FROM PACIENTE p
LEFT JOIN ATENDIMENTO a ON a.PACIENTE_id_paciente = p.id_paciente
GROUP BY p.id_paciente, p.nome
ORDER BY p.id_paciente;

-- 2. Colaboradores e suas contas opcionais.
SELECT c.id_colaborador,
       c.nome,
       c.cargo,
       u.login,
       u.status AS status_conta
FROM COLABORADOR c
LEFT JOIN USUARIO u ON u.COLABORADOR_id_colaborador = c.id_colaborador
ORDER BY c.id_colaborador;

-- 3. Itens com seu fornecedor, quantidade informada e localizacao.
SELECT e.id_item,
       e.nome_item,
       e.quantidade,
       e.localizacao,
       f.razao_social
FROM ESTOQUE e
JOIN FORNECEDOR f ON f.id_fornecedor = e.FORNECEDOR_id_fornecedor
ORDER BY e.id_item;

-- 4. Requisicoes com solicitante e item.
SELECT r.id_requisicao,
       r.data_requisicao,
       c.nome AS solicitante,
       e.nome_item,
       r.quantidade AS quantidade_solicitada,
       r.status
FROM REQUISICAO_DE_MATERIAIS r
JOIN COLABORADOR c ON c.id_colaborador = r.COLABORADOR_id_colaborador
JOIN ESTOQUE e ON e.id_item = r.ESTOQUE_id_item
ORDER BY r.data_requisicao, r.id_requisicao;

-- 5. Aplicacoes de medicacao com paciente e colaborador.
SELECT rm.id_registro_medicacao,
       p.nome AS paciente,
       c.nome AS colaborador,
       rm.nome AS medicacao,
       rm.dose,
       rm.data_aplicacao
FROM REGISTRO_MEDICACAO rm
JOIN PACIENTE p ON p.id_paciente = rm.PACIENTE_id_paciente
JOIN COLABORADOR c ON c.id_colaborador = rm.COLABORADOR_id_colaborador
ORDER BY rm.data_aplicacao, rm.id_registro_medicacao;

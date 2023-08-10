SELECT
    c.nome AS client_nome,
    c.cpf AS client_cpf,
    c.rg AS client_rg,
    c.data_nascimento AS client_data_nascimento,
    a.cep AS address_cep,
    a.logradouro AS address_logradouro,
    a.complemento AS address_complemento,
    a.numero AS address_numero,
    a.bairro AS address_bairro,
    a.cidade AS address_cidade,
    a.estado AS address_estado
FROM clients c
JOIN addresses a ON c.endereco_id = a.id;
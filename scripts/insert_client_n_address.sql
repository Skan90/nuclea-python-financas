INSERT INTO addresses (cep, logradouro, complemento, numero, bairro, cidade, estado)
VALUES ('11065-200', 'Avenida Presidente Wilson', '13L', '42', 'Gonzaga', 'Santos', 'SP')
RETURNING id;

INSERT INTO clients (nome, cpf, rg, data_nascimento, endereco_id)
VALUES ('Manuela Lopes', '51633872432', '12345678x', '2022-10-30', 1);
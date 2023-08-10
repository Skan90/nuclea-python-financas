UPDATE address
SET complemento = '<new_complemento>'
WHERE client_id = (SELECT id FROM clients WHERE cpf = '<client_cpf>');

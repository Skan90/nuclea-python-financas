import unittest
from unittest.mock import patch

from faker import Factory

from repository.clients_data import clients
from main import main
from utils.is_valid_cpf import generate_cpf
from utils.return_to_menu import ReturnToMenuException


def fake_name_generator():
    fake = Factory.create('pt_BR')
    return fake.name()


class TestStringMethods(unittest.TestCase):

    def test_should_register_a_user_and_exit(self):
        name = fake_name_generator()
        cpf = generate_cpf()
        inputs = ["1", name, cpf, "12345678x", "30/10/2022", "11065200", "sim", "42", "s", "13L", "nao"]
        with patch("builtins.input", side_effect=inputs):
            try:
                main()
            except ReturnToMenuException:
                pass

        expected_client = {
            'Nome': name,
            'CPF': cpf,
            'RG': '12345678x',
            'Data de Nascimento': '2022-10-30',
            'Endereço': {'CEP': '11065-200', 'Logradouro': 'Avenida Presidente Wilson', 'Complemento': '13L',
                         'Número': '42', 'Bairro': 'Gonzaga', 'Cidade': 'Santos', 'Estado': 'SP'}
        }
        self.assertIn(expected_client, clients)


if __name__ == '__main__':
    unittest.main()

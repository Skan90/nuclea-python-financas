import requests
import re


def is_valid_cep(cep):
    cep_regex = re.compile(r'^\d{8}$')
    return bool(cep_regex.match(cep))


def search_cep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if "erro" not in data:
            address = {
                "CEP": data["cep"],
                "Logradouro": data["logradouro"],
                "Complemento": data["complemento"],
                "Bairro": data["bairro"],
                "Cidade": data["localidade"],
                "Estado": data["uf"]
            }
            return address
    return None

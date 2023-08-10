from client_functions.print_single_client import print_single_client
from repository.clients_data import clients
from utils.is_valid_cep import search_cep, is_valid_cep
from utils.is_valid_cpf import is_valid_cpf
from utils.is_valid_date_of_birth import validate_brazilian_date
from utils.is_valid_rg import is_valid_rg
from utils.return_to_menu import return_to_menu
from utils.text_format import capitalize_text


def register_client():
    print("Informe os dados do cliente:")

    client = {
        "Nome": capitalize_text(input("Nome: ")),
        "CPF": is_valid_cpf(),
        "RG": is_valid_rg(),
        "Data de Nascimento": validate_brazilian_date(),
    }

    while True:
        cep = input("CEP: ")
        if not is_valid_cep(cep):
            print("Por favor, digite 8 números no padrão: 11065200")
            continue

        address = search_cep(cep)
        if address is None:
            print("CEP não encontrado. Digite novamente o CEP.")
            continue

        print("Endereço encontrado:")
        for key, value in address.items():
            print(f"{key}: {value}")

        confirm = input("Confirmar endereço? (Sim/Não): ").strip().lower()
        if confirm in ("sim", "s", "y"):
            client["Endereço"] = {
                "CEP": address["CEP"],
                "Logradouro": address["Logradouro"],
                "Complemento": address["Complemento"],
                "Número": input("Digite o número: "),
                "Bairro": address["Bairro"],
                "Cidade": address["Cidade"],
                "Estado": address["Estado"]
            }
            break

    complemento_choice = input("O endereço é apartamento ou tem complemento? (Sim/Não): ").strip().lower()
    if complemento_choice in ("sim", "s", "y"):
        client["Endereço"]["Complemento"] = input("Digite o complemento ou o apartamento: ")
    else:
        client["Endereço"]["Complemento"] = ""

    clients.append(client)
    print("Cliente cadastrado com sucesso!\n")

    print("Detalhes do cliente cadastrado:")
    print(clients)
    print("----\n\n\n")
    print_single_client(client)

    return_to_menu()

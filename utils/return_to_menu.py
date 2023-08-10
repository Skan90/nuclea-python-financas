class ReturnToMenuException(Exception):
    pass


def return_to_menu():
    while True:
        choice = input("Deseja retornar ao Menu Principal? (Sim / Não): ").lower()
        if choice in ["sim", "s", "yes"]:
            break
        elif choice in ["não", "nao", "no", "n"]:
            print("Saindo do sistema...")
            raise ReturnToMenuException()  # Raise the custom exception
        else:
            print("Escolha inválida! Por favor, tente novamente.")

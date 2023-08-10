from client_functions.register_client import register_client
from portfolio_functions.analyze_investment_portfolio import analyze_investment_portfolio
from portfolio_functions.print_portfolio_report import print_portfolio_report
from stock_functions.register_stock import register_stock
from utils.print_menu import print_menu


def main():
    while True:
        print_menu()
        try:
            choice = int(input("Digite sua escolha: "))
            if choice == 1:
                register_client()
            elif choice == 2:
                register_stock()
            elif choice == 3:
                analyze_investment_portfolio()
            elif choice == 4:
                print_portfolio_report()
            elif choice == 5:
                print("Saindo do sistema...")
                break
            else:
                print("Escolha inválida! Por favor, tente novamente.")
        except ValueError:
            print("Erro! Por favor, digite um número.")

if __name__ == "__main__":
    main()

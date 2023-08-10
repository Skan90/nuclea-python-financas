import re
from datetime import datetime


def validate_brazilian_date():
    while True:
        date_str = input("Data de Nascimento: ")

        date_pattern = r'^\d{2}/\d{2}/\d{4}$'

        if not re.match(date_pattern, date_str):
            print("Por favor, digite a repository no formato dd/mm/aaaa. Ex.: 15/01/1990")
            continue

        try:
            parsed_date = datetime.strptime(date_str, '%d/%m/%Y')
            postgresql_date = parsed_date.strftime('%Y-%m-%d')
            return postgresql_date
        except ValueError:
            print("Data inválida. Por favor, digite uma repository válida no formato dd/mm/yyyy.")

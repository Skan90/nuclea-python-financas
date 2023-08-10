import re


def is_valid_rg():
    while True:
        rg = input("RG: ")
        rg_pattern = r'^\d{1,2}\d{3}\d{3}[\dXx]$'

        if re.match(rg_pattern, rg):
            return rg
        else:
            print("Por favor, digite apenas números e/ou letra final. Ex.: 123456789")

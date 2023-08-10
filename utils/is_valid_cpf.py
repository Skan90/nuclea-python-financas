from validate_docbr import CPF


def is_valid_cpf():
    cpf_is_invalid = True

    while cpf_is_invalid:
        cpf = input("CPF: ")
        cpf_validator = CPF()

        if cpf_validator.validate(cpf):
            cpf_is_invalid = False
            return cpf  # Return the validated CPF number
        else:
            print("Erro ao validar CPF.\nPor favor, digite um número de CPF válido.")


def generate_cpf():
    cpf = CPF()
    return cpf.generate()

import sys

cpf_input = input("Digite o CPF (pode conter pontos e traços): ")

# Remover pontos e traços
cpf_limpo = ''.join(filter(str.isdigit, cpf_input))

# Valida se o cpf consta números repetidos.
valorSequencial = cpf_limpo == cpf_limpo[0] * len(cpf_limpo)

if valorSequencial:
    print("Você enviou sequência de números iguais.")
    sys.exit()

# Verificar se o CPF possui 11 dígitos
if len(cpf_limpo) != 11:
    print("CPF inválido. Deve conter 11 dígitos.")
else:
    # Calcular o primeiro dígito verificador
    soma = 0
    peso = 10
    for i in range(9):
        soma += int(cpf_limpo[i]) * peso
        peso -= 1
    resto = soma % 11
    digito1 = 0 if resto < 2 else 11 - resto

    # Calcular o segundo dígito verificador
    soma = 0
    peso = 11
    for i in range(10):
        soma += int(cpf_limpo[i]) * peso
        peso -= 1
    resto = soma % 11
    digito2 = 0 if resto < 2 else 11 - resto

    # Verificar se os dígitos verificadores são válidos
    if int(cpf_limpo[9]) == digito1 and int(cpf_limpo[10]) == digito2:
        print("CPF válido.")
    else:
        print("CPF inválido.")

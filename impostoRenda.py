salario = float(input("Digite o valor do seu sálario: "))

if salario <= 1903.98:
    print(f"Colaborador isento de imposto de renda")
    print(f"Salário a receber = {salario}")

elif salario <= 2826.65:
    ir=salario*0.075
    salario = salario - ir
    print(f"O colaborador deve pagar {ir}")
    print(f"Salário a receber = {salario}")

elif salario <= 3751.05:
    ir=salario*0.15
    salario = salario - ir
    print(f"O colaborador deve pagar {ir}")
    print(f"Salário a receber = {salario}")

elif salario <= 3751.05:
    ir=salario*0.15
    salario = salario - ir
    print(f"O colaborador deve pagar {ir}")
    print(f"Salário a receber = {salario}")

elif salario <= 4664.68:
    ir=salario*0.15
    salario = salario - ir
    print(f"O colaborador deve pagar {ir}")
    print(f"Salário a receber = {salario}")
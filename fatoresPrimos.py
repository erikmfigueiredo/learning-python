n = int(input("Entre com um inteiro maior que 1: "))
fator = 2
mult = 0

while n > 1:
    while n % fator == 0:
        mult = mult + 1
        n = n / fator
    if mult>0:
        print("Fator:",fator, "Multiplicidade = ", mult)
    fator = fator + 1
    mult = 0
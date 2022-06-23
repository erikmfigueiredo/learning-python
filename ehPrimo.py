def ehPrimo(x):
    fator = 2
    if x == 2:
        return True
    while x  % fator != 0 and fator <= x/2:
        fator = fator + 1
    if x % fator == 0:
        return False
    else:
        return True

n = int(input("Digite um numero inteiro: "))
while n>0:
    if ehPrimo(n):
        print(n, "Eh primo!")
    else:
        print(n, "Nao eh primo!")
    n = int(input("Digite um numero inteiro: "))


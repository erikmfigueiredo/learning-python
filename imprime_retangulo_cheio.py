x = int(input("digite a largura: "))
y = int(input("digite a altura: "))

contx = 0
conty = 0

while conty < y:
    while contx < x:
        print("#", end="")
        contx = contx + 1
    print()
    conty = conty + 1
    contx = 0
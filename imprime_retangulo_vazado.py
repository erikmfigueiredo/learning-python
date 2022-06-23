x = int(input("digite a largura: "))
y = int(input("digite a altura: "))

z = x-2
contx = 0
conty = 0
contz = 0

while conty < y:
    if conty == 0 or conty == y-1:
        while contx < x:
            print("#", end="")
            contx = contx + 1
    else:
         while contx < x:
            print("#", end="")
            while contz < z:
                print(" ", end="")
                contz = contz + 1
            contx = contx + (x-1)
    contz = 0
    print()
    conty = conty + 1
    contx = 0

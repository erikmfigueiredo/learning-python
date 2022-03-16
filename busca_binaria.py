def busca_binaria(lista, elemento):
    min = 0
    max = len(lista)-1
    encontrado = False

    while min <= max and not encontrado:
        meio_lista = (min+max)//2
        if lista[meio_lista] == elemento:
            encontrado = True

        else:
            if elemento < lista[meio_lista]:
                max = meio_lista - 1
            
            else:
                min = meio_lista + 1
    return encontrado


testelista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(busca_binaria(testelista, 16))
def exec_quicksort(lista,inicio,fim):
    if inicio < fim:
        pivo = exec_particao(lista,inicio,fim)
        exec_quicksort(lista,inicio,pivo-1)
        exec_quicksort(lista,pivo+1,fim)
    return lista


def exec_particao(lista,inicio,fim):
    pivo = lista[fim]
    esquerda = inicio
    for direita in range (inicio,fim):
        if lista[direita] <= pivo:
            lista[direita], lista[esquerda] = lista[esquerda], lista[direita]
            esquerda += 1
    lista[esquerda], lista[fim] = lista[fim], lista[esquerda]
    return esquerda

lista = [1,8,9,77,5,7,63,58,0]

print(exec_quicksort(lista,inicio=0,fim=len(lista)-1))
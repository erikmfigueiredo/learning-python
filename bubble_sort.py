def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(n-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    
    return lista

lista1 = [5,8,7,3,6,5,4,1,8,2]
print(bubble_sort(lista1))
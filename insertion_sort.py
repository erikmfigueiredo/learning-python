from wsgiref.validate import validator


def insertion_sort(lista):
    for i in range(1,len(lista)):
        valor_inserir = lista[i]
        j = i - 1
        
        while j >= 0 and lista[j] > valor_inserir:
            lista[j+1] = lista[j]
            j = j - 1    
        lista[j+1] = valor_inserir   
   
    return lista

lista1 = [10,5,8,12,6,7,25,3]
print(insertion_sort(lista1))
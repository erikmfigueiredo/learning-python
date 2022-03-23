def merge_sort_div(lista):
    if len(lista) <= 1: return lista
    else:
        meio = len(lista) // 2
        esquerda = merge_sort_div(lista[:meio])
        direita = merge_sort_div(lista[meio:])
        return merge_sort_exec(esquerda,direita)

def merge_sort_exec(esquerda,direita):
    sub_lista_ordenada = []
    topo_esquerda, topo_direita = 0, 0
    while topo_esquerda < len(esquerda) and topo_direita < len(direita):
        if esquerda[topo_esquerda] <= direita[topo_direita]:
            sub_lista_ordenada.append(esquerda[topo_esquerda])
            topo_esquerda += 1
        else:
            sub_lista_ordenada.append(direita[topo_direita])
            topo_direita += 1
    
    sub_lista_ordenada += esquerda[topo_esquerda:]
    sub_lista_ordenada += direita[topo_direita:]
    
    return sub_lista_ordenada

lista = [5,8,2,10,9,55,6,8,9,5,77,42]
print(merge_sort_div(lista))

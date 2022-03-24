#DESAFIO PARA ORGANIZAR, ORDENAR E BUSCAR CPF's

#PARTE 1: ALGORITMO MERGE SORT (MELHOR TEMPO DE RESPOSTA EM PIOR CASO):

from xml.dom import minicompat


def executar_merge_sort(lista, inicio=0,fim=None):
    if not fim:
        fim = len(lista)

    if fim - inicio > 1:
        meio = (inicio+fim)//2
        executar_merge_sort(lista,inicio,meio)
        executar_merge_sort(lista,meio,fim)
        executar_merge(lista,inicio,meio,fim)

    return lista

def executar_merge(lista,inicio,meio,fim):
    esquerda = lista[inicio:meio]
    direita = lista[meio:fim]
    topo_esquerda = topo_direita = 0

    for p in range(inicio,fim):
        if topo_esquerda >= len(esquerda):
            lista[p] = direita[topo_direita]
            topo_direita += 1
        elif topo_direita >= len(direita):
            lista[p] = esquerda[topo_esquerda]
            topo_esquerda += 1
        elif esquerda[topo_esquerda] < direita[topo_direita]:
            lista[p] = esquerda[topo_esquerda]
            topo_esquerda += 1
        else:
            lista[p] = direita[topo_direita]
            topo_direita += 1   


#PARTE 2: ALGORITMO DE BUSCA (BINÁRIA POIS É O MELHOR PARA DADOS ORDENADOS):

def executar_busca_binaria(lista,valor):
    min = 0
    max = len(lista)-1

    while min <= max:
        meio = (min+max)//2
        if valor < lista[meio]:
            max = meio - 1
        elif valor > lista[meio]:
            min = meio +1
        else:
            return True
    return False


#PARTE 3: ALGORITMO QUE VERIFICA E CORRIGE O CPF:

def criar_lista_dedup_ordenada(lista):
    lista = [str(cpf).replace('.','').replace('-','') for cpf in lista]
    lista = [cpf for cpf in lista if len(cpf) == 11]
    lista = executar_merge_sort(lista)

    lista_dedup = []
    for cpf in lista:
        if not executar_busca_binaria(lista_dedup, cpf):
            lista_dedup.append(cpf)

    return lista_dedup


#PARTE 4: TESTAR

def testar_funcao(lista_cpfs):
    lista_dedup = criar_lista_dedup_ordenada(lista_cpfs)
    print(lista_dedup)

lista_cpfs = ['44444444444', '111.111.111-11', '11111111111', '222.222.222-22', '333.333.333-33', '22222222222', '444.44444']
testar_funcao(lista_cpfs)
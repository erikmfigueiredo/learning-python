def conversao_mes_extenso(data):
    mes = '''janeiro fevereiro março
      abril maio junho julho agosto
      setembro outubro novembro
      dezembro'''.split()
    d, m, a = data.split('/')
    
    mes_extenso = mes[int(m)-1]
    return f'{d} de {mes_extenso} de {a}'

date = str(input("Entre com a data no formato dd/mm/aaaa:  "))

print(conversao_mes_extenso(date))
def calcular_valor(valor_prod, qtde, moeda="real", desconto=None, acrescimo=None):
    v_bruto = valor_prod * qtde

    if desconto:
        v_liquido = v_bruto - (v_bruto * (desconto / 100))

    elif acrescimo:
        v_liquido = v_bruto + (v_bruto * (acrescimo / 100))

    else:
        v_liquido = v_bruto

    if moeda == 'real':
        return v_liquido

    elif moeda == 'dolar':
        return v_liquido * 5
    
    elif moeda == 'euro':
        return v_liquido * 5.7

    else:
        print("Moeda não cadastrada!")
        return 0

a = int(input("Entre com valor do produto: "))
b = int(input("Entre com a quantidade de produto: "))
c = input("Entre com o tipo de moeda: ")
d = int(input("Entre com o desconto caso houver: "))
e = int(input("Entre com acrescimo caso houver: "))

valor_a_pagar = calcular_valor(a, b, c, d, e)

print(f"\nO valor final da conta é {valor_a_pagar} reais.")
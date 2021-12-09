def fatorial(x):
  valor = 1
  while x>1:
    valor = valor * x
    x = x-1
  return valor

n = int(input("Entre com valor de N: "))
k = int(input("Entre com valor de K: "))

a = fatorial(n)
b = fatorial(k)
c = fatorial((n-k))

coeficienteBinomial = a/(b*c)

print("\nO coeficiente binomial é:",coeficienteBinomial)
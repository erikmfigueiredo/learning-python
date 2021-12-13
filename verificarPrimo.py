# VERIFICAR SE É PRIMO

n = int(input("Digite um número inteiro: "))
i = 2 
primo = 0

while i<n and primo==0:
  if (n%i) == 0:
    primo = 1
    print("não primo")
  i=i+1

if primo==0:
  print("primo")

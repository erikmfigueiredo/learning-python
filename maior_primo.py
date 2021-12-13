def ehPrimo(n):
  primo = 0
  i = 2
  while i<n:
    if (n%i) == 0:
      primo = 1
      return False
    i=i+1

  if primo==0:
    return True

def maior_primo(k):
    j = 2
    maior = 0
    
    while j<=k:
        if ehPrimo(j) == True:
            maior = j
        j=j+1

    return(maior)

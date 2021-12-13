def ehPrimo(n):
  primo = 0
  i = 2
  while i<n:
    if (n%i) == 0:
      primo = 1
      print("não primo")
      return
    i=i+1

  if primo==0:
    print("primo")
    return

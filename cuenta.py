numero = 4

def aumentar():
  global numero
  numero = numero + numero
  print(numero)
  return numero

def restar():
  global numero
  numero = numero - numero/2
  print(numero)
  return(numero)

aumentar()
restar()
print(numero)
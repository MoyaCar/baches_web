from django.shortcuts import render
import cuenta
import modelos



def baches(request):
  option_test_val = modelos.option_test_val
  return render(request,'home.html', {'option_test':option_test_val})

def salida(request):
  option_test_val = modelos.option_test_val
  numero = cuenta.aumentar()
  print(numero)
  print(cuenta.numero)
  return render(request, 'home.html', {'numero':numero, 'option_test':option_test_val})

def restar(request):
  numero = cuenta.restar()
  print(numero)
  return render(request, 'home.html', {'numero':numero})

def filmar_video(request):
  modelos.reproducir_video()
  return render(request, 'home.html')

def option_test(request):
  modelos.option_test()
  option_test_val = modelos.option_test_val
  return render(request, 'home.html', {'option_test':option_test_val})

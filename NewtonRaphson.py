# Newton Raphson

# Victoria Nieto
# Camilo Mora
# Juan Camilo Gomez

import Funciones as fn

print('Algoritmo Newton Raphson')

x = 0
error = 1.0
i = 1

print('------INICIO------\n')

while(error > 0.01):
  print(f'Iteracion # {i}\n')
  print(f'Valor x = {x: .4f}')

  print(f'f(x) = {fn.ft_Newton(x):.4f}')
  print(f'f_dev(x) = {fn.ft_Dev_Newton(x):.4f}')

  x1 = x - (fn.ft_Newton(x) / fn.ft_Dev_Newton(x))
  error = abs((x1-x)/x1)
  
  print(f'Raiz Aproximada x1 = {x1: .4f}')
  print(f'Error = {error*100: .2f}%')
  print('-----------------------')
  
  x = x1

  i = i + 1

print(f'El error aproximado final fue = {error*100: .2f}%\n')
print(f'La raiz Aproximada fue = {x: .4f}')
print('-------FIN-------')
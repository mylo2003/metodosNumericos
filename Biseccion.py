# Bisección

# Victoria Nieto
# Camilo Mora
# Juan Camilo Gomez

import Funciones as fn

print('Método de Bisección\n')

a = 0
b = 1
error = 1.0
i = 1

print('------INICIO------\n')

while(error > 0.01):
  
  m = (a + b) / 2
  error = (b - a) / 2
  
  print(f'Iteracion # {i}')
  print(f'Punto a = {a: .4f}')
  print(f'Punto b = {b: .4f}')
  print(f'Punto m = {m: .4f}')
  print(f'f(a) = {fn.ft_Biseccion(a): .4f}')
  print(f'f(b) = {fn.ft_Biseccion(b): .4f}')
  print(f'f(m) = {fn.ft_Biseccion(m): .4f}')
  print(f'Error = {error*100: .2f}%')
  print('-----------------')
  
  if((fn.ft_Biseccion(a) * fn.ft_Biseccion(m)) < 0):
    b = m
  else:
    a = m
    
  i = i + 1 

print(f'El error aproximado final fue = {error*100: .2f}%\n')
print(f'Los puntos A y B respectivamente fueron = ({a: .4f}, {b: .4f})\n')
print('-------FIN-------')

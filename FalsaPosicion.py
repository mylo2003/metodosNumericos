# Falsa posición

# Victoria Nieto
# Camilo Mora
# Juan Camilo Gomez

import Funciones as fn

print('Método de Falsa Posición')

a = 0
b = 1
error = 1.0
i = 1

print('--------INICIO--------\n')

while(error > 0.01):

  c = ((a*fn.ft_FalsaPosicion(b))-(b*fn.ft_FalsaPosicion(a)))/(fn.ft_FalsaPosicion(b)-fn.ft_FalsaPosicion(a))
  
  if(i > 1):
    error = abs(c - aux)
    
  aux = c

  
  print(f'Iteracion #{i}')
  print(f'Punto a = {a: .4f}')
  print(f'Punto b = {b: .4f}')
  print(f'Punto c = {c: .4f}')
  print(f'f(a) = {fn.ft_FalsaPosicion(a):.4f}')
  print(f'f(b) = {fn.ft_FalsaPosicion(b):.4f}')
  print(f'f(c) = {fn.ft_FalsaPosicion(c): .4f}')

  if(i > 1):
    print(f'Error = {(error*100):.2f}%')
  
  if((fn.ft_FalsaPosicion(a) * fn.ft_FalsaPosicion(c)) < 0):
    b = c
  else: 
    a = c
  
  print('------------------------')
  
  i = i + 1 

print(f'El error aproximado final fue = {error*100: .2f}%\n')
print(f'Los puntos A y B respectivamente fueron = ({a: .4f}, {b: .4f})\n')
print('-------FIN-------')
  

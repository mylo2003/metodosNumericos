# Punto Fijo

# Victoria Nieto
# Camilo Mora
# Juan Camilo Gomez

import Funciones as fn

print('Método Punto Fijo')

x = 0
error = 1.0
i = 1

print('------INICIO------\n')

while(error > 0.01):

  error = abs((fn.ft_PuntoFijo(x) - x)/fn.ft_PuntoFijo(x))

  x = fn.ft_PuntoFijo(x)

  print(f'Iteracion # {i}')
  print(f'Raiz Aproximada x = {x: .4f}')
  print(f'Error = {error*100: .2f}%')
  print('-----------------')

  i = i + 1


print(f'El error aproximado final fue = {error*100: .2f}%')
print(f'La raiz Aproximada fue = {x: .4f}\n')
print('-------FIN-------')



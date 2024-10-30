import math

# -----------------------------------
# Funciones para Método Bisección

# Algebraica
def fa_Biseccion(x):
  return x**4 - 7*x**3 - 7

# Trascendental
def ft_Biseccion(x):
  return math.exp(3*x) - 4

# -----------------------------------
# Funciones para Método Falsa posición

# Algebraica
def fa_FalsaPosicion(x):
  return x**5 - 7*x**2 - 1

# Trascendental
def ft_FalsaPosicion(x):
  return math.exp(3*x) - 4


# -----------------------------------
# Funciones para  Método de Newton-Raphson

# Algebraica
def fa_Newton(x):
  return x**3 - 2*x - 5

def fa_Dev_Newton(x):
  return (3*x**2) - 2

# Trascendental
def ft_Newton(x):
  return (1 / math.e**x) - x

def ft_Dev_Newton(x):
  return ((-1)*math.e**((-1)*x)) - 1


# -----------------------------------
# Funciones para Método Punto Fijo

# Algebraica
def fa_PuntoFijo(x):
  return 5/(2*x + 1)

# Trascendental
def ft_PuntoFijo(x):
  return 0.4*math.e**(x**2)

# -----------------------------------


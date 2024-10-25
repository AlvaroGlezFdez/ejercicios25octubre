import random


def calcular_modulo(a, b):
    if b == 0:
        raise ValueError("El divisor b no puede ser cero.")
    
    # Ajustar el valor de a para que esté en el rango de 0 a b - 1
    while a >= b:
        a -= b
    while a < 0:
        a += b

    return a

x = random.randint(1,200)
y = random.randint(1,200)

print(x)
print(y)
print(calcular_modulo(x,y))
      
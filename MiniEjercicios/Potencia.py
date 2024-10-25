import random

x = random.randint(1,10)
y = random.randint(1,20)

def calcular_potencia(a,b):
    resultado = a
    for i in range(1,b):
        resultado = resultado * a
         

    return resultado



print(f"la base es {x} y el exponenete es {y}")

print(calcular_potencia(x,y))



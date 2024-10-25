import random
# Para esta primera solucion nos piden untilizar un bucle for
# el primer paso es crear una lista de n elemtos, de forma aleatoria.

n = random.randint(4,20)  # este va ser el número de elementos de nuestra lista
lista = [] # creamos una lista vacía donde añadiremos después nuestros numeros aleatoriamente
for i in range(1, n+1):
    numero_lista = random.randint(1,50)
    while numero_lista in lista:
        numero_lista = random.randint(1,50) # ponemos este while para evitar que en nuestra lista haya algun numero repetido
    lista.append(numero_lista)

print("nuestra lista de ejemplo es:",lista)


def suma_de_listas(lista,resultado=0): # Aquí estammos utilizando una funcion para poder guardar los valores de la sunma en una variable llamada resultado
    for i in lista:
        resultado = resultado + i # iteramos de tal forma que se va actualizando el valor de resultado

    return resultado        # devolvemos el valor de resulado
    

    
print(suma_de_listas(lista)) # llamamos a la funcion y le pasamos como parametro nuestra lista aleatoria



    

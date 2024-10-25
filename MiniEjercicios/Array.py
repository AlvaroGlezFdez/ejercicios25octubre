import random

lista = []
tamaño_lista = random.randint(5,15)

for i in range(1,tamaño_lista +1):
    i = random.randint(1,200)
    while i in lista:
        i = random.randint(1,200)
    
    lista.append(i)

print(lista)

def ordenar_array(arr):
    print(" Seleccione el la opción de como quiere ordenar la lista:")
    print("==========================================================")
    print("\n1. Ascendiente \n2. Descenciente \n3. Aleatoriamente")

    respuesta = int(input())

    if respuesta == 1:
        arr = sorted(arr)
    elif respuesta == 2:


        arr = sorted(arr)                       
        lista_desc = []
        while len(arr) > 0:
            num_mayor = arr[len(arr)-1]
            lista_desc.append(num_mayor)
            arr.pop(len(arr)-1)
        arr = lista_desc
        
    else:
        
        arr = random.shuffle(arr)
    return arr




print(ordenar_array(lista))

   
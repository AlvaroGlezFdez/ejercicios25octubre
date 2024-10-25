
import random



def raiz_cuadrada_entera(n):
    if n < 0:
        raise ValueError("El número no puede ser negativo.")
    if n == 0 or n == 1:  # Caso base 
        return n

   
    inicio, fin = 1, n
    while inicio <= fin:
        mid = (inicio + fin) // 2
        if mid * mid == n:
            return mid
        elif mid * mid < n:
            inicio = mid + 1
            resultado = mid  # almacena la raíz entera provisional
        else:
            fin = mid - 1

    return resultado

a = random.randint(1,2000)

print(a)
print(raiz_cuadrada_entera(a))



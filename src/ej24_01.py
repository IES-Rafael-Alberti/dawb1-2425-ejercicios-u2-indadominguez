# ejercicio 24_01

def burbuja(arr):
    """
    Ordena una lista utilizando el algoritmo de ordenamiento burbuja.

    Este algoritmo compara cada elemento con su vecino inmediato y
    los intercambia si están en el orden incorrecto. Este proceso
    se repite hasta que la lista está completamente ordenada.

    Parámetros:
    arr (list): La lista de números a ordenar.

    """
    n = len(arr)
     
    for i in range(n - 1):
         
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
              
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def burbuja_optimizado(arr):
    """
    Ordena una lista utilizando el algoritmo de ordenamiento burbuja optimizado.

    Esta versión del algoritmo burbuja incluye una verificación
    para detectar si se realizaron intercambios durante una pasada.
    Si no se realizan intercambios, significa que la lista ya está
    ordenada, y se realizan todas las iteraciones restantes.

    Parámetros:
    arr (list): La lista de números a ordenar.

    """
    n = len(arr)
 
    for i in range(n - 1):
        intercambiado = False  
   
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
               
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                intercambiado = True  
 
if __name__ == "__main__":

    lista = [64, 34, 25, 12, 22, 11, 90]
    burbuja(lista)
    print("Lista ordenada:", lista)

    lista_optimizada = [64, 34, 25, 12, 22, 11, 90]
    burbuja_optimizado(lista_optimizada)
    print("Lista ordenada (optimizada):", lista_optimizada)

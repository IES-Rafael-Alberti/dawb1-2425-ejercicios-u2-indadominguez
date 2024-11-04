# ejercicio 22_16

def mayor_numero():
    mayor = None  
    numero = None  

    print("Introduce números enteros positivos (ingresa 0 para terminar):")
    
    
    while numero != 0:
        numero = int(input("Número: "))
        
        
        if numero > 0:
            if mayor is None or numero > mayor:
                mayor = numero

    return mayor


def main():
    resultado = mayor_numero()  
    
    
    if resultado is not None:
        print("El mayor número ingresado es:", resultado)
    else:
        print("No se ingresaron números positivos.")


if __name__ == "__main__":
    main()


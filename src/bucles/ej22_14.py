# ejercicio 22_14

def numero():
    suma = 0
    numero = None  
    
    print("Introduce números enteros (ingresa 0 para terminar):")
    
    while numero != 0:
        numero = int(input("Número: "))
        
        if numero != 0:
            suma += numero
    
    return suma

def main():
    total = numero()  
    
    print("La sumatoria de todos los números ingresados es:", total)

if __name__ == "__main__":
    main()


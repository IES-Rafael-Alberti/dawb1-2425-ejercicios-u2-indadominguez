# ejercicio 22_18

def suma_digitos(numero):
    suma = 0
    
    for digito in str(numero):
        suma += int(digito)  
    return suma

def contador_pares(numeros):
    contador = 0
    for numero in numeros:
        if numero % 2 == 0:
            contador += 1
    return contador

def main():
    numeros = []   
    print("Introduce números enteros positivos (ingresa -1 para terminar):")

    numero = 0  
    
    while numero != -1:
        numero = int(input("Número: "))
 
        if numero == -1:
            continue   
        
        if numero < 0:
            print("Introduce un numero entero por favor")
            continue   

        suma = suma_digitos(numero)
        print(f"La suma de los dígitos del número {numero} es: {suma}")

        numeros.append(numero)

    total_pares = contador_pares(numeros)
    print("Se ingresaron", total_pares, "números pares.")

 
if __name__ == "__main__":
    main()


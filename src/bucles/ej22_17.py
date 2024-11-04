# ejercicio 22_17

def suma_digitos(numero):
    suma = 0
 
    for digito in str(numero):
        suma += int(digito)  
    return suma

def main():
    numero = int(input("Introduce un número entero positivo: "))

    if numero < 0:
        print("Por favor, introduce un número entero positivo.")
        return

    resultado = suma_digitos(numero)
    print(f"La suma de los dígitos del número {numero}, es: {resultado}")


if __name__ == "__main__":
    main()

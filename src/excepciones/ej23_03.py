# ejercicio 23_03

def main():
    numero = 0
    
    while numero <= 0:
        try:
            numero = int(input("Introduce un número entero positivo: "))
            if numero <= 0:
                print("El número debe ser positivo. Intenta de nuevo.")
        except ValueError:
            print("Entrada inválida. Por favor, introduce un número entero.")
    
    cuenta_atras = []

    for i in range(numero, -1, -1):
        cuenta_atras.append(i)

    print("Cuenta atrás desde", numero, "hasta 0:", ", ".join(map(str, cuenta_atras)))

if __name__ == "__main__":
    main()

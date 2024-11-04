# ejercicio 23_02

def main():
    numero = 0

    while numero <= 0:
        try:
            numero = int(input("Introduce un número entero positivo: "))
            if numero <= 0:
                print("El número debe ser positivo. Intenta de nuevo.")
        except ValueError:
            print("Entrada inválida. Por favor, introduce un número entero.")

    impares = []

    for i in range(1, numero + 1):
         
        if i % 2 != 0:
            impares.append(i)

    print("Números impares desde 1 hasta", numero, ":", ", ".join(map(str, impares)))


if __name__ == "__main__":
    main()


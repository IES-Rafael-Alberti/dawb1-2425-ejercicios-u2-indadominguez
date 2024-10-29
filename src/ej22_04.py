# ejercicio 22_04

def cuenta_atras(n):
    if n < 0:
        print("Por favor, ingresa un número entero positivo.")
        return
    resultado = ""
    for i in range(n, -1, -1):
        resultado += str(i) + (", " if i > 0 else "")
    print(resultado)

def main():
    num1 = int(input("Introduce un número entero positivo: "))
    cuenta_atras(num1)


if __name__ == "__main__":
    main()
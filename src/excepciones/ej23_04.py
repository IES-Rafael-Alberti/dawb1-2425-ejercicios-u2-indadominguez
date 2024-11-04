# ejercicio 23_04

def main():
    try:
        numero = int(input("Introduce un número entero: "))
        print(f"Has introducido el número: {numero}")
    except ValueError as e:
        print("La entrada no es correcta.")
        raise e

if __name__ == "__main__":
    main()

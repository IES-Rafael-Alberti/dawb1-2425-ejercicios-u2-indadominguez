# ejercicio 22_07

def tabla_multiplicar():
    for i in range(1, 11):
        print(f"Tabla de multiplicar del {i}:\n")
        for j in range(1, 11):
            print(f"{i} x {j} = {i * j}")
            print()

def main():

    tabla_multiplicar()


if __name__ == "__main__":
    main()
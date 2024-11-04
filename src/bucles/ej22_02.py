# ejercicio 22_02

def mostrar_años_cumplidos(edad):
    for año in range(1, edad + 1):
        print(año)

def main():
    edad_usuario = int(input("Introduce tu edad por favor: "))
    mostrar_años_cumplidos(edad_usuario)

if __name__ == "__main__":
    main() 
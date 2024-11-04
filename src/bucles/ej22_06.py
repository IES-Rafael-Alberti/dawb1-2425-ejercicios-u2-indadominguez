# ejercicio 22_06

def triangulo_rectangulo(altura_triangulo):
    for i in range(1, altura_triangulo + 1 ):
        print("*" * i)

def main():
    altura = int(input("Introduce un número entero para la altura del triángulo: "))
    triangulo_rectangulo(altura)



if __name__ == "__main__":
    main()
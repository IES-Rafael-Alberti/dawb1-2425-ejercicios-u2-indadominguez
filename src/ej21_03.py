# ejercicio 21_03

def main():

    numero1 = int(input("Introduce el primer numero: "))
    numero2 = int(input("Introduce el segundo numero: "))

    if numero2 == 0:
        print("**Error**, no se puede realizar la operación")
    else:
        resultado = numero1 / numero2
        print(f"El resultado de la división es: {resultado:.2f}")



if __name__ == "__main__":
    main()







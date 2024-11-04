# ejercicio 21_09

def main():
    edad_cliente = int(input("Introduce tu edad por favor: "))

    if edad_cliente < 4:
        print("Usted puede entrar gratis")
    elif 4 <= edad_cliente <= 18:
        print("Usted debe de pagar 5€")
    elif edad_cliente > 18:
        print("Usted debe pagar 10€")
    else:
        print("Escriba su edad")






if __name__ == "__main__":
    main()
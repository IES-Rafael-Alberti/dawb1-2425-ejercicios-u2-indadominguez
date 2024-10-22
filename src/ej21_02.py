# ejercicio 21_02

def main():

    contraseña = "cadiz cf"

    nueva_contraseña = input("Introduce una contraseña: ")

    if nueva_contraseña.lower() == contraseña.lower():
        print("La contraseña es correcta")
    else:
        print("La contraseña es incorrecta")




if __name__ == "__main__":
    main()
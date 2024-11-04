# ejercicio 23_05

def verificar_contrasena():
    contrasena_correcta = "indalecio_programa"  
    contrasena_ingresada = input("Por favor, introduce la contraseña: ")

    if contrasena_ingresada != contrasena_correcta:
        raise NameError("Incorrect Password!!")  

    print("Contraseña correcta.")

def main():
    try:
        verificar_contrasena()
    except NameError as e:
        print(e)  

if __name__ == "__main__":
    main()

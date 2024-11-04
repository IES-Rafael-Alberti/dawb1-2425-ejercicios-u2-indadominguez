# ejercicio 22_09

def verificar_contraseña(contraseña_correcta):
    contraseña_correcta_ingresada = False  

    while not contraseña_correcta_ingresada:
        contraseña_usuario = input("Introduce la contraseña: ")
        if contraseña_usuario == contraseña_correcta:
            contraseña_correcta_ingresada = True  
            print("Contraseña correcta. Acceso concedido.")
        else:
            print("Contraseña incorrecta. Inténtalo de nuevo.")

def main():
    
    contraseña_correcta = "como cuestan los ejercicios"

    
    verificar_contraseña(contraseña_correcta)


if __name__ == "__main__":
    main()
# ejercicio 22_19


def opcion():
    print("\nMenú:")
    print("1 - Comenzar programa")
    print("2 - Imprimir listado")
    print("3 - Finalizar programa")

    return int(input("Selecciona una opción (1, 2 o 3): "))

def main():
    opcion_usuario = 0

    while opcion_usuario != 3:
        opcion_usuario = opcion()   
         
        if opcion_usuario == 1:
            print("El programa ha comenzado. (Vinicius Jr, no ganará el balón de oro)")
        elif opcion_usuario == 2:
            print("Aquí está el listado: (Rodrigo Hernandez, si ganará el balón de oro)")
        elif opcion_usuario == 3:
            print("Finalizando el programa...")
        else:
            print("Por favor selecciona 1, 2 o 3.")

 
if __name__ == "__main__":
    main()



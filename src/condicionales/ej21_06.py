# ejercicio 21_06

def main():
    nombre_alumno = input("Introduce tu nombre por favor: ")
    sexo_alumno = input("Introduce tu sexo por favor: ")
    
    if sexo_alumno == "mujer" and nombre_alumno < "m":
        print("Te coresponde el grupo A") 
    elif sexo_alumno == "hombre" and nombre_alumno > "n":
        print("Te coresponde el grupo A") 
    else:
        print("Te coresponde el grupo B") 
    
    


if __name__ == "__main__":
    main()
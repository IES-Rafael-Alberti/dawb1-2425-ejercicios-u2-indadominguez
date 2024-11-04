# ejercicio 21_01

def verificar_edad(edad):
    if edad >= 18:
        return "Eres mayor de 18 años"
    else:
        return"No eres mayor de 18 años enano"

def main():
    edad = int(input("Indica tu edad por favor: "))
    print(verificar_edad(edad))

    
if __name__ == "__main__":
    main()

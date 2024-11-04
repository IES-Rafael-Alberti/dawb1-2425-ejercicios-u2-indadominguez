# ejercicio 21_05

def main():

    edad = int(input("Introduzca su edad por favor: "))
    sueldo = float(input("Introduzca su sueldo por favor: "))

    if sueldo >= 1000 and edad > 16:
        print("¡Debes tributar el impuesto!")
    else: 
        print("¡No puedes tributar el impuesto!")



if __name__ == "__main__":
    main()
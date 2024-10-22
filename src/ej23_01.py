# ejercicio 23_1

def pedir_edad() -> int:
    edad = None

    while edad == None:
        try:
            edad = int(input("Intruduzca su edad: "))

            if edad < 0:
                 raise ValueError("La edad no puede ser negativa")
            if edad == 0:
                 raise ValueError("La edad no puede ser cero")
            if edad > 125:
                 raise ValueError("La edad no puede ser mayor que 125!")

        except ValueError as e:
            print(f"**Error** {e}. Intentalo de nuevo!")

    return edad

def mostrar_anios_cumplidos(edad: int):
    for i in range(1, edad + 1):
            print(i)



def main():
    edad = pedir_edad()
    if edad != None:
         mostrar_anios_cumplidos(edad)



if __name__ == "__main__":
    main()
# ejercicio 21_07

def main():
    renta = float(input("Introduzca su renta anual: "))

    if renta < 10000:
        print("Su tipo impositivo es de 5 %")
    elif 10000 <= renta < 20000:
        print("Su tipo impositivo es de 15 %")
    elif 20000 <= renta < 35000:
         print("Su tipo impositivo es de 20 %")
    elif 35000 <= renta < 60000:
         print("Su tipo impositivo es de 30 %")
    else:
        print("Su tipo impositivo es de 45 %")
    



if __name__ == "__main__":
    main()
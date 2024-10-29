# ejercicio 22_05

def calcular_capital(cantidad_invertir, interes_anual, numero_años):
    capital = cantidad_invertir
    print("\n Capital obtenido cada año:")
    for año in range(1, numero_años + 1):
        capital *= 1 + interes_anual / 100
        print(f"Año {año}: {capital:.2f}")

def main():
    
    cantidad_invertir = float(input("Introduce la cantidad a invertir: "))
    interes_anual = float(input("Introduce el interés anual (en %): "))
    numero_años = int(input("Introduce el número de años: "))

    calcular_capital(cantidad_invertir, interes_anual, numero_años)

if __name__ == "__main__":
    main()


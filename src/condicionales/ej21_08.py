# ejercicio 21_08

def calcular_nivel_y_dinero(puntuacion):
    dinero_puntos = 2400

    if puntuacion == 0.0:
        print(f"Nivel de rendimiento: Inaceptable")
        print(f"Cantidad de dinero: 0.0")
    elif puntuacion == 0.4:
        cantidad_dinero = dinero_puntos * puntuacion
        print(f"Nivel de rendimiento: Aceptable")
        print(f"Cantidad de dinero: {cantidad_dinero:.2f}€")
    elif puntuacion >= 0.6:
        cantidad_dinero = dinero_puntos * puntuacion
        print(f"Nivel de rendimiento: Meritorio")
        print(f"Cantidad de dinero: {cantidad_dinero:.2f}€")
    else:
        print("Puntuación no válida")

def main():
    puntuacion = float(input("Ingrese su puntuación (0.0, 0.4, 0.6 o más): "))
    
    if puntuacion > 0.6:
        print("Puntuación no valida, introduce un número correto:")
        
    else:
        calcular_nivel_y_dinero(puntuacion)

if __name__== "__main__":
    main()
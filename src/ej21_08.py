# ejercicio 21_08

def calcular_nivel_y_dinero(puntuacion):
    
    dinero_por_punto = 2400
    
    
    nivel = ""
    cantidad_dinero = 0.0

    if puntuacion == 0.0:
        nivel = "Inaceptable"
        cantidad_dinero = 0.0
    elif puntuacion == 0.4:
        nivel = "Aceptable"
        cantidad_dinero = dinero_por_punto * puntuacion
    elif puntuacion >= 0.6:
        nivel = "Meritorio"
        cantidad_dinero = dinero_por_punto * puntuacion
    else:
        nivel = "Puntuación no válida"

    return nivel, cantidad_dinero

def main():
     
    puntuacion = float(input("Ingrese su puntuación (0.0, 0.4, 0.6 o más): "))
    
     
    nivel, cantidad_dinero = calcular_nivel_y_dinero(puntuacion)

     
    if nivel != "Puntuación no válida":
        print(f"Nivel de rendimiento: {nivel}")
        print(f"Cantidad de dinero a recibir: {cantidad_dinero:.2f}€")
    else:
        print(nivel)

 
if __name__ == "__main__":
    main()

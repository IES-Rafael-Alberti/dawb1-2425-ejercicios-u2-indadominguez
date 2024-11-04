# ejercicio 22_08

def hacer_fila(inicio: int) -> str:
    fila = ""
    for i in range(inicio, 0, -2):
        fila += str(i) + " "

    return fila.strip()

def hacer_triangulo(numero):
    resultado = ""
    for i in range(1, numero + 1, 2):
        resultado += hacer_fila(i) + "\n"    
        
    return resultado

def main():
    while True:
        try:
            numero = int(input("Introduce un numero entero: "))
            if numero <= 0:
                print("Por favor introduce un número válido!")
            else:
                print(hacer_triangulo(numero))
            break
        except ValueError:
            print("Entrada no válida por favor")
            

if __name__ == "__main__":
    main()
def calcular_fila(num: int) ->str:
    fila = ""
    suma = 0

    for i in range(0, num + 1, 1):
        fila += str(i)
        if i < num :
            fila += " + "
        if i == num:
            fila += " = "
        suma += i
    fila += str(suma) 
    return fila


def calcular2(num):
    resultado = ""
    for i in range(num, -1 ,-1):
        resultado += f"{i} => " + calcular_fila(i) + "\n"    
        
    return resultado


def comprobar(valor: int):
    if valor < 0:
        raise ValueError("No puede ser negativo")
    if valor > 100:
        raise ValueError("No puede ser mayor que 100")


def pedir_num():
    valor = None

    while valor == None:
        try:
            valor = int(input("Introduce un número: "))
            comprobar(valor)
        except ValueError as e:
            if valor is None:
                print("Número no valido, intentalo de nuvo: ")
            else:
                valor = None
                print(f"**ERROR** {e}, intentalo de nuevo")
    return valor

def main():
    num = pedir_num()
    print(calcular2(num))
    

if __name__ == "__main__":
    main()
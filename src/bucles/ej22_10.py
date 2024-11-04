# ejercicio 22_10

def verificar_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True


def main():
    numero = int(input("Introduce un número entero: "))
    
    if verificar_primo(numero):
        print(f"{numero} es un número primo.")
    else:
        print(f"{numero} no es un número primo.")


if __name__ == "__main__":
    main()







    
# ejercicio 22_24

def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def contar_primos():
    cantidad_primos = 0  
    numero = -1   

    while numero != 0:
        numero = int(input("Ingresa un número mayor que 1 (0 para finalizar): "))
        
        if numero > 1:
            if es_primo(numero):
                cantidad_primos += 1   

    print(f"Cantidad de números primos ingresados: {cantidad_primos}")

def main():
    contar_primos()   

if __name__ == "__main__":
    main()

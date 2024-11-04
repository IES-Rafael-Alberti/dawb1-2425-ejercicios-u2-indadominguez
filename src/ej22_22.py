# ejercicio 22_22

def contar_digitos(n):
    pares = 0
    impares = 0

    
    for digito in str(n):
        if int(digito) % 2 == 0:
            pares += 1
        else:
            impares += 1
            
    return pares, impares

def main():
    total_pares = 0  
    total_impares = 0   
    numero = -1   

    while numero != 0:   
        
        numero = int(input("Ingresa un número entero positivo (0 para finalizar): "))
        
        if numero < 0 and numero != 0:
            print("Por favor, ingresa un número entero positivo.")
            continue  

        if numero != 0:
            pares, impares = contar_digitos(numero)
             
            print(f"Número: {numero} - Dígitos pares: {pares}, Dígitos impares: {impares}")

            total_pares += pares
            total_impares += impares

    print(f"Total de dígitos pares leídos: {total_pares}")
    print(f"Total de dígitos impares leídos: {total_impares}")


if __name__ == "__main__":
    main()


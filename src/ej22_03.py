# ejercicio 22_03

def impar(numero_impar):
    
    return numero_impar % 2 != 0  

def mostrar_impares(num1):
    
    for i in range(1, num1 + 1):  
        if impar(i):  
            if i < num1:  
                print(i, end=", ")  
            else:  
                print(i)  

def main():
    
    numero = int(input("Introduce un número entero positivo: "))  
    if numero > 0:  
        mostrar_impares(numero)  
    else:
        print("Introduce un número entero positivo por favor.")  


if __name__ == "__main__":
    main()












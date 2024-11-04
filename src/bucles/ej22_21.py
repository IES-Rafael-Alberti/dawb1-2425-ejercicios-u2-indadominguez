# ejercicio 22_21

def calcular_total():
    total = 0   
    monto = None   

     
    while monto != 0:
         
        monto = float(input("Ingresa el monto de la compra (0 para finalizar): "))

         
        if monto < 0:
            print("Monto inválido. Por favor, ingresa un monto positivo.")
            continue   

         
        if monto > 0:
            total += monto

     
    if total > 1000:
        descuento = total * 0.10  
        total -= descuento  
    return total   

def main():
     
    total_a_pagar = calcular_total()

     
    print(f"El total a pagar es: ${total_a_pagar:.2f}")

 
if __name__ == "__main__":
    main()

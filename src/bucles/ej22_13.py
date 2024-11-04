# ejercicio 22_13

def main():
    texto = ""
   
    while texto.lower() != "salir":
        texto = input("Introduce un texto: ")
        
        if texto.lower() != "salir":
            print("Eco:", texto)
    
    print("Bye, bye....")

if __name__ == "__main__":
    main()
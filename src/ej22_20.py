# ejercicio 22_20

def main():
     
    frase = input("Ingresa una frase: ")
    letra_buscada = input("Ingresa una letra: ")

    encontrada = False
    
    for i in range(len(frase)):
        if frase[i] == letra_buscada:
            print(f"La letra '{letra_buscada}' se encontró en la posición {i}.")
            encontrada = True   
        else:
            print(f"No hay coincidencia en la posición {i}.")

    
    if not encontrada:
        print(f"La letra '{letra_buscada}' no se encontró en la frase.")


if __name__ == "__main__":
    main()

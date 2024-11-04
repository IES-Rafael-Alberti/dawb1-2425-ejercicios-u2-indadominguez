# ejercicio 22_12


def main():
    
    frase = input("Introduce una frase: ")
    
    letra = input("Introduce una letra: ")

    
    if len(letra) != 1:
        print("Por favor, introduce solo una letra.")
        return

    
    contador = frase.count(letra)

    
    print(f"La letra '{letra}' aparece {contador} vez/veces en la frase.")


if __name__ == "__main__":
    main()

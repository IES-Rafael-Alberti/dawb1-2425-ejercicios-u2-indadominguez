# ejercicio 22_25

def analisis_frase(frase):
    palabras = frase.split()

    if not palabras:
        return None, 0 

   
    palabra_mas_larga = ""
    for palabra in palabras:
        if len(palabra) > len(palabra_mas_larga):
            palabra_mas_larga = palabra   

    return palabra_mas_larga, len(palabras)   

def main():
    frase = input("Introduce una frase: ")
    palabra_mas_larga, cantidad_palabras = analisis_frase(frase)

    if palabra_mas_larga:
        print(f"La palabra más larga es: '{palabra_mas_larga}'")
    else:
        print("No hay palabras")

    print(f"Cantidad de palabras: {cantidad_palabras}")

if __name__ == "__main__":
    main()

# ejercicio 22_11

def palabra(palabra):
    for letra in palabra[::-1]:
        print(letra)
    
    
def main():
    palabra_escrita = input("Introduce una palabra por favor: ")

    palabra(palabra_escrita)

if __name__ == "__main__":
    main()
# ejercicio 22_23

def contar_digitos(titulos):
    return sum(c.isdigit() for titulo in titulos for c in titulo)

def titulo():
   
    total_lineas = 0   
    continuar_ingreso = True  

    while continuar_ingreso:
        lineas_digitos = 0   
        titulos = []  

        ingresar_titulos = True   

        while ingresar_titulos:
            entrada = input("Ingresa un título de libro (o '*' para finalizar, '/' para terminar línea): ")

            if entrada == "*":
                if total_lineas == 0:
                    print("Introduce lineas completas")
                print(f"Fin. Se leyeron {total_lineas} líneas completas.")
                continuar_ingreso = False   
                ingresar_titulos = False   
            elif entrada == "/":
                total_lineas += 1
                lineas_digitos += contar_digitos(titulos)
                print(f"Línea completa. Aparecen {lineas_digitos} dígitos numéricos.")
                titulos = []   
            else:
                titulos.append(entrada)   

def main():
    titulo()   

if __name__ == "__main__":
    main()

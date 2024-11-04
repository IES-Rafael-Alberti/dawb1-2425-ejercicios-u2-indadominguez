# ejercicio 21_10

def main():
    tipo_pizza = input("¿Elige una pizza vegetariana o no vegetariana? ").strip()
    
    if tipo_pizza == "Vegetariana".lower():
        
        ingrediente = input("Elige un ingrediente vegetariano (Pimiento, Tofu): ")
        ingredientes = ["Mozzarella", "Tomate", ingrediente]
        print("Tu pizza es vegetariana y lleva:", ", ".join(ingredientes))
    
    elif tipo_pizza == "No vegetariana".lower():

        ingrediente = input("Elige un ingrediente no vegetariano (Peperoni, Jamón, Salmón): ")
        ingredientes = ["Mozzarella", "Tomate", ingrediente]
        print("Tu pizza es no vegetariana y lleva:", ", ".join(ingredientes))
    
    else:
        print("Opción no válida.")


if __name__ == "__main__":
    main()
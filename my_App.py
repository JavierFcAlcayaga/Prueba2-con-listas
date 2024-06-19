from my_funciones import es_primo, es_par, mostrar_menu, obtener_numero_entero_positivo, agregar_primo_a_archivo

pares = []

while True:
    opcion = mostrar_menu()
    
    if opcion == 1:
        numero = obtener_numero_entero_positivo("Ingrese un número para verificar si es primo: ")
        
        if es_primo(numero):
            print(f"{numero} es un número primo.")
            agregar_primo_a_archivo(numero)
        else:
            print(f"{numero} no es un número primo.")

    elif opcion == 2:
        numero = obtener_numero_entero_positivo("Ingrese un número para verificar si es par o impar: ")
        if es_par(numero):
            pares.append(numero)
            sum_par = sum(pares)
            print(f"{numero} es un número par.")
        else:
            print(f"{numero} es un número impar.")

    elif opcion == 3:
        if len(pares) > 1:
            print(f"La suma de los pares ingresados hasta el momento es: {sum_par}")
        else:
            print("La cantidad de pares no alcanza para una suma") 

    elif opcion == 4:
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Intente nuevamente.")



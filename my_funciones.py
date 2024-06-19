def mostrar_menu():
    print("\nMenu de usuario:")
    print("1: Verificar si un número es primo.")
    print("2: Verificar si un número es par o impar.")
    print("3: Calcular la suma de los números pares ingresados hasta el momento.")
    print("4: Salir del programa.")

    while True:
        try:
            opcion = int(input("Seleccione una opción: "))
            if 1 <= opcion <= 4:
                return opcion
            else:
                print("Opción inválida. Intente nuevamente.")
        except ValueError:
            print("Error: Ingrese un número válido para la opción.")

def es_primo(numero):
        if numero <= 1:
            return False
        if numero <= 3:
            return True
        if numero % 2 == 0 or numero % 3 == 0:
            return False
        i = 5
        while i * i <= numero:
            if numero % i == 0 or numero % (i + 2) == 0:
                return False
            i += 6
        return True 

def es_par(numero):
    return numero % 2 == 0

def obtener_numero_entero_positivo(x):
    while True:
        try:
            numero = int(input(x))
            if numero > 0:
                return numero
            else:
                print("Por favor ingrese un número entero positivo.")
        except ValueError:
            print("Error: Ingrese un número entero válido.")

def agregar_primo_a_archivo(numero):
    nombre_archivo = "numeros_primos.txt"
    with open(nombre_archivo, 'a') as archivo:
        archivo.write(f"{numero} \n")
        archivo.close()
    print(f"El número primo {numero} ha sido agregado al archivo {nombre_archivo}.")


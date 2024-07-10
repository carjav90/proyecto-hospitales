def escribir_en_primero(texto):
    with open("primero.txt","a") as archivo_primero:
        archivo_primero.write(texto + "\n")

def leer_y_escribir_segundo():
    with open("primero.txt","r") as archivo_primero:
        lineas = archivo_primero.readlines()

    with open("segundo.txt","w") as archivo_segundo:
        for linea in lineas:
            archivo_segundo.write(linea)


if __name__== "__main__":
   while True:
    print("1. Escribir en primero.txt")
    print("2. Leer de primero.txt y escribir en segundo.txt")
    print("3. Salir")

    opcion =input("Seleccione una opcion(1/2/3): ")

    if opcion == "1":
        texto = input("Ingresa el texto para escribir en primero.txt: ")
        escribir_en_primero(texto)
        print("Texto escrito en primero.txt")
    elif opcion == "2":
        leer_y_escribir_segundo()
        print("Contenido de primero.txt escrito en segundo.txt")
    elif opcion == "3":
        break

    else:
        print("Opcion no Valida. Por Favor selecciona 1, 2 o 3")


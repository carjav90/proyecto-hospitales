import matplotlib.pyplot as plt
import pandas as pd
import csv
import json
import os
import mpld3

def guardar_info_por_fecha(data):
    info_por_fecha = {}
    for row in data:
        fecha = row["date"]
        if fecha not in info_por_fecha:
            info_por_fecha[fecha] = []
        info_por_fecha[fecha].append(row)

    # Verificamos si el archivo 'informacion.json' existe
    if not os.path.isfile("informacion.json"):
        # Si no existe, creamos un archivo JSON vacío
        with open("informacion.json", "w") as fichero:
            json.dump({}, fichero)

    # Cargamos el contenido actual del archivo JSON
    with open("informacion.json", "r") as fichero:
        contenido_actual = json.load(fichero)

    # Actualizamos el contenido con la nueva información
    contenido_actual.update(info_por_fecha)

    # Guardamos el contenido actualizado en el archivo JSON
    with open("informacion.json", "w") as fichero:
        json.dump(contenido_actual, fichero, indent=5)


def leer_json():
    if not os.path.isfile("informacion.json"):
        with open("informacion.json", "w") as f:
            json.dump({}, f)
    with open("informacion.json", "r") as f:
        return json.load(f)


def leer_csv(file):
    results = []
    with open("estadisticas.csv", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            results.append(dict(row))
        return results


def grafica(categoria, valor):
    plt.figure(figsize=(16, 16))
    plt.pie(
        valor, labels=categoria, autopct="%1.1f%%", startangle=90, labeldistance=1.1

    )
    plt.title("Grafico Salud")
    plt.axis("equal")
    plt.tight_layout()
    plt.show()

    # Guardar el gráfico en un archivo HTML
    html_fig = mpld3.fig_to_html(plt.gcf())
    with open("grafico.html", "w") as f:
        f.write(html_fig)
    print("Tu gráfica está lista ")
    plt.show()

def defunciones(datos):
    provincias = []
    defunciones = []
    for dato in datos:
        if dato["num_def"] != "0":
            provincias.append(dato["province"])
            defunciones.append(dato["num_def"])
    return provincias, defunciones

def casos(datos):
    provincias = []
    casos = []
    for dato in datos:
        if dato["new_cases"] != "0":
            provincias.append(dato["province"])
            casos.append(dato["new_cases"])
    return provincias, casos

def hospitalizados(datos):
    provincias = []
    hospitalizados = []
    for dato in datos:
        if dato["num_hosp"] != "0":
            provincias.append(dato["province"])
            hospitalizados.append(dato["num_hosp"])
    return provincias, hospitalizados

def uci(datos):
    provincias = []
    uci = []
    for dato in datos:
        if dato["num_uci"] != "0":
            provincias.append(dato["province"])
            uci.append(dato["num_uci"])
    return provincias, uci

def filtrar_por_fecha(datos_json, fecha):
    return datos_json.get(fecha, [])



while True:
    datos_csv = leer_csv("estadisticas.csv")
    guardar_info_por_fecha(datos_csv)

    print("¿Que Grafica Quieres Visualizar?")
    print("1. Defunciones")
    print("2. Casos")
    print("3. Hospitalizados")
    print("4. UCI")
    print("5. Salir")
    opcion = input("Seleccione una Opcion: ")

    if opcion in ["1", "2", "3", "4"]:
        fecha = input("Introduce la Fecha (YYYY-MM-DD): ")
        datos_json = leer_json()
        datos_fecha = filtrar_por_fecha(datos_json, fecha)

        if opcion == "1":
            categoria, valor = defunciones(datos_fecha)
            grafica(categoria, valor)
        elif opcion == "2":
            categoria, valor = casos(datos_fecha)
            grafica(categoria, valor)
        elif opcion == "3":
            categoria, valor = hospitalizados(datos_fecha)
            grafica(categoria, valor)
        elif opcion == "4":
            categoria, valor = uci(datos_fecha)
            grafica(categoria, valor)
        elif opcion == "5":
            exit()

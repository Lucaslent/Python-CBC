#Ejercicio 1
def formula(x):
    if x > 7:
        return True
    else:
        return False
def devolver_diccionario_estudiantes (lista__de_listas):
    estudiantes = []
    nombre, apellido, intentos, notas = lista__de_listas
    for i in range(len(nombre)):
        estudiante = {}
        estudiante["nombre"] = nombre[i]
        estudiante["apellido"] = apellido[i]
        estudiante["intentos"] = intentos[i]
        estudiante["notas"] = notas[i]
        estudiante["promociona"] = formula(notas[i])
        estudiantes.append(estudiante)
    return estudiantes

#Ejercicio 2
def procesar_promedio_profundidades (archivo):
    with open(archivo, "r") as archivo_csv:
        lineas = archivo_csv.readlines()
    total_profundidad = 0
    momentos = 0
    for cada_linea in lineas[1:]:
        momentos += 1
        cada_linea = cada_linea.strip().split(',')
        try:
            total_profundidad += float(cada_linea[4])
        except ValueError:
            print(f"Fecha: {cada_linea[0]}, Hora: {cada_linea[1]}, Profundidad: {cada_linea[4]}\n")
    return (total_profundidad / momentos)

#Ejercicio 3
def procesar_sospechosos (archivos):
    sospechosos = {}
    for cada_archivo in archivos:
        nombre_archivo = cada_archivo.split(".")
        try:
            with open(cada_archivo, "r") as archivo:
                lineas = archivo.readlines()
            for cada_linea in lineas:
                cada_linea = cada_linea.strip().split(";")
                if nombre_archivo[0] in sospechosos:
                    try:
                        sospechosos[nombre_archivo[0]] += float(cada_linea[2])
                    except ValueError:
                        print(f"El sospechoso {nombre_archivo[0]} tiene un error!\n")
                else:
                    try:
                        sospechosos[nombre_archivo[0]] = float(cada_linea[2])
                    except ValueError:
                        print(f"El sospechoso {nombre_archivo[0]} tiene un error!\n")
        except FileNotFoundError:
            print(f"El archivo del sospechoso {nombre_archivo[0]} no existe!!")
    return (sospechosos)

#Ejercicio 4
empleados = {
    "apellido" : ['Perez', 'Sanches','Gomez','Quilpe'],
    "nombre" : ['Malena','Sergio','Carla','Jose'],
    "año_ingreso" : [2008, 2015, 2023, 2022],
    "salario_al_ingreso" : [700000, 450000, 300000, 600000]
}

import pandas as pd
empleados_df = pd.DataFrame(empleados)
empleados_df["salario_actual"] = (empleados_df["salario_al_ingreso"] + (empleados_df["salario_al_ingreso"] * 0.5 * (2024 - empleados_df["año_ingreso"])))
empleados_copia = empleados_df.copy()
empleados_por_abajo_canasta = empleados_copia[empleados_copia["salario_actual"] < 851351]
empleados_por_abajo_canasta["salario_nuevo"] = (empleados_por_abajo_canasta["salario_actual"] * 4)

import numpy as np
import matplotlib.pyplot as plt

bucle_chico = np.arange(2, 24, 2)
bucle_grande = np. arange(5, 35, 5)

fuerza_centripeta_1 = ((300 * (27.78**2)) / bucle_chico)
fuerza_centripeta_2 = ((300 * (27.78**2)) / bucle_grande)

fig, ax  = plt.subplots()
ax.plot(bucle_chico, fuerza_centripeta_1, label= 'm=300kg, v=27.78m/s')
ax.plot(bucle_grande, fuerza_centripeta_2, label = 'm=300kg, v=27.78m/s')
ax.set_title("Fuerza centripeta segun radio")
ax.set_xlabel("radio")
ax.set_ylabel("fuerza centripeta")
ax.legend()

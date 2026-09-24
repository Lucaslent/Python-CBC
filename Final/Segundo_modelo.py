#Ejercicio 1
def corregir_errores (Archivo_con_errores, errores):
    palabras = {}
    with open(Archivo_con_errores, "r") as archivo_viejo:
        lineas = archivo_viejo.readlines()
    with open("Corregido.txt", "w") as archivo_nuevo:
        for cada_linea in lineas:
            cada_linea = cada_linea.strip().split(" ")
            for cada_palabra in cada_linea:
                for clave, valor in errores.items():
                    if clave in cada_palabra:
                        cada_palabra = cada_palabra.replace(clave,valor)
                archivo_nuevo.write(f"{cada_palabra} ")
            archivo_nuevo.write("\n")
    with open("Corregido.txt", "r") as archivo:
        lineas = archivo.readlines()
        for cada_linea in lineas:
            cada_linea = cada_linea.strip().split()
            for cada_palabra in cada_linea:
                if len(cada_palabra) >= 4:
                    if cada_palabra in palabras:
                        palabras[cada_palabra] += 1
                    else:
                        palabras[cada_palabra] = 1
    return palabras

#Ejercicio 2
def analizar_ventas (autores):
    ganancias = {}
    for autor in autores:
        nombre = autor.split(".")
        ganancia_total = 0
        with open(autor, "r") as archivo:
            lineas = archivo.readlines()
        for cada_linea in lineas:
            cada_linea = cada_linea.strip().split("-")
            try:
                ganancia_total += (float(cada_linea[1]) * (float(cada_linea[2])))
            except ValueError:
                print(f"El libro '{cada_linea[0]}' contiene un error! ")
        
        if nombre[0] in ganancias:
            ganancias[nombre[0]] += ganancia_total
        else:
            ganancias[nombre[0]] = ganancia_total
    return ganancias

#Ejercicio 3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
partidas = pd.read_csv("control_calidad_aceite.csv", sep=";")

extra_virgen = partidas[partidas["porcentaje_acidez"] < 0.8]
virgen = partidas[(partidas["porcentaje_acidez"] > 0.8) & (partidas["porcentaje_acidez"] < 2)]
lampante = partidas[partidas["porcentaje_acidez"] > 2]

extra_virgen["calidad"] = "extra_virgen"
virgen["calidad"] = "virgen"
lampante["calidad"] = "lampante"

acidez = partidas["porcentaje_acidez"].to_numpy()
indice_calidad = 100 - acidez * 0.25
print(np.mean(indice_calidad))
print(np.max(indice_calidad))
print(np.min(indice_calidad))

fig, ax = plt.subplots()
ax.bar(partidas["partida"], indice_calidad)
ax.set_title("Índice de calidad por partida")
ax.set_xlabel("Partidas")
ax.set_ylabel("Índices de calidad")
plt.show()
 






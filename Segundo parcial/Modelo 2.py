#A
def devolver_informacion_paises (ruta_archivo):
    informacion_paises = []
    with open(ruta_archivo, "r") as archivo:
        lineas = archivo.readlines()
    for cada_linea in lineas[1:]:
        cada_linea = cada_linea.strip().split(";")
        pais = {
            "pais" : cada_linea[0] ,
            "energia_solar_gwh": cada_linea[1] ,
            "cant_eolica_gwh": cada_linea[2] ,
            "cant_hidraulica_gwh": cada_linea[3]
             
        }
        informacion_paises.append(pais)

#B
def devolver_altura_promedio (nombre_archivo):
    try:
        with open(nombre_archivo) as archivo:
            lineas = archivo.readlines()
            error_invalidos = 0
            total = len(lineas)
            suma = 0
        for cada_linea in lineas:
            cada_linea = cada_linea.strip()
            try:
                suma += float(cada_linea)
            except ValueError:
                error_invalidos += 1
        total_sin_errores = error_invalidos - total
        try:
            promedio = suma / total_sin_errores
        except ZeroDivisionError:
            promedio = 0
            print("No se puede dividir por cero")
        return promedio 
    except FileNotFoundError:
        print("Archivo no encontrado!")

#C
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,11,0.5)
ep = (0.5 * 0.15 * x**2)
fig,ax = plt.subplots()
ax.plot(x,ep,label="k = 0,15 N/m")
ax.set_title("Grafico de energia potencial elastica")
ax.set_xlabel("Distacia metros")
ax.set_ylabel("Energia potencial")
ax.grid()
ax.legend()
plt.show()

import pandas as pd
df = pd.DataFrame("archivo.csv")
df["Valor_total"] = df["precio_unitario"] * df["stock"]
df["Disponible"] = df[df["stock"]> 0]
df[(df["Disponible"] == True) & (df["Valor_total"]>20000)].sort_values(by=["Valor_total"], ascending=False)





import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#A
def obtener_tupla (ruta_archivo):
    with open(ruta_archivo, "r") as archivo:
        lineas = archivo.readlines()
        lineas = lineas[1:]
    artistas = {}
    reproducciones_totales = 0
    cant_artistas = 0
    for cada_linea in lineas:
        cada_linea = cada_linea.strip().split(";")
        reproducciones_totales += int(cada_linea[1])
        if cada_linea[0] not in artistas:
            cant_artistas += 1
            artistas[cada_linea[0]] = float(cada_linea[1])
        else:
            artistas[cada_linea[0]] += float(cada_linea[1])

    promedio = reproducciones_totales / cant_artistas
    return(artistas, promedio)

#B
def devolver_analisis_de_archivo (ruta_archivo):
    analisis_final = []
    with open(ruta_archivo, "r") as archivo:
        lineas = archivo.readlines()
    informacion_separada = {}    
    for cada_linea in lineas[1:]:
        informacion_separada = {} 
        cada_linea = cada_linea.strip().split(";")
        try:
            eficiencia_energetica = (float(cada_linea[3]))/(float(cada_linea[2]))
        except TypeError:
            print(f"El modelo {cada_linea[0]} contiene informacion erronea!")
            continue
        try:
            if cada_linea[4] > "2024/06/27":
                informacion_separada["Modelo"] = cada_linea[0]
                informacion_separada["Eficiencia_energetica"] = eficiencia_energetica
                informacion_separada["fecha_analisis"] = cada_linea[4]
            else:
                print("No cumple con la fecha requerida!")
        except TypeError:
            print(f"El modelo {cada_linea[0]} contiene informacion erronea!")
            continue
    analisis_final.append(informacion_separada)

    with open("analisis_modelo_ia.txt", "w") as archivo_txt:
        archivo_txt.write("modelo;eficiencia_energetica;fecha-analisis/n")
        for cada_parte in analisis_final:
            archivo_txt.write(
                  f"{cada_parte['Modelo']};{cada_parte['Eficiencia_energetica']:.2f};{cada_parte['fecha_analisis']}/n"
            )

#C
#Inciso A
x = np.arange(0,51)
y1 = 10 * (1 - np.e ** (-0.1 * x))
y2 = 10 * (1 - np.e ** (-0.2 * x))

fig, ax = plt.subplots()
ax.plot(x,y1, label = "K = 0,1")
ax.plot(x,y2, label = "K = 0,2")
ax.set_title("Velocidad descenso")
ax.set_xlabel("tiempo")
ax.set_ylabel("velocidad en funcion del tiempo")
plt.legend()
#plt.show()

#Inciso B
df = pd.DataFrame("futbolistas")
df["años_club"] = 2026- df["ingreso_club"]
promedio_goles = df["cantidad_goles_club"] / df["años_club"]
goleadores = []
for x in df["promedio_goles"]:
    if x >= 5:
        goleadores.append("Si")
    else:
        goleadores.append("No")
df["goleador"] = goleadores
df.sort_values(by=df["años_club"], ascending =False)





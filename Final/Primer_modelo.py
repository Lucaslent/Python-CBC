#1
def clasificar_materias (materias):
    creditos_totales = 0
    cant_materias = 0
    cant_alta = 0
    cant_media = 0
    cant_baja = 0
    for cada_materia in materias:
        creditos_totales += cada_materia["creditos"]
        cant_materias += 1
        if cada_materia["creditos"] <= 2 :
            cant_baja += 1
            print(f"Materia: {cada_materia["materia"]}, Creditos:{cada_materia["creditos"]} --> Clasificacion: Baja")
        elif cada_materia["creditos"] < 6 and cada_materia["creditos"] > 2:
            cant_media += 1
            print(f"Materia: {cada_materia["materia"]}, Creditos:{cada_materia["creditos"]} --> Clasificacion: Media")
        else:
            cant_alta += 1
            print(f"Materia: {cada_materia["materia"]}, Creditos:{cada_materia["creditos"]} --> Clasificacion: Alta") 
    nuevo_diccionario = {
        "creditos_totales" : (creditos_totales),
        "promedio": int(creditos_totales / cant_materias),
        "porc_carga_baja": ((100 * cant_baja)/cant_materias),
        "porc_carga_media": ((100 * cant_media)/cant_materias),
        "porc_carga_alta": ((100 * cant_alta)/cant_materias)
    }
    return(print(nuevo_diccionario))

#2
import pandas as pd
def devolver_analisis (archivo):
    operaciones_totales = 0
    operaciones_validas = 0
    operaciones_observacionales = 0
    confiable = None
    errores = 0
    with open(archivo, "r") as archivo:
        lineas = archivo.readlines()
    for cada_linea in lineas[1:]:
        operaciones_totales += 1
        cada_linea = cada_linea.strip().split(";")
        try:
            int(cada_linea[2])
            int(cada_linea[3])
            operaciones_validas += 1
        except ValueError:
            errores += 1
        if cada_linea[4] != "-":
            operaciones_observacionales += 1
    pureza = ((operaciones_validas * 100 ) / operaciones_totales)
    if pureza >= 75:
        confiable = True
    else:
        confiable = False
    nueva_informacion = {
        "Concepto" : "valor",
        "Operaciones totales" : (operaciones_totales),
        "Operaciones validas" : (operaciones_validas),
        "Operaciones con observaciones" : (operaciones_observacionales),
        "Porcentaje de pureza de la informacion" : (f"{int(pureza)}%"),
        "Datos confiables" : (confiable)
    }
    with open("reporte_inventario.csv", "w") as nuevo_archivo:
        for clave,valor in nueva_informacion.items():
            nuevo_archivo.write(f"{clave};{valor}\n")

#3
def devolver_estadisticas (archivos_mensuales):
    total_inscripciones = 0
    horas_donadas_validas = 0
    lineas_validas = 0
    cant_voluntarios_destacados = 0
    errores = 0
    for archivo_mensual in archivos_mensuales:
        with open(archivo_mensual, "r") as archivo:
            lineas = archivo.readlines()
        for cada_linea in lineas[1:]:
            total_inscripciones += 1
            linea_separada = cada_linea.strip().split(";")
            try:
                int(linea_separada[3])
                horas_donadas_validas += (int(linea_separada[3]))
                lineas_validas += 1
                if int(linea_separada[3]) >= 10:
                    cant_voluntarios_destacados += 1
            except ValueError:
                errores += 1
                with open("analisis_pendiente.csv", "w") as analisis_pendiente:
                    analisis_pendiente.write(f"{cada_linea}\n")

    with open("estadisticas_voluntarios.txt", "w") as nuevo_archivo:
        nuevo_archivo.write(f"Total inscripciones: {total_inscripciones}\n")
        nuevo_archivo.write(f"Promedio horas: {round((horas_donadas_validas / lineas_validas), 2)}\n")
        nuevo_archivo.write(f"Porcentaje de destacados: {round((100 * cant_voluntarios_destacados) / lineas_validas, 2)}% \n")
        nuevo_archivo.write(f"Porcentaje errores: {round((errores / total_inscripciones) * 100, 2) }% \n")
 
#4 - Inciso 1
estudiantes = {
    "apellido": ["Perez", "Sanchez", "Gomez", "Quilpe"],
    "nombre": ["Mariana", "Lucia", "Carla", "Jose"],
    "carrera": ["Quimica", "Informática", "Mecánica", "Industrial"],
    "año_ingreso": [2014, 2015, 2012, 2017],
    "materias_aprobadas": [42, 45, 20, 3],
    "materias_totales": [55, 60, 55, 47],
    "plan_nuevo": [False, False, False, False],
    "genero": ["F", "F", "X", "M"],
    "mail_fiuba": ["mperez@fi.uba.ar", None, "lsanchez@fi.uba.ar", None]
}
df = pd.DataFrame(estudiantes)
df["Porc_pendiente"] = (((df["materias_totales"] - df["materias_aprobadas"])* 100 ) / df["materias_totales"])
falta_terminar = df[df["Porc_pendiente"] >= 40]
candidatos = falta_terminar[(falta_terminar["mail_fiuba"].notna()) & ((2023 - falta_terminar["año_ingreso"]) > 10)].copy()
candidatos.loc[:,"plan_nuevo"] = True
df.loc[candidatos.index , "plan_nuevo"] = True
df.sort_values("carrera", ascending=False)

#4 - Inciso 2

import matplotlib.pyplot as plt

No_tienen_mail = df[df["mail_fiuba"].isna()]
tienen_mail = df[df["mail_fiuba"].notna()]

datos = [len(No_tienen_mail), len(tienen_mail)]
nombres = ["No tienen mail", "Tienen mail"]

fig, ax = plt.subplots()
ax.pie(datos, labels=nombres, autopct='%1.1f%%')
ax.set_title("Tiene Mail")
plt.show()
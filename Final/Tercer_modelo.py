#Ejercicio 1
def clasificar_materias (informacion_materias):
    cant_materias = 0
    porc_total_aprobados = 0
    cant_baja = 0
    cant_media = 0
    cant_alta = 0
    for cada_materia in informacion_materias:
        cant_materias += 1
        porc_aprobados = ((cada_materia["aprobados"] * 100) / cada_materia["anotados"])
        porc_total_aprobados += porc_aprobados
        if porc_aprobados <= 25:
            clasificacion = "BAJA"
            cant_baja += 1
        elif porc_aprobados > 25 and porc_aprobados < 50:
            clasificacion = "MEDIA"
            cant_media += 1
        else:
            clasificacion = "ALTA"
            cant_alta += 1
        print(f"Materia: {cada_materia["materia"]}, aprobacion: {porc_aprobados}% --> clasificacion: {clasificacion}")
    nueva_informacion = {
        "cant_materias_analizadas" : cant_materias ,
        "promedio_porcentaje" : (porc_total_aprobados / cant_materias) ,
        "porc_aprob_baja" : ((cant_baja * 100) / cant_materias),
        "porc_aprob_media" : ((cant_media * 100) / cant_materias),
        "porc_aprob_alta" : ((cant_alta * 100) / cant_materias)
    }
    return nueva_informacion

#Ejercicio 2 
def devolver_estadisticas (archivo):
    with open(archivo, "r") as archivo_dia:
        lineas = archivo_dia.readlines()
    cant_operaciones = 0
    registros_sin_error = 0
    errores = 0
    operaciones_ordenadas = 0
    datos_sucios = None
    for cada_linea in lineas[1:]:
        cant_operaciones += 1
        cada_linea = cada_linea.strip().split(";")
        try:
            int(cada_linea[2]) and float(cada_linea[3])
            registros_sin_error += 1
        except ValueError:
            errores += 1
        if cada_linea[4] == "-":
            operaciones_ordenadas += 1
    porc_errores = ((errores * 100) / cant_operaciones)
    if porc_errores >= 50:
        datos_sucios = True
    else:
        datos_sucios = False
    with open("reporte_inventario.csv", "w") as nuevo_archivo:
        nuevo_archivo.write("concepto;valor\n")
        nuevo_archivo.write(f"operaciones totales;{cant_operaciones}\n")
        nuevo_archivo.write(f"operaciones validas;{registros_sin_error}\n")
        nuevo_archivo.write(f"operaciones ordenadas;{operaciones_ordenadas}\n")
        nuevo_archivo.write(f"porcentaje errores;{int(porc_errores)}%\n")
        nuevo_archivo.write(f"datos sucios;{datos_sucios}")

#Ejercicio 3
def analizar_archivos_mensuales (archivos):
    horas_donadas_totales_validas = 0
    total_inscripciones = 0
    lineas_sin_errores = 0
    apariciones_por_persona = {}
    destacados = 0
    for cada_archivo in archivos:
        with open(cada_archivo, "r") as archivo:
            lineas = archivo.readlines()
        for cada_linea in lineas[1:]:
            cada_linea_separada = cada_linea.strip().split(";")
            total_inscripciones += 1
            try:
                float(cada_linea_separada[3])
                horas_donadas_totales_validas += float(cada_linea_separada[3])
                lineas_sin_errores += 1
            except ValueError:
                with open('analisis_pendiente.csv', 'a') as archivo_csv:
                    archivo_csv.write(cada_linea)
                
            if cada_linea_separada[2] in apariciones_por_persona:
                    apariciones_por_persona[cada_linea_separada[2]] += 1
            else:
                apariciones_por_persona[cada_linea_separada[2]] = 1
    for clave, valor in apariciones_por_persona.items():
        if valor >= 2:
            destacados += 1
    with open("estadisticas_voluntarios.txt", "w") as nuevo_archivo:
        nuevo_archivo.write(f"suma_horas: {round(horas_donadas_totales_validas,1)}\n")
        nuevo_archivo.write(f"destacados: {destacados}\n")
        nuevo_archivo.write(f"porcentaje_sin_errores: {round(lineas_sin_errores / total_inscripciones * 100,2)}%\n")
        nuevo_archivo.write(f"cant_donaciones_voluntarios: {apariciones_por_persona}")

#Ejercicio 4
import pandas as pd
estudiantes = estudiantes = {
    "apellido": ["Perez", "Sanchez", "Gomez", "Quilpe"],
    "nombre": ["Mariana", "Lucia", "Carla", "Jose"],
    "carrera": ["Quimica", "Informática", "Mecánica", "Industrial"],
    "año_ingreso": [2014, 2015, 2012, 2017],
    "creditos": [142, 45, 120, 35],
    "creditos_totales": [231, 226, 250, 236],
    "plan_nuevo": [True, True, True, True],
    "genero": ["F", "F", "X", "M"],
    "mail_fiuba": ["mperez@fi.uba.ar", None, "lsanchez@fi.uba.ar", None]
}
estudiantes_df = pd.DataFrame(estudiantes)
estudiantes_df["porc_creditos"] = ((estudiantes_df["creditos"] * 100) / estudiantes_df["creditos_totales"])
personas_por_terminar_df = estudiantes_df[estudiantes_df["porc_creditos"] >= 64].copy()
personas_a_cambiar_df = personas_por_terminar_df[(personas_por_terminar_df["mail_fiuba"].isnull()) & ((2023 - personas_por_terminar_df["año_ingreso"]) < 5)].copy()
estudiantes_df.loc[personas_a_cambiar_df.index, "plan_nuevo"] = False
personas_a_cambiar_df["plan_nuevo"] = False
estudiantes_df.sort_values("apellido", ascending=True)

#Ejercicio 4 - 2
import matplotlib.pyplot as plt
nuevo_plan = estudiantes_df["plan_nuevo"] == True
viejo_plan = estudiantes_df["plan_nuevo"] == False
datos = (nuevo_plan.sum(), viejo_plan.sum())
fig, ax = plt.subplots()
ax.pie(datos, labels=["si", "no"], autopct='%1.1f%%')
ax.set_title = "Tienen plan nuevo"

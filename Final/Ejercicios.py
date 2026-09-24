def resolver_necesidad (diccionarios):
    lista_aprobados_sin_promocionar = []
    lista_aprobados_promocionando = []
    personas = 0
    desprobados = 0
    for i in range(len(diccionarios)):
        personas += 1
        estudiante = diccionarios[i]
        if estudiante["nota1"] >= 7 and estudiante["nota2"] >= 7:
            lista_aprobados_promocionando.append(f"{estudiante["nombre"]}, {estudiante["apellido"]}")
        elif (estudiante["nota1"] < 7 and estudiante["nota1"] >= 4) and (estudiante["nota2"] < 7 and estudiante["nota2"] >= 4):
            lista_aprobados_sin_promocionar.append(f"{estudiante["nombre"]}, {estudiante["apellido"]}")
        elif estudiante["nota1"] < 4 or estudiante["nota2"] < 4:
            desprobados += 1
    tupla_final = (f'{lista_aprobados_sin_promocionar},{lista_aprobados_promocionando},{((desprobados * 100) / personas)}%')
    return (tupla_final)

import pandas as pd
empleados = empleados = {
    "apellido": ['Perez', 'Sanchez', 'Gomez', 'Quilpe'],
    "nombre": ['Mariana', 'Lucia', 'Carla', 'Jose'],
    "año_ingreso": [2008, 2015, 2023, 2022],
    "salario_al_ingreso": [700000, 450000, 300000, 600000],
    "salario_hoy": [790000, 650000, 800000, 680000]
}
empleados_df = pd.DataFrame(empleados)
empleados_con_mas_aumento = empleados_df[(((empleados_df["salario_al_ingreso"] + empleados_df["salario_hoy"]) / 2) - empleados_df["salario_al_ingreso"]) >= 100000]
empleados_por_debajo_de_la_linea_de_pobreza = empleados_df.copy()
empleados_por_debajo_de_la_linea_de_pobreza = empleados_por_debajo_de_la_linea_de_pobreza[empleados_por_debajo_de_la_linea_de_pobreza["salario_hoy"] < 939887]
empleados_df["bajo_linea_de_pobreza"] = True
empleados_df.loc[empleados_por_debajo_de_la_linea_de_pobreza.index,"bajo_linea_de_pobreza"] = False

import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 100, 1000)
formula_resorte_1 = 0.5 * 0.10 * (x)**2
formula_resorte_2 = 0.5 * 0.45 * (x)**2

fig, ax = plt.subplots()
ax.plot(x,formula_resorte_1, label="k = 0.10 N/M")
ax.plot(x, formula_resorte_2, label="K = 0.45 N/M")
ax.legend()
ax.set_title("Energia potencial elastica")
ax.set_xlabel("Metros")
ax.set_ylabel("EP")

def listas_facturas_pagas (diccionarios):
    for cada_diccionario in diccionarios:
        if cada_diccionario["pagada"] == True:
            print(cada_diccionario["numero"],cada_diccionario["fecha"],cada_diccionario["proveedor"],cada_diccionario["monto"])
            
def pagar_facturas_proveedor (diccionarios, proveedor):
    for cada_diccionario in diccionarios:
        if cada_diccionario["proveedor"] == proveedor:
            cada_diccionario["pagada"] = True
        
    return diccionarios

q = np.linspace(1000,10000,5000)
costo_decreciente = (500 + 200 * q - 10 * (q)**2)
costo_creciente = (100 * q + 50 * (q)**1.5)

fig,ax = plt.subplots()
ax.scatter(q, costo_decreciente,label="Costo decreciente")
ax.scatter(q, costo_creciente,label="Costo creciente")
ax.grid()
ax.legend()
ax.set_title("Costos segun Q")
ax.set_xlabel("Variable Q")
ax.set_ylabel("Costos")

fig, ax = plt.subplots()
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
valor1 = len(df["mail_fiuba"].isnull())
valor2 = len(df["mail_fiuba"].notnull())
valores = (valor1, valor2)
nombres = ["No tienen mail", "Tienen mail"]
ax.pie(valores, labels=nombres, autopct='%1.1f%%')
ax.set_title("Tiene mai")

fig, bc = plt.subplots()
apellidos = df["apellido"]
porcentajes = (((df["materias_totales"] - df["materias_aprobadas"]) * 100 ) / df["materias_totales"])
bc.bar(apellidos, porcentajes)
bc.grid()
bc.set_title("porcentaje completado de la carrera")
bc.set_ylabel("Porcentaje")
plt.show()
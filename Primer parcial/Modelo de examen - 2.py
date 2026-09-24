#Ejercicio 1

def Simular_viaje (cant_nafta):
    tramos = []
    horas_recorridas = 0
    tramo_total = 0
    if cant_nafta >= 15:
        print(f"INICIANDO SIMULACIÓN - Nafta incial {cant_nafta} litros!")
        while cant_nafta > 14:
            #tramo = random.randint (10,50)
            #tramos.append(tramo)
            horas_recorridas += 1
            #consumo = (0.1 / tramo)
            #cant_nafta -= consumo
            #print(f"Tramo recorrido: {tramo}km!- Nafta restante: {cant_nafta} litros!")
        print("Atencion! La nafta esta llegando al nivel critico. Por favor, busque una estacion de servicio!")
        for lista_tramo in tramos:
            tramo_total += lista_tramo
        velocidad_promedio = (tramo_total / horas_recorridas)
        print(f"--- Resumen del viaje ---")
        print(f"Distacia total recorrida: {tramo_total}km!")
        print(f"Tiempo total empleado: {horas_recorridas} horas!")
        print(f"Velocidad promedio: {velocidad_promedio} km/h!")
        print(f"Nafta promedio: {cant_nafta} litros!")
    else:
        print("Error! Nafta insuficiente para la simulacion")

#Ejercicio 2

def Determinar_usario_mayor_horas (usuarios):
    mayor_hora = 0
    mayor_usuario = None
    for usuario in usuarios:
        if usuario[1] > mayor_hora:
            mayor_hora = usuario[1]
            mayor_usuario = usuario
    return (tuple(mayor_usuario[0], mayor_usuario[2]))

#Ejercicio 3
# 1-
def Es_posible_cubrir (espacios_a_fumigar, cuadrillas):
    cant_espacios_verdes = 0
    cant_cuadrillas = 0
    for espacio in espacios_a_fumigar:
        cant_espacios_verdes += espacio[1]
    for cuadrilla in cuadrillas:
        cant_cuadrillas += cuadrilla[1]
    if cant_cuadrillas == cant_espacios_verdes:
        return True
# 2-
def Devolver_mayor_capacidad (cuadrillas):
    lista_cuadrillas = []
    for cuadrilla in cuadrillas:
        lista_cuadrillas.append(cuadrilla)
    lista_cuadrillas.sort(reverse=True)
    return (tuple(lista_cuadrillas[0:2]))


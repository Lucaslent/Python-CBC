#EJERCICIO 1
def donar():
    donaciones = []
    primera_donacion = input("Bienvenido! Que desea donar ?: ")
    cosas_donadas = []
    cant_donada = 0
    donacion = None
    if primera_donacion != "*":
        donaciones.append(primera_donacion)
        while donacion != "*":
            donacion = input("Muchas gracias! Que mas desea donar ?: ")
            donaciones.append(donacion)
    for donacion in donaciones:
        partes = donacion.split("-")
        cosas_donadas.append(partes[1])
        cant_donada += int(partes[0])
    print(f"Muchas gracias! Usted ha donado {cosas_donadas}!")
    return cant_donada
#EJERCICIO 2
def devolver_finalistas (participantes):
    puntuaciones = []
    finalistas = []
    promedio_puntuacion = 0
    for participante in participantes:
        if participante[1] > 80:
            finalistas.append(participante[0])
            puntuaciones.append(participante[1])
    for puntuacion in puntuaciones:
        promedio_puntuacion += puntuacion
    if (len(puntuaciones))>0:
        promedio_puntuacion = (promedio_puntuacion / (len(puntuaciones)))
    return (tuple(finalistas, promedio_puntuacion))
#EJERCICIO 3
def hallar_vectores (ejercicios):
    vectores = []
    for ejercicio in ejercicios:
        if ((ejercicio[0]*ejercicio[3])+(ejercicio[1]*ejercicio[2])) == 0:
            vectores.append(ejercicio)
    return vectores


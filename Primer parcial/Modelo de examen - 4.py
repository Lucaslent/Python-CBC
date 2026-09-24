def convertir_kcal_en_joules ():
    print("Hola! Esto es una conversión de kcal a joules...")
    entrada = input('Ingrese un valor kcal o "X" para salir: ')
    joules = None

    while entrada.upper != "X":
        entrada = numero
        if (int(numero)) > 0:
            numero = input('Ingrese un valor kcal o "X" para salir: ')
            joules = (int(numero) * 4184)
            print(f"{numero} kcal = {joules} J")
        elif (int(numero)) < 0:
            print("Error: Las kilocalorías no pueden ser negativas")
    
#EJERCICIO 2
def calcular_lote (productos):
    lotes = []
    for nombre, fecha in productos:
        partes = fecha.split("/")
        año = int(partes[2])
        if año < 26:
            lote = "A1"
        elif año < 27:
            lote = "A2"
        else:
            lote = "A3"
        lotes.append((nombre, fecha, lote))
    return lotes

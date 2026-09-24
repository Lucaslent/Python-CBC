#EJERCICIO 1

def Despachar (cant_camiones):
    lista_a_despachar = []
    vueltas = 0
    while vueltas < cant_camiones:
        codigo_de_producto = input("Ingrese un código de producto: ")
        if len(codigo_de_producto) != 4:
            print("El codigo debe tener 4 caracteres!")
        elif codigo_de_producto not in lista_a_despachar:
            print("El codigo fue guardado correctamente!")
            lista_a_despachar.append(codigo_de_producto)
            vueltas +=1
        else:
            print("El codigo ya ha sido ingresado anteriormente!")
    return lista_a_despachar
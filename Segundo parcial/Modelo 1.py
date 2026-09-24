#A
def obtener_lista_diccionarios (lista_productos):
    productos = []
    for cada_producto in lista_productos:
        producto = {}
        archivo = open(cada_producto, "r")
        linea = archivo.readline()
        while linea != "":
            linea_limpia = linea.strip().split(": ")
            if len(linea_limpia) == 2:
                producto[linea_limpia[0]] = [linea_limpia[1]]
        archivo.close()
    productos.append(producto)
    return productos

#B
#import pandas as pd
#def devolver_informacion_produccion_por_producto (lista_archivos):
    for produccion_diaria in lista_archivos:
        try:
            df = pd.read_csv(produccion_diaria)
            productos = {}
            for i in range(len(df)):
                df.iloc[[i]]

        except FileNotFoundError:
            print("El archivo no existe!")
    
import pandas as pd

df = pd.DataFrame({
    'Nombre': ['Ana', 'Juan'],
    'Edad': [25, 30]
})

for i in range(len(df)):
    # Imprime el índice y el nombre en cada fila
    print(f"Fila {i}: {df.iloc[i]['Nombre']}")


        




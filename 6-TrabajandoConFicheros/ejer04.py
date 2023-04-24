import json
import os
import random

# Definición de la lista de ciudades
NombreCiudades = {"Madrid", "Barcelona", "Sevilla", "Malaga", "Cordoba", "Toledo", "Valencia", "Bilbao", "Salamanca", "Palma", "Caceres", "Segovia", "Zaragoza", "Cuenca", "Alicante", "Las Palmas", "Avila", "Merida", "Granada", "Murcia"}

# Definición de funciones

def generar_diccionario():
    """
    Genera un diccionario aleatorio de ciudades con su temperatura media anual y lo almacena en un archivo.
    """
    ciudades = {}
    for ciudad in NombreCiudades:
        media_temperaturas = sum([random.randint(-10, 40) for _ in range(12)])
        ciudades[ciudad] = round(media_temperaturas / 12,2)
    with open("ciudades.json", "w") as f:
        json.dump(ciudades, f)
    print("Diccionario de ciudades generado y almacenado en el archivo 'ciudades.json'.")
    return ciudades

def cargar_diccionario():
    """
    Carga el diccionario de ciudades desde el archivo 'ciudades.json', si existe.
    Si no existe el archivo, genera un nuevo diccionario aleatorio y lo almacena en el archivo.
    """
    if os.path.exists("ciudades.json"):
        with open("ciudades.json", "r") as f:
            ciudades = json.load(f)
        print("Diccionario de ciudades cargado desde el archivo 'ciudades.json'.")
    else:
        generar_diccionario()
        with open("ciudades.json", "r") as f:
            ciudades = json.load(f)
    return ciudades

def ciudad_con_temperatura_extrema(ciudades, op):
    """
    Busca la(s) ciudad(es) con la temperatura media anual más alta o más baja, según la opción 'op'.
    """
    if op == "alta":
        extrema = max(ciudades.values())
    elif op == "baja":
        extrema = min(ciudades.values())
    ciudades_extremas = [k for k, v in ciudades.items() if v == extrema]
    return ciudades_extremas

def ciudades_ordenadas_por_temperatura(ciudades):
    """
    Devuelve todas las ciudades en orden descendente de temperatura media anual.
    """
    #El método sorted() y la función items() del diccionario ciudades se usan para crear una lista
    #de tuplas donde cada tupla contiene el par (clave, valor) del diccionario. 
    #Luego, se utiliza la opción key para indicar que el criterio de ordenamiento debe ser 
    #el valor (x[1]) de la tupla. 
    #La función lambda se utiliza para definir una función anónima que toma una tupla como entrada 
    #y devuelve su segundo elemento (x[1]). 
    #Por último, se utiliza la opción reverse=True para que el ordenamiento sea descendente. 
    #El resultado es una lista de tuplas ordenadas por la temperatura media anual

    ciudades_ordenadas = sorted(ciudades.items(), key=lambda x: x[1], reverse=True)
    #ciudades_ordenadas_con_valores = [(k, v) for k, v in ciudades_ordenadas]

    #El método sorted() directamente sobre el diccionario ciudades. 
    #La opción key se utiliza para indicar que el criterio de ordenamiento debe ser la 
    #función get() del diccionario, que toma una clave como argumento y devuelve 
    #el valor correspondiente. 
    #La opción reverse=True se utiliza nuevamente para que el ordenamiento sea descendente. 
    #El resultado es una lista de claves ordenadas por la temperatura media anual. 
    #Nota que en este caso, no se incluyen los valores de las temperaturas en la lista ordenada.
    #ciudades_ordenadas = sorted(ciudades,key=ciudades.get,reverse=True)

    return ciudades_ordenadas

def guardar_resultados_en_archivo(resultados, archivo):
    """
    Guarda los resultados en un archivo JSON.
    """
    with open(archivo, "w") as f:
        json.dump(resultados, f)
    print("Resultados guardados en el archivo '{}'.\n".format(archivo))

# Programa principal

print("""
      OPCIONES:\n
      1. Generar diccionario aleatorio y almacenarlo en disco.\n
      2. Cargar diccionario del disco o generar uno nuevo.\n
      3. Mostrar ciudad(es) con la temperatura media anual más alta.\n
      4. Mostrar ciudad(es) con la temperatura media anual más baja.\n
      5. Mostrar todas las ciudades en orden descendente de temperatura media anual.\n
      6. Salir.\n"
      """)
ciudades=None
while True:
    op = input("Entre opción:")
    if op=="1":
        ciudades=generar_diccionario()
    elif op=="2":
        ciudades=cargar_diccionario()
    elif op=="3":
        ciudad_alta=ciudad_con_temperatura_extrema(ciudades,"alta")
        for ciudad in ciudad_alta:
            print(ciudad)
    elif op=="4":
        ciudad_baja=ciudad_con_temperatura_extrema(ciudades,"baja")
        for ciudad in ciudad_baja:
            print(ciudad)
    elif op=="5":
        ciudad_ordenada=ciudades_ordenadas_por_temperatura(ciudades)
        for ciudad in ciudad_ordenada:
            print(f"{ciudad[0]},{round(ciudad[1],2)}")
            #print(ciudad)
    elif op=="6":
        exit()
    else:
        print("opción invalida, intente nuevamente.")
    con=input("...(press any key)")


        
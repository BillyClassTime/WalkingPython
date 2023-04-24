import json
from random import randint

NombreCiudades = {"Madrid","Barcelona","Sevilla","Malaga","Cordoba","Toledo","Valencia","Bilbao","Salamanca","Palma","Caceres","Segovia","Saragoça ","Cuenca","Alicante","Las Palmas","Avila","Merida","Granada","Murcia"}

def generar_diccionario():
    ciudades = {}
    for i in NombreCiudades:
        media_temperaturas = sum(randint(-10, 40) for j in range(12))
        ciudades[i] = media_temperaturas / 12
    return ciudades

def guardar_diccionario(diccionario):
    with open('temperaturas.json', 'w') as f:
        json.dump(diccionario, f)

def cargar_diccionario():
    try:
        with open('temperaturas.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return generar_diccionario()

def ciudades_mas_calurosas(diccionario):
    max_temperatura = max(diccionario.values())
    return [ciudad for ciudad, temperatura in diccionario.items() if temperatura == max_temperatura]

def ciudades_mas_frias(diccionario):
    min_temperatura = min(diccionario.values())
    return [ciudad for ciudad, temperatura in diccionario.items() if temperatura == min_temperatura]

def ciudades_ordenadas_por_temperatura(diccionario):
    return sorted(diccionario.items(), key=lambda x: x[1], reverse=True)

def guardar_resultados(resultados):
    with open('resultados.json', 'w') as f:
        json.dump(resultados, f)

def main():
    opcion = input("Seleccione una opción:\n1. Generar diccionario aleatorio y guardar en disco.\n2. Cargar diccionario del disco.\nOpción: ")
    if opcion == "1":
        diccionario = generar_diccionario()
        guardar_diccionario(diccionario)
    elif opcion == "2":
        diccionario = cargar_diccionario()
    else:
        print("Opción inválida.")
        return
    
    print(f"Las ciudades más calurosas son: {ciudades_mas_calurosas(diccionario)}")
    print(f"Las ciudades más frías son: {ciudades_mas_frias(diccionario)}")
    print("Ciudades ordenadas por temperatura:")
    for ciudad, temperatura in ciudades_ordenadas_por_temperatura(diccionario):
        print(f"{ciudad}: {temperatura}")
    
    opcion = input("Desea guardar los resultados en un archivo json? (S/N): ")
    if opcion.upper() == "S":
        resultados = {
            "ciudades_mas_calurosas": ciudades_mas_calurosas(diccionario),
            "ciudades_mas_frias": ciudades_mas_frias(diccionario),
            "ciudades_ordenadas_por_temperatura": ciudades_ordenadas_por_temperatura(diccionario)
        }
        guardar_resultados(resultados)

if __name__ == '__main__':
    main()

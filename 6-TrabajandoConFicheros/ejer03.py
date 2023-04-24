from random import randint
import json

def generar_personas():
    personas = [{"genero": "F" if randint(0, 1) == 0 else "M", "edad": randint(0, 120)} for _ in range(100)]
    with open("personas.json", "w") as f:
        json.dump(personas, f)
    return personas

def recuperar_personas():
    try:
        with open("personas.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return generar_personas()

def contar_mujeres_mayores(personas):
    return sum(1 for p in personas if p["genero"] == "F" and p["edad"] >= 18)

def contar_hombres_menores(personas):
    return sum(1 for p in personas if p["genero"] == "M" and p["edad"] < 18)

def encontrar_edad_menor(personas, genero):
    edades_genero = [p["edad"] for p in personas if p["genero"] == genero]
    return min(edades_genero)

def calcular_promedio_edad(personas, genero):
    edades_genero = [p["edad"] for p in personas if p["genero"] == genero]
    return round(sum(edades_genero) / len(edades_genero),2)

if __name__ == "__main__":
    # generar o recuperar lista
    opcion = input("Seleccione una opción: (1) generar nueva lista o (2) recuperar lista existente: ")
    if opcion == "1":
        personas = generar_personas()
    else:
        personas =  recuperar_personas()

    # mostrar estadísticas
    print("Número de mujeres mayores de edad:", contar_mujeres_mayores(personas))
    print("Número de hombres menores de edad:", contar_hombres_menores(personas))
    print("Edad menor entre los hombres:", encontrar_edad_menor(personas, "M"))
    print("Edad menor entre las mujeres:", encontrar_edad_menor(personas, "F"))
    print("Promedio de edad de los hombres:", calcular_promedio_edad(personas, "M"))
    print("Promedio de edad de las mujeres:", calcular_promedio_edad(personas, "F"))

    # guardar estadísticas en archivo json
    guardar_estadisticas = input("¿Desea guardar las estadísticas en un archivo json? (s/n): ")
    if guardar_estadisticas.lower() == "s":
        estadisticas = {
            "mujeres_mayores": contar_mujeres_mayores(personas),
            "hombres_menores": contar_hombres_menores(personas),
            "edad_menor_hombres": encontrar_edad_menor(personas, "M"),
            "edad_menor_mujeres": encontrar_edad_menor(personas, "F"),
            "promedio_edad_hombres": calcular_promedio_edad(personas, "M"),
            "promedio_edad_mujeres": calcular_promedio_edad(personas, "F")
        }
        with open("estadisticas.json", "w") as f:
            json.dump(estadisticas, f)
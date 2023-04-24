import random
import json

def generar_lista_aleatoria():
    return [random.choice(["H", "M"]) for _ in range(100)]

def guardar_lista_en_archivo(lista):
    with open("lista_personas.json", "w") as f:
        json.dump(lista, f)

def cargar_lista_desde_archivo():
    try:
        with open("lista_personas.json", "r") as f:
            lista = json.load(f)
            return lista
    except FileNotFoundError:
        return None

def clasificar_genero(lista):
    hombres = lista.count("H")
    mujeres = lista.count("M")
    porcentaje_hombres = hombres / len(lista) * 100
    porcentaje_mujeres = mujeres / len(lista) * 100
    return hombres, mujeres, porcentaje_hombres, porcentaje_mujeres

if __name__ == "__main__":
    opcion = input("""
       Elige una opción:\n
       1. Generar lista aleatoria\n
       2. Recuperar lista del archivo o generar nueva\n
       """)

    if opcion == "1":
        lista = generar_lista_aleatoria()
    elif opcion == "2":
        lista = cargar_lista_desde_archivo()
        if lista is None:
            lista = generar_lista_aleatoria()
            guardar_lista_en_archivo(lista)
    else:
        print("Opción no válida")
        exit()

    hombres, mujeres, porcentaje_hombres, porcentaje_mujeres = clasificar_genero(lista)

    print(f"Numero de hombres: {hombres}")
    print(f"Numero de mujeres: {mujeres}")
    print(f"Porcentaje de hombres: {porcentaje_hombres:.2f}%")
    print(f"Porcentaje de mujeres: {porcentaje_mujeres:.2f}%")

    opcion_guardar = input("¿Deseas guardar los resultados en un archivo? (s/n)\n")
    if opcion_guardar.lower() == "s":
        resultados = {
            "num_hombres": hombres,
            "num_mujeres": mujeres,
            "porcentaje_hombres": round(porcentaje_hombres,2),
            "porcentaje_mujeres": round(porcentaje_mujeres,2)
        }
        with open("resultados.json", "w") as f:
            json.dump(resultados, f)

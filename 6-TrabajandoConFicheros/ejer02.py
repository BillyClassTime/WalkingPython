import json
import random
from collections import Counter

def generate_persons_list(num_persons):
    return [random.randint(0, 125) for _ in range(num_persons)]

def save_list_to_file(persons_list, filename):
    with open(filename, "w") as f:
        json.dump(persons_list, f)

def load_list_from_file(filename):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except:
        return None


def calculate_statistics(persons_list):
    num_18_or_more = sum(age >= 18 for age in persons_list)
    max_age = max(persons_list)
    min_age = min(persons_list)
    age_distribution = Counter(persons_list)
    age_percentage = {age: count / len(persons_list) * 100 for age, count in age_distribution.items()}
    return {
        "num_18_or_more": num_18_or_more,
        "max_age": max_age,
        "min_age": min_age,
        "age_distribution": age_distribution,
        "age_percentage": age_percentage
    }

def save_statistics_to_file(statistics, filename):
    with open(filename, "w") as f:
        json.dump(statistics, f)

#def load_statistics_from_file(filename):
#    with open(filename, "r") as f:
#        return json.load(f)

def main():
    persons_list_filename = "persons_list.json"
    statistics_filename = "statistics.json"
    opcion = input("Elige una opción:\n1. Generar lista aleatoria\n2. Recuperar lista del archivo o generar nueva\n")
    if opcion == "1":
       persons_list = generate_persons_list(100)
    elif opcion == "2":
        persons_list = load_list_from_file(persons_list_filename)
        if persons_list is None:
            persons_list = generate_persons_list(100)
            save_list_to_file(persons_list, persons_list_filename)
    else:
        print("Opción no válida")
        exit()
    statistics = calculate_statistics(persons_list)
    print(f"Number of persons with 18 or more years: {statistics['num_18_or_more']}")
    print(f"Maximum age: {statistics['max_age']}")
    print(f"Minimum age: {statistics['min_age']}")
    print("Age distribution:")
    
    for age, count in sorted(statistics['age_distribution'].items()):
        percentage = statistics['age_percentage'][age]
        print(f"{age}: {count} ({percentage:.2f}%)")

    opcion_guardar = input("¿Deseas guardar los resultados en un archivo? (s/n)\n")

    if opcion_guardar.lower() == "s":
        save_statistics_to_file(statistics, statistics_filename)

if __name__ == "__main__":
    main()
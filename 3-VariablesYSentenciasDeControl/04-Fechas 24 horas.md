4. Crea un programa que le pida al usuario una hora en formato "hh:mm" y luego calcule y muestre la hora en 24 horas (por ejemplo, "19:30" se convertiría en "19:30").

La hora debe ser validada para asegurarse de que esté en el formato correcto y de que las horas y los minutos sean números enteros.

```
def validar_hora(hora):
    # Verificar si la hora está en el formato correcto
    if len(hora) != 5 or hora[2] != ":":
        return False
    
    # Verificar si las horas y los minutos son enteros
    try:
        horas = int(hora[:2])
        minutos = int(hora[3:])
    except ValueError:
        return False
    
    # Verificar que las horas y los minutos están en los rangos correctos
    if horas < 0 or horas > 23 or minutos < 0 or minutos > 59:
        return False
    
    # Si todo está bien, la hora es válida
    return True

# Pedir la hora al usuario
hora_usuario = input("Ingrese una hora en formato 'hh:mm': ")

# Validar la hora ingresada
while not validar_hora(hora_usuario):
    hora_usuario = input("La hora ingresada no es válida. Ingrese una hora en formato 'hh:mm': ")

# Convertir la hora a formato de 24 horas
horas = int(hora_usuario[:2])
minutos = int(hora_usuario[3:])
if horas == 12:
    horas = 0
if hora_usuario[-2:] == "pm":
    horas += 12

# Mostrar la hora en formato de 24 horas
print(f"La hora en formato de 24 horas es: {horas:02d}:{minutos:02d}")
```



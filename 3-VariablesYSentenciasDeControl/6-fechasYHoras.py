# %%
from datetime import datetime
datenow1 = datetime.now().date()
#print(f"Hora:{datenow1.hour}:{datenow1.minute}")

print(type(datenow1))
print("Fecha:",datenow1)
print(f"Año de la primera Fecha:{datenow1.year}")
datenow2 = datetime.now()
print("Fecha:",datenow2)
print("Año:",datenow2.year)
print("Mes:",datenow2.month)
print("Dia:",datenow2.day)
print(f"Hora:{datenow2.hour}:{datenow2.minute}")
print(f"El dia de la semana es: {datenow2.weekday}")

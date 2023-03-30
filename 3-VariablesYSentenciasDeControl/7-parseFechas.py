# %%
from datetime import datetime
fecha = "10-11-2022"
obj = datetime.strptime(fecha,'%m-%d-%Y')
print(obj)
print(f"{obj.day}-{obj.month}-{obj.year}")

# %%
colores=["Red","Yellow","Green"]
colores.append("Black")
colores.insert(2,"Orange")
print("Lista de colores:",colores)

print("Posicion color Yellow:",colores.index("Yellow"))
colores.remove("Yellow") #Remueve la primera 

print("Color en la posición 2:",colores[2])
print("Lista de colores:",colores)

# %%
colores1=["Red Strong","Yellow Dark","Ligth Green"]
colores2=["Magenta","Pink","Blue"]
print(colores2)
colores2.extend(colores1)
print(colores2)
colores2.pop(2)
print(colores2)


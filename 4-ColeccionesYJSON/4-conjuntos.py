# %%
ciudades = {"madrid","albacete","sevilla"}
ciudades.add("valencia")
print("Conjunto de ciudades:",ciudades)
ciudades.discard("albacete")
print("Conjunto de ciuades:",ciudades)
for ciudad in ciudades:
    print(ciudad)
print(len(ciudades))


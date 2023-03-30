# %%
dicc= {"red":"rojo", "blue":"blue", "green":"verde"}
dicc["black"]="negro"
print(dicc)
dicc.pop("blue")
print(dicc)
print(dicc["red"])
for key in dicc:
    print(key,'->',dicc[key])

# %%
dicc= {"red":"rojo", "blue":"blue", "green":"verde"}
print(dicc.get("red","no exite"))
# %%
print("Instruccion antes del while")
valor = 50
while(valor<5):
    valor+=1
    if(valor == 3):
        continue
    print(f"Valor actual:{valor}")
    if(valor ==4):
        break
print("Instruccion después del while")
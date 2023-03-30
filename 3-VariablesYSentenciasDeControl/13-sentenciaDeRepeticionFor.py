# %%
lenguajes = ['python','c','c++','java','CSharp','R','COBOL','java script','php']
# for lenguaje in lenguajes:
#     print(lenguaje)
cantidadLenguajes= len(lenguajes)
for numero in range(cantidadLenguajes): 
    if (numero >= 5 and numero <=7):
        continue #break
    else:
        print(f"P:{numero} - V:{lenguajes[numero]}")
#fin para        
print("Estos son los lenguaje mas populares")
# %%
numero1 = 100
numero2 = 0

try:
    print(numero1/numero2)
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
except ZeroDivisionError:
    print("Error al dividir por cero.")
except TypeError:
    print("Error en la división ")
except:
    print("Error")
else:
    print("La división se calculo correctamente.")
finally:
    print("Fin del programa")
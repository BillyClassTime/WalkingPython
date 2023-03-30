# %%
numero1 = 100
numero2 = 0

try:
    print(numero1/numero2)
except ZeroDivisionError:
    print("Error al dividir por cero.")
except:
    print("Error")
else:
    print("La división se calculo correctamente.")
finally:
    print("Fin del programa")
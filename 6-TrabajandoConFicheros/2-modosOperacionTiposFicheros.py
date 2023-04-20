fichero = None
def fichero_exite(nombre_fichero):
    try:
        open(nombre_fichero) #,"rt")
    except Exception: #FileNotFoundError: 
        return False
    else: 
        return True
try:
    file = input("Entre el nombre del fichero:") #"InformacionPersonas.json"
    if (not fichero_exite(file)):
        fichero=open(file,"wt",encoding='UTF-8')
        #contenido = '{"nombre": "Juan", "edad": 30, "email": "juan@acme.com", "trabajo": {"empresa": "Acme Corp", "puesto": "Ingeniero de software"}}'
        contenido = input("Entre lo que va a contener el fichero:")
        fichero.write(contenido)
        print('Escrito contenido en fichero')
    else:
        fichero=open(file,"rt",encoding='UTF-8')
        contenido = fichero.read()
        print(f"Leido contenido:\n{contenido}")
except ValueError as e:
    print(f"E:{e}")
except FileNotFoundError as e:
    print(f"E:{e}")
except Exception as e:
    print(f"E:{e}")
finally:
    if fichero != None:
        fichero.close()
        print('closing')

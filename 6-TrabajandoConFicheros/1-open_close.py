fichero=None
try:
    fichero=open("BillyVanegasEjerciciosFundamentos.md","rt",encoding='UTF-8') #D:\caperta\nombrefichero.extension
    #,encoding='UTF-8')
    #print(type(fichero))
    contenido = fichero.read()
    print(contenido)
except FileNotFoundError as e:
    print(f"{e}")
except Exception as e:
    print(f"E:{e}")
finally:
    if fichero != None :
        fichero.close()
        print('closing')

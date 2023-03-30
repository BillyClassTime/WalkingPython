try:
    fichero=open("file_500.csv","rt")
    #,encoding='UTF-8')
    print(type(fichero))
    contenido = fichero.read()
    print(contenido)
except FileNotFoundError as e:
    print(f"{e}")
except Exception as e:
    print(f"E:{e}")
finally:
    fichero.close()
    print('closing')

def fichero_exite(nombre_fichero):
    try:
        open(nombre_fichero,"rt")
    except FileNotFoundError:
        return False
    return True
try:
    file = "file_300.csv"
    if (not fichero_exite(file)):
        fichero=open(file,"wt",encoding='UTF-8')
        contenido = "'árbol','limón','naranja'"
        fichero.write(contenido)
        print('Escrito contenido en fichero')
    else:
        fichero=open(file,"rt",encoding='UTF-8')
        contenido = fichero.read()
        print(f"Leido contenido:{contenido}")
except Exception as e:
    print(f"E:{e}")
finally:
    fichero.close()
    print('closing')

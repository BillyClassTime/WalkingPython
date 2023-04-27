def validaDNI(DNI,letra):
    letrasDNI = "TRWAGMYFPDXBNJZSQVHLCKE"
    if type(DNI)!='str':
         DNI = str(DNI)
    if len(DNI) == 8 and DNI[:8].isdigit():
        resto = int(DNI[:8]) % 23
        letraValida = letrasDNI[resto]
        if letraValida == letra:
            resultado = "DNI válido"
        else:
            resultado = "La letra no coincide"
    else:
        resultado = "El formato del DNI no es válido"
    return resultado

if __name__ == '__main__':
    try:
        dni = input("Entre DNI:")
        dni = int(dni)
        letra = input("Entre letra:")
        resultado = validaDNI(dni,letra)
        print(resultado)
    except Exception as e:
        print(e)
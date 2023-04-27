def validaDNI(DNI,letrasDNI):
    if len(DNI) == 9 and DNI[:8].isdigit() and DNI[8].isalpha():
        letra = DNI[8]
        resto = int(DNI[:8]) % 23
        letraValida = letrasDNI[resto]
        if letraValida == letra:
            resultado = "DNI válido"
        else:
            resultado = "La letra no coincide"
    else:
        resultado = "El formato del DNI no es válido"
    return resultado

if __name__ == "__main__":
    dni = input("Entre dni:")
    letra = input("Entre letra:")
    validaDNI(dni,letra)
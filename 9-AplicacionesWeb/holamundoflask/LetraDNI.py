def LetraDNI(numero,letra):
    letraDNI = "TRWAGMYFPDXBNJZSQVHLCKE"
    #op = "si"
    #while op == "si":
        #numero = input("Pon el número de tu DNI: ")
    if len(str(numero)) == 8 and str(numero).isnumeric():
        resto = int(numero) % 23
        if letra == letraDNI[resto]:
            return f"La letra del DNI introducido es: {letraDNI[resto]}, es un DNI Válido"
        else:
            return f"la letra {letra} no corresponde al dni: {numero}"
    #    choose = input("Quieres buscar otra letra del DNI 'si' o 'no': ")
    #    op = choose.lower()
    else:
        return "DNI inválido"
    #print("¡Hasta luego!")

if __name__ == "__main__":
    numero=input("Entre el número del DNI:")
    letra =input("Entre la letra del DNI:")
    LetraDNI()
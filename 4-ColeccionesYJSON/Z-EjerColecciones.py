def diccionario():
    frutas={"Manzanas":5,"Naranja":3,"Bananas":7}
    frutas["Peras"]=4
    print(frutas)
    del frutas["Naranja"]
    print(frutas)

    for fruta,cantidad in frutas.items():
        print(f"Tengo: {fruta} {cantidad}")

#Lista
def borradoDeElementosListas():
    lista=[1,6,3,4,5]
    print(lista)
    longitudLista = len(lista)
    i=0
    while(i<longitudLista):
        del lista[0]
        if i==3 or len(lista)<3:
            break
        i+=1
    print(lista)
    lista=[1,6,3,4,5]
    for i in range(len(lista)):
        del lista[0]
        if i==3 or len(lista)<3:
            break
    print(lista)


#Trabajo con Tuplas
def trabajoTuplas():
    #1 - Unir dos tuplas
    tuplaUno = (1,3,4)
    tuplaDos = (5,7,88)
    tuplaTres = tuplaUno+tuplaDos
    print(tuplaTres)
    #2 - Contar cuantas veces existe un elemento en la tupa
    tuplaCuatro=(1,23,3,1,3,1,34,1)
    print(tuplaCuatro)
    print(len(tuplaCuatro))
    print(tuplaCuatro.count(3))
    #3 - Encontrar el elemento que aparezca dado su indice
    print(tuplaCuatro.index(5)) # El 3 esta en la posición 2

#Conjuntos
def conjuntos():
    conjunto = {1,2,3}
    conjuntoUno = set()
    conjunto.add(34)
    conjuntoUno.add(1)
    print(conjunto)
    print(conjuntoUno)
    #unir conjuntos
    conjuntoTres = conjunto.union(conjuntoUno)
    conjunto.remove(2)
    print(conjunto)
    #intersección de conjuntos
    conjuntoCinco = {1,2,3}
    conjuntoSeis = {3,4,5}
    conjuntoSiete = conjuntoCinco.intersection(conjuntoSeis)
    print(conjuntoSiete)
    #subconjunto
    conjuntoOcho = {1,2,3}
    conjuntoNueve = {1,2}
    print(conjuntoNueve.issubset(conjuntoOcho))

asistencias = {"Ana": (1, 2, 3, 5, 6), "Luis": (2, 3, 4, 6, 7)}
#1
contadorSesiones=0
i=0
for nombre, sesiones in asistencias.items():
    print(nombre,len(sesiones))
    contadorSesiones += len(sesiones)
    i+=1
print(f"1.Ana y Luis, asistieron a:{contadorSesiones} sesiones entre los dos")

#1 Alternativa:
print("1A.Ana y Luis, asistieron a:{} sesiones entre los dos".format(len(asistencias["Ana"])+len(asistencias["Luis"])))

#2 
sesionesConjuntas=0
sConjuntas=[]
for sesion in asistencias["Ana"]:
    if sesion in asistencias["Luis"]:
        sesionesConjuntas+=1
        sConjuntas.append(sesion)
print(f"2,Las sesiones que asistieron ambos:{sesionesConjuntas},{sConjuntas}")

#2 Alternativa
print("2A.Las sesiones que asistieron ambos:{}".format(set(asistencias["Ana"]).intersection(set(asistencias["Luis"]))))

#3 
sesionesDiferentes=0
sDiferentes=[]
for sesion in asistencias["Ana"]:
    if sesion not in asistencias["Luis"]:
        sesionesDiferentes+=1
        sDiferentes.append(sesion)
for sesion in asistencias["Luis"]:
    if sesion not in asistencias["Ana"]:
        sesionesDiferentes+=1
        sDiferentes.append(sesion)
sDiferentes.sort()
print(f"3.Las sesiones que no asistieron ambos, pero al menos asistió Luis o Ana:{sesionesDiferentes},{sDiferentes}")


#3 Alternativa
def sesionesSoloUno(sesionesAlumnoA,sesionesAlumnoB):
    sesiones=0
    sDiferentes=[]
    for sesion in sesionesAlumnoA:
        if sesion not in sesionesAlumnoB:
            sesiones+=1
            sDiferentes.append(sesion)
    return sesiones, sDiferentes

sDiferentes=[]
sesionesDiferentes, anaNoEnLuis=sesionesSoloUno(asistencias["Ana"],asistencias["Luis"])
sDiferentes.extend(anaNoEnLuis)
sesionesDiferentes, luisNoEnAna=sesionesSoloUno(asistencias["Luis"],asistencias["Ana"])
sDiferentes.extend(luisNoEnAna)
sDiferentes.sort()
print(f"3A.Las sesiones que no asistieron ambos,pero al menos asistió Luis o Ana:{sesionesDiferentes},{sDiferentes}")

#3 Alternativa
sesionesQueNoAsistieronAmbos=set()
for nombre,sesiones in asistencias.items():
    for sesion in sesiones:
        sesionA=set({sesion})
        if not sesionA.issubset(sConjuntas):
            sesionesQueNoAsistieronAmbos.add(sesion)
sesionesQueNoAsistieronAmbosList=list(sesionesQueNoAsistieronAmbos)
sesionesQueNoAsistieronAmbosList.sort()
print("3B.Las sesiones que no asistieron ambos:{}, pero al menos asistió Luis o Ana".format(sesionesQueNoAsistieronAmbosList))

#3 Alternativa
print("3C.Las sesiones que no asistieron ambos:{}, pero al menos asistió Luis o Ana".format(set(asistencias["Ana"]).symmetric_difference(set(asistencias["Luis"]))))

#4
cAnaPeroNoLuis=0
AnaPeroNoLuis=[]
for sesion in asistencias["Ana"]:
    if sesion not in asistencias["Luis"]:
        cAnaPeroNoLuis+=1
        AnaPeroNoLuis.append(sesion)
print("4.Las sesiones que asistio Ana pero no Luis:{}".format(AnaPeroNoLuis))

#4 Alternativa
sAnaNoLuis=[]
sesionesDiferentes, anaNoEnLuis=sesionesSoloUno(asistencias["Ana"],asistencias["Luis"])
sAnaNoLuis.extend(anaNoEnLuis)
print("4A.Las sesiones que asistio Ana pero no Luis:{}".format(sAnaNoLuis))

cLuisPeroNoAna=0
LuisPeroNoAna=[]
for sesion in asistencias["Luis"]:
    if sesion not in asistencias["Ana"]:
        cLuisPeroNoAna+=1
        LuisPeroNoAna.append(sesion)
print("5.Las sesiones que asistio Luis pero no Ana:{}".format(LuisPeroNoAna))


sLuisNoAna=[]
sesionesAna, anaNoEnLuis=sesionesSoloUno(asistencias["Luis"],asistencias["Ana"])
sLuisNoAna.extend(anaNoEnLuis)
print("5A.Las sesiones que asistio Luis pero no Ana:{}".format(sLuisNoAna))
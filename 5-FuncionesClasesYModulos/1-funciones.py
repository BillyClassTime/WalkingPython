def saludar(nombre):
    #funcionalidad del tiempo
    print(f'hola {nombre}, buenos dias')

def sumar(a,b):
    return (a+b)

def addColores(colores,color):
    try:
        colores.append(color)
        return True
    except AttributeError:
        return False 


saludar('Billy') #,'Carlos')
saludar('Carlos')
saludar('Helena')
saludar('Silvia')

resultado = sumar(5,5) #resultado = 5+5
print(resultado)
print(sumar(7,5))
print(sumar(9,5))
print(sumar(0,5))
print(sumar(4,4))

colores=[]
if(addColores(colores,'azul')):
    print('Inserte el color')
if(addColores(colores,'rojo')):
    print('Inserte el color')
if(addColores(colores,'verde')):
    print('Inserte el color')
if(addColores(colores,'negro')):
    print('Inserte el color')
if(addColores(colores,'purpura')):
    print('Inserte el color')
saludar(colores)

if (addColores('billy','naranja')):#Equivalente addCo..()==True
    print('Insertado color')
else:
    print('No insertado color')

if (addColores(colores,'naranja')):#Equivalente addCo..()==True
    print('Insertado color')
else:
    print('No insertado color')

ciudad='Nairobi'

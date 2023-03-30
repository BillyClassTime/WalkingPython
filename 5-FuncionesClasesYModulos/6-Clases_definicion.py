class Persona:
    Nombres=""
    Apellidos=""
    def __init__(self,nombres,apellidos):
         self.Nombres = nombres
         self.Apellidos = apellidos
    def __str__(self):
        return "{} {}".format(self.Nombres,self.Apellidos)
    def caminar(self):
        print('caminando')
a = 1
profesor = Persona("Billy ","Vanegas")
# profesor.Nombres="Billy "    #setter
# profesor.Apellidos="Vanegas" #setter
print(type(profesor.Nombres))

alumno = Persona("Pedro","Sanchez")
# alumno.Nombres = "Pedro"
# alumno.Apellidos = "Sanchez"

alumno1 = Persona("Miguel","Feijo")
# alumno1.Nombres = "Miguel"
# alumno1.Apellidos = "Feijo"

administrativo = Persona("Oscar","León")
# administrativo.Nombres = "Oscar"
# administrativo.Apellidos = "León"
print("El profesor: {} {}".format(profesor.Nombres,profesor.Apellidos)) #getter
print("El alumno: {} {}".format(alumno.Nombres,alumno.Apellidos))
print("El alumno 1: {} {}".format(alumno1.Nombres,alumno1.Apellidos))
print("El administrativo: {} {}".format(administrativo.Nombres,administrativo.Apellidos))
print("El Alumno :",alumno)
profesor.caminar()
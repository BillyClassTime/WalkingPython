class Persona:
    def __init__(self,nombres,apellidos):
        self.Nombres = nombres
        self.Apellidos = apellidos

class Alumno(Persona):
    Curso = None
    def __init__(self, nombres, apellidos,curso):
        self.Curso = curso
        super().__init__(nombres, apellidos)

est = Alumno('Ricardo','Montalban','Azure fundamentals')
print(f'{est.Nombres} {est.Apellidos} {est.Curso}')
class student:
    school = "San Patric"   #Atributos de clase
    totalStudents = 0       #Atributos de clase
    def __init__(self, name, std,rool_nos):
        self.nm = name      #Atributos de instancia
        self.std = std
        student.totalStudents +=1
    def getData(self):      #metodo getter
        print("Student name:",self.nm)
        print("Standard:",self.std)
                            #metodo setter
    def setData(self, name, std):
        self.nm = name
        self.std = std


print("The school name is:",student.school)
stud_1= student("0m","4th",9)
stud_1.getData()
stud_2 = student("Harri","5th",14)
stud_2.getData()
print("The total students are:",student.totalStudents)
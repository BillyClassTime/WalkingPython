class partner:
    def __init__(self):
        self._age = 0
    def get_age(self):
        print('getter llamado')
        return self._age
    def set_age(self,a):
        print('setter llamado')
        if (a<10):
            raise ValueError("edad no permitida")
        self._age = a
    def del_age(self):
        del self._age
    age = property(get_age,set_age,del_age)
mark = partner()
try:
    mark.age = 10
except ValueError:
    print("Edad no permitida")
finally:
    print(mark.age)

    
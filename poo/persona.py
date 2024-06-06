class Persona():

    def __init__(self, dni, name, age):
        self.dni = dni
        self.name = name
        self.age = age
    
    @property
    def dni(self):
        return self._dni
    
    @dni.setter
    def dni(self, dni):
        self._dni = dni

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        if age>0:
            self._age = age
        else:
            self._age = 0
            print("Edad incorrecta")

    def mostrar(self):    
        return self.dni.mostrar()+" "+self.name+" ("+str(self.age)+")"
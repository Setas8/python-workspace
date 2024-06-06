from persona import Persona

class Alumno(Persona):

    def __init__(self, dni, name, age, curse, mark):
        super().__init__(dni, name, age)
        self.curse = curse
        self.mark = mark

    @property
    def curse(self):
        return self._curse
    
    @curse.setter
    def curse(self, curse):
        self._curse = curse

    @property
    def mark(self):
        return self._mark
    
    @mark.setter
    def mark(self, mark):
        if mark>=0 and mark<=10:
            self._mark = mark 
        else:
            self._mark = -1
            print("Nota incorrecta")      

    def estaAprobado(self):
        if self.mark >= 5:
            print("Está aprobado")
        elif self.mark>=0 and self.mark<5:
            print("Está suspenso")   
        else:
            print("Nota incorrecta")

    def mostrar(self):
        return super().mostrar()+" "+self.curse+" --> "+str(self.mark)
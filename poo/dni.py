class Dni():

    def __init__(self,number):
        self.number = number
    
    def __calcular_letra(self):
        letras= 'TRWAGMYFPDXBNJZSQVHLCKE'
        return letras[int(self.number)%23]
    
    @property
    def number(self):
        return self._number
    
    @property
    def letra(self):
        return self._letra
    
    @number.setter
    def number(self,number):
        if len(number) == 8 and number.isdigit():
            self._number = number
            self._letra = self.__calcular_letra()
        else:
            self._number = 0
            self._letra = ""
            print("DNI INCORRECTO")

    def mostrar(self):
        return self.number + self.letra
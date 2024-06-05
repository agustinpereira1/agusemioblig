from persona import Persona

class Socio (Persona):
    def __init__(self, nombre, apellido, ci, nacimiento, ingreso, celular,tipo,deuda):
        super().__init__(nombre, apellido, ci, nacimiento, ingreso, celular)
        
        self.__tipo = tipo
        self.__deuda = deuda

    @property
    def tipo (self):
        return self.__tipo
        
    @property
    def deuda (self):
        return self.__deuda

    @deuda.setter
    def deuda(self, nueva_deuda):
        self.__deuda += nueva_deuda
        return nueva_deuda
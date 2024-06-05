from persona import Persona

class Medico (Persona):
    def __init__(self, nombre, apellido, ci, nacimiento, ingreso, celular,especialidad_nombre2):
        super().__init__(nombre, apellido, ci, nacimiento, ingreso, celular)
        self.__especialidad_nombre2 = especialidad_nombre2
        self.__lista_cant_pacientes = []
    
    @property 
    def especialidad_nombre2 (self):
        return self.__especialidad_nombre2
    
    @property
    def lista_cant_pacientes(self):
        return self.__lista_cant_pacientes
    
    # class Especialidad:
    #     def __init__(self,nombre,precio):
    #         self.__nombre = nombre
    #         self.__precio = precio
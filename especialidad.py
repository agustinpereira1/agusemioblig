class Especialidad:
    def __init__(self,especialidad_nombre,precio):
        self.__especialidad_nombre = especialidad_nombre
        self.__precio = precio

    @property
    def especialidad_nombre (self):
        return self.__especialidad_nombre
    
    @property
    def precio (self):
        return self.__precio
    

    
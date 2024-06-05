class Consulta:
    def __init__(self, especialidad_nombre3, nombre_apellido_medico, fecha_consulta, numero_pacientes):
        self.__fecha_consulta = fecha_consulta
        self.__especialidad_nombre3 = especialidad_nombre3
        self.__nombre_apellido_medico = nombre_apellido_medico
        self.__numero_pacientes = []

        for i in range(1,numero_pacientes+1):
            self.__numero_pacientes.append(i)

    @property 
    def fecha_consulta (self):
        return self.__fecha_consulta
    @property
    def especialidad_nombre3(self):
        return self.__especialidad_nombre3
    @property
    def nombre_apellido_medico(self):
        return self.__nombre_apellido_medico
    @property
    def numero_pacientes(self):
        return self.__numero_pacientes
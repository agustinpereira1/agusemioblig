from abc import ABC, abstractmethod

class Persona:
    def __init__(self, nombre, apellido, ci, nacimiento,ingreso,celular):
        self.__nombre = nombre
        self.__appelido = apellido
        self.__ci = ci
        self.__nacimiento = nacimiento
        self.__ingreso = ingreso
        self.__num_celular = celular

    @property
    def nombre(self):
        return self.__nombre
    @property
    def apellido(self):
        return self.__appelido
    @property
    def ci(self):
        return self.__ci
    @property
    def nacimiento(self):
        return self.__nacimiento
    @property
    def ingreso(self):
        return self.__ingreso
    @property
    def celular(self):
        return self.__num_celular
    
    
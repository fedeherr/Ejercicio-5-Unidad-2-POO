import csv
class Alumno:
    __nombre = 'x'
    __anio = 0
    __division = 'x'
    __inasistencias = 0
    inasistenciasmax = 20
    totalclases = 150
    def __init__(self, nombre = 'x', anio = 0, division = 'x', inasistencias = 0):
        self.__nombre = nombre
        self.__anio = anio
        self.__division = division
        self.__inasistencias = inasistencias
    def getNombre(self):
        return self.__nombre
    def getAnio(self):
        return self.__anio
    def getDivision(self):
        return self.__division
    def getInasistencias(self):
        return self.__inasistencias
    @classmethod
    def getinasistenciasmax(cls):
        return cls.inasistenciasmax
    @classmethod
    def modinasistenciasmax(cls, nuevo):
        cls.inasistenciasmax = nuevo
    @classmethod
    def gettotalclases(cls):
        return cls.totalclases
    def __str__(self):
        return "%s %d %s %d" % (self.__nombre, self.__anio, self.__division, self.__inasistencias)

    

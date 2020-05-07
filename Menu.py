from Alumno import Alumno
from ManejadorAlumnos import manejadorAlumnos

a = manejadorAlumnos() 
a.manejarAlumnos()

class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { 0:self.opcion0,
                            1:self.opcion1,
                            2:self.opcion2,
                         }
    def getSwitcher(self):
        return self.__switcher
    def opcion(self, op):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func()
    def opcion0(self):
        print('Chao')
    def opcion1(self):
        alumanio = int(input("Ingrese el año a buscar: "))
        alumdivision = input("Ingrese la division: ")
        a.buscarAlumnos(alumanio,alumdivision)
    def opcion2(self):
        clasealumno = Alumno()
        maximo = int(input("Ingrese nuevo maximo de inasistencias: "))
        clasealumno.modinasistenciasmax(maximo)

import csv
from Alumno import Alumno
class manejadorAlumnos:
    __listaAlumnos = []
    def __init__ (self, listaAlumnos = []):
        self.__listaAlumnos = listaAlumnos
    def agregarAlumno(self, unAlumno):
        self.__listaAlumnos.append(unAlumno)
    def __str__(self):
        s = ""
        for alumno in self.__listaAlumnos:
            s += str(alumno) + '\n'
        return s
    def buscarAlumnos(self,anio,division):
        print ("Alumno      Porcentaje")
        for indice, alumno in enumerate(self.__listaAlumnos):
            if ((alumno.getAnio() == anio) & (alumno.getDivision() == division) & (alumno.getInasistencias() > alumno.getinasistenciasmax())):
                print ("" + alumno.getNombre() + "       " + str((alumno.getInasistencias() * 100) / alumno.gettotalclases()))
    def manejarAlumnos(self):
        archivo = open('Alumnos.csv')
        reader = csv.reader(archivo,delimiter=';')
        bandera = True
        for fila in reader:
            if bandera:
                "'saltear cabecera'"
                bandera = not bandera
            else:
                nombre = fila[0]
                anio = int(fila[1])
                division = fila[2]
                inasistencias = int(fila[3])
                unAlumno = Alumno(nombre,anio,division,inasistencias)
                self.agregarAlumno(unAlumno)
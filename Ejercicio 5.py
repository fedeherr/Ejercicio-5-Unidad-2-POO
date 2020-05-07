from Menu import Menu


if __name__ == '__main__':

    menu=Menu()
    salir = False
    while not salir:
        print("""
              0 Salir
              1 Buscar Alumnos que sobrepasaron la inasistencia máxima
              2 Modificar valor de inasistencia máxima""")
        op = int(input('Ingrese una opcion: '))
        menu.opcion(op)
        salir = op == 0
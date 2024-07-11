import os,msvcrt,time, random
from funciones import *

while True:
    print("""Bienvenido
            1. Asignar sueldos aleatorios
            2. Clasificar sueldos
            3. Ver estadísticas.
            4. Reporte de sueldos
            5. Salir del programa
          """)
    opc=elegir_opcion()
    if opc==1:
        asignar_sueldos_aleatorios()
    elif opc==2:
        clasificar_sueldos()
    elif opc==3:
        ver_estadisticas()
    elif opc==4:
        reporte_sueldos()
    elif opc==5:
        salir()
    else:
        pass
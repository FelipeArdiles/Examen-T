import random,os,msvcrt,time


#Variables
trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
sueldos=[]

#funciones
def elegir_opcion():
    while True:
        try:
            opc=int(input("Ingrese una opción del menú: "))
            if opc in (1,2,3,4,5):
                return opc
            else:
                print("ERROR! Ingrese una opción válida")
        except:
            print("ERROR! Debe ingresar un número entero")

def salir():
    print("Finalizando programa...")
    print("Desarrollado por Felipe Ardiles")
    print("RUT 20.001.919-9")
    exit()

def asignar_sueldos_aleatorios():
        while True:
            os.system("cls")
            print("\tASIGNAR SUELDOS ALEATORIOS")
            c=0
            while True:
                aleatorio=random.randint(300000,2500000)
                sueldos.append(aleatorio)
                c=c+1
                if c==10:
                    break
            sueldo_final=[trabajadores,sueldos]
            for x in range (10):
                print(trabajadores[x],"\t","$",sueldos[x],end="\n")
            while True:
                try:
                    opc1=int(input("¿Desea volver a generar la tabla? 1=SI, 2=NO: "))
                    if opc1 in (1,2):
                        break
                except:
                    print("Ingrese un número entero")
            if opc1==2:
                break
            print("La tabla se generó con éxito!")
            print("Presione una tecla para continuar...")
            msvcrt.getch

#ehh... :(
def clasificar_sueldos():
    print("\nSueldos menores a $800.000")
    #for x in (sueldos):
     #   menor=sueldos[x]
      #  if menor<800000:
       #     pass

def ver_estadisticas():
    if not sueldos:
        print("No hay tablas creadas")
    else:
        print("\tVer estadísticas")
        promedio=sum(sueldos)/10
        print("Promedio de los Sueldos:","$",promedio)
        #^1/10

def reporte_sueldos():
    if not sueldos:
        print("No hay tablas creadas")
    else:
        os.system("cls")
        print("\tReporte Sueldos")
        print("NOMBRE","\t\t","Sueldo Base","\t\t","SALUD","\t\t","AFP","\t\t","Sueldo Líquido")
        for x in range(10):
            print(trabajadores[x],"  ","$",sueldos[x],"\t\t","$",round(sueldos[x]*0.12,2),"\t\t","$",round(sueldos[x]*0.07,2),"\t\t","$",sueldos[x]*0.81,end="\n")
        print("Presione una tecla para continuar...")
        msvcrt.getch()
        
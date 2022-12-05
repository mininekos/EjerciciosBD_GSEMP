from sqlite3 import *
from conecionBD import *
from datetime import date
from datetime import datetime

#crearBD()
EMPLEADOS=1
correcto=False
fecha_ingreso = str(datetime(2000,1,25).date());
print(fecha_ingreso)
for i in range(EMPLEADOS):
    nombre = input(("\nIntroduzca nombre: "))
    apellido = input(("\nIntroduzca apellido: "))
    while correcto == False:
        try:
            sueldo_base=float(input("\nIntroduzca sueldo base: "))
            if sueldo_base > 0:
                correcto = True
        except:
            print("Sueldo no valido")
    correcto=False
    while correcto == False:
        try:
            AFAP=int(input("\n¿Tiene AFAP?(1 si o 0 no): "))
            if AFAP == 0 or AFAP == 1:
                correcto = True
        except:
            print("AFAP no valido")
    correcto=False
    while correcto == False:
        try:
            print("\nFecha de ingreso: ")
            dia=input("Dia: ")
            mes = input("Mes(En numero): ")
            anno = input("Año: ")
            fecha_ingreso = str(datetime(anno,mes,dia).date());
            if not fecha_ingreso.__eq__(""):
                correcto=True
        except:
            print("fecha no valiada")
    correcto=False

from sqlite3 import *
from conecionBD import *
from datetime import date
from datetime import datetime

#crearBD()
EMPLEADOS=10
PORCENTAJE_HIJOS=5
PORCENTAJE_AFAP=12
PORCENTAJE_FONASA=7
correcto=False
def diff_month(d1):
    return (datetime.now().year - d1.year) * 12 +  datetime.now().month - d1.month
"""
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
            dia=int(input("Dia: "))
            mes = int(input("Mes(En numero): "))
            anno = int(input("Año: "))
            fecha_ingreso = str(datetime(anno,mes,dia).date())
            print(fecha_ingreso)
            if not fecha_ingreso is None:
                correcto=True
        except:
            print("fecha no valiada")
    correcto=False

    while correcto == False:
        try:
            num_hijo=int(input("\nIngrese numero de hijos: "))
            if num_hijo>=0:
                correcto=True
            else:
                print("Num de hijos no valido")
        except:
            print("Error")

    try:
        insertarEmpleado(nombre,apellido,sueldo_base,AFAP,fecha_ingreso,num_hijo)
    except:
        print("Error al insertar")
"""
mostrarEmpleados()
try:
    id_Empleado=int(input("Seleccione empleado a calcular: "))
    empleado= getEmpleado(id_Empleado)
    sueldo_base=empleado[3]
    fecha_ingreso=date(int(empleado[5].split("-")[0]),int(empleado[5].split("-")[1]),int(empleado[5].split("-")[2]))
    #print(diff_month(fecha_ingreso))
    base_imponible=sueldo_base+(sueldo_base*(empleado[6]*PORCENTAJE_HIJOS)/100)+(sueldo_base*diff_month(fecha_ingreso)/100)
    print(f"La base imponible del empleado es: {base_imponible}€")
    FONASA=base_imponible*PORCENTAJE_FONASA/100
    if int(empleado[4])==1:
        AFAP=base_imponible*PORCENTAJE_AFAP/100
    else:
        AFAP=0
    print(f"El empleado destina a AFAP {AFAP}€ y a FONASA {FONASA}€")
except:
    print("Error con el id del empleado")

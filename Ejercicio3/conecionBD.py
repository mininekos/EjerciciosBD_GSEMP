from sqlite3 import *

def crearBD():
    try:
        bd = connect("BDEjercicio3.db")
        cursor = bd.cursor()
        empleado = ''' 
			CREATE TABLE IF NOT EXISTS "empleado"(
                "id_E" INTEGER NOT NULL,
                "nombre" TEXT NOT NULL,
                "apellido" TEXT NOT NULL,
                "sueldo_base" REAL NOT NULL,
                "AFAP" INTEGER NOT NULL,
                "fecha_ingreso" TEXT NOT NULL,
                "num_hijos" INTEGER NOT NULL,
                PRIMARY KEY ("id_E" AUTOINCREMENT)
            );
		'''

        cursor.execute(empleado)
        print("Empleado creado correctamente")
    except OperationalError as error:
        print("Error al abrir:", error)
    finally:
        cursor.close()

def insertarEmpleado(nombre,apellido,sueldo_base,AFAP,fecha_ingreso,num_hijos):
    try:
        bd = connect("BDEjercicio3.db")
        cursor = bd.cursor()
        sentencia= "INSERT INTO empleado (nombre,apellido, sueldo_base,AFAP,fecha_ingreso,num_hijos) VALUES (?,?,?,?,?,?)"
        cursor.execute(sentencia,[nombre,apellido, sueldo_base,AFAP,fecha_ingreso,num_hijos])

        bd.commit()  # Guardamos los cambios al terminar el ciclo
        print("Datos insertados correctamente")
        """
        sentencia = "SELECT * FROM empleado;"
        cursor.execute(sentencia)
        empleados = cursor.fetchall()
        print("+{:-<20}+{:-<20}+{:-<20}+{:-<20}+{:-<20}+{:-<20}+{:-<20}+".format("","", "", "", "", "", ""))
        print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format("id_E","nombre","apellido",
                                                                   "sueldo_base","AFAP","fecha_ingreso","num_hijos"))
        print("+{:-<20}+{:-<20}+{:-<20}+{:-<20}+{:-<20}+{:-<20}+{:-<20}+".format("", "", "", "", "", "",""))

        for id_E, nombre, apellido, sueldo_base, AFAP, fecha_ingreso,num_hijos in empleados:
            print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format(id_E, nombre, apellido,
                                                                       sueldo_base, AFAP, fecha_ingreso,num_hijos))

        print("+{:-<20}+{:-<20}+{:-<20}+{:-<20}+{:-<20}+{:-<20}+{:-<20}+".format("", "", "", "", "", "",""))
        """
    except OperationalError as error:
        print("Error al abrir:", error)
    finally:
        cursor.close()

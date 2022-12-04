from sqlite3 import *

def crearBD():
    try:
        bd = connect("BDEjercicio2.db")
        cursor = bd.cursor()
        tablas = [
            ''' 
			CREATE TABLE IF NOT EXISTS "region"(
			    "id_region" INTEGER NOT NULL,
				"nombre" TEXT NOT NULL,
				PRIMARY KEY ("id_region" AUTOINCREMENT)
			);
		''',
        '''
            CREATE TABLE IF NOT EXISTS "provincia"(
                "id_provincia" INTEGER NOT NULL,
                "nombre" TEXT NOT NULL,
                "id_region" INTEGER NOT NULL,
                PRIMARY KEY ("id_provincia" AUTOINCREMENT),
                FOREIGN KEY ("id_region") REFERENCES region ("id_region")
            );
        ''',
        '''
            CREATE TABLE IF NOT EXISTS "localidad"(
                "id_localidad" INTEGER NOT NULL,
                "nombre" TEXT NOT NULL,
                "id_provincia" INTEGER NOT NULL,
                PRIMARY KEY ("id_localidad" AUTOINCREMENT),
                FOREIGN KEY ("id_provincia") REFERENCES provincia ("id_provincia")
            );
        ''',
        '''
            CREATE TABLE IF NOT EXISTS "empleado"(
                "id_E" INTEGER NOT NULL,
                "DNI_E" TEXT NOT NULL,
                "nombre" TEXT NOT NULL,
                "tlf" TEXT NOT NULL,
                "salario" REAL NOT NULL,
                "id_localidad" INTEGER NOT NULL,
                PRIMARY KEY ("id_E" AUTOINCREMENT),
                FOREIGN KEY ("id_localidad") REFERENCES localidad ("id_localidad")
            );
        '''
        ]
        for tabla in tablas:
            cursor.execute(tabla);
        print("Tablas creadas correctamente")
    except OperationalError as error:
        print("Error al abrir:", error)
    finally:
        cursor.close()

def insertarDatos():
    try:
        bd = connect("BDEjercicio2.db")
        cursor = bd.cursor()
        tablas = [
            """
            INSERT INTO region
            (nombre)
            VALUES
            ('Andalucia');
            """,
            """
            INSERT INTO provincia
            (nombre,id_region)
            VALUES
            ('Cádiz',1);
            """,
            """
            INSERT INTO localidad
            (nombre,id_provincia)
            VALUES
            ('Jerez',1);
            """,
            """
            INSERT INTO empleado
            (DNI_E,nombre,tlf,salario,id_localidad)
            VALUES
            ('12345678A', 'Juan','987654321',2000,1),
            ('12345678B', 'Luis','987654322',2000,1),
            ('12345678C', 'Pepe','987654323',2000,1);
            """
        ]
        for sentencia in tablas:
            cursor.execute(sentencia);
        bd.commit()  # Guardamos los cambios al terminar el ciclo
        print("Datos insertados correctamente")
    except OperationalError as error:
        print("Error al abrir:", error)
    finally:
        cursor.close()

def insertarEmpleado():
    try:
        bd = connect("BDEjercicio2.db")
        cursor = bd.cursor()
        dniEmpleado = input("\nDni: ")
        nombre=input("\nNombre: ")
        tlf = input("\nTLF: ")
        salario=input("\nSalario: ")
        localidad=input("\nId Localidad: ")
        sentencia= "INSERT INTO empleado (DNI_E,nombre, tlf,salario,id_localidad) VALUES (?,?,?,?,?)"
        cursor.execute(sentencia,[dniEmpleado,nombre,salario,tlf,localidad])

        bd.commit()  # Guardamos los cambios al terminar el ciclo

        sentencia = "SELECT * FROM empleado;"
        cursor.execute(sentencia)
        empleados = cursor.fetchall()

        print("Datos insertados correctamente")
        print("+{:-<20}+{:-<20}+{:-<20}+{:-<20}+{:-<20}+{:-<20}+".format("", "", "", "", "", ""))
        print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format("id_E", "DNI_E", "nombre", "tlf", "salario",
                                                                   "id_localidad"))
        print("+{:-<20}+{:-<20}+{:-<20}+{:-<20}+{:-<20}+{:-<20}+".format("", "", "", "", "", ""))

        for id_E, DNI_E, nombre, tlf, salario, id_localidad in empleados:
            print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format(id_E, DNI_E, nombre, tlf, salario, id_localidad))

        print("+{:-<20}+{:-<20}+{:-<20}+{:-<20}+{:-<20}+{:-<20}+".format("", "", "", "", "", ""))

    except OperationalError as error:
        print("Error al abrir:", error)
    finally:
        cursor.close()

def eliminarEmpleado():
    try:
        # Conectar a la base de datos
        bd = connect("BDEjercicio2.db")
        cursor = bd.cursor()

        # Listar los empleados
        sentencia = "SELECT * FROM empleado;"
        cursor.execute(sentencia)
        empleados = cursor.fetchall()

        print("+{:-<20}+{:-<20}+{:-<20}+{:-<20}+{:-<20}+{:-<20}+".format("", "", "", "", "",""))
        print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format("id_E", "DNI_E", "nombre", "tlf", "salario","id_localidad"))
        print("+{:-<20}+{:-<20}+{:-<20}+{:-<20}+{:-<20}+{:-<20}+".format("", "", "", "", "",""))

        for id_E, DNI_E, nombre, tlf, salario,id_localidad in empleados:
            print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format( id_E, DNI_E, nombre, tlf, salario,id_localidad ))

        print("+{:-<20}+{:-<20}+{:-<20}+{:-<20}+{:-<20}+{:-<20}+".format("", "", "", "", "",""))

        print("Seleccione un ID a eliminar")
        idEmpleado=input("\nId a eliminar: ")
        sentencia= "DELETE FROM empleado WHERE id_E=?"
        cursor.execute(sentencia,[idEmpleado])
        bd.commit();
        print("Datos eliminados correctamente")
    except OperationalError as error:
        print("Error al abrir:", error)
    finally:
        cursor.close()

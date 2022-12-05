from sqlite3 import *

def crearBD():
    try:
        bd = connect("BDEjercicio1.db")
        cursor = bd.cursor()
        tablas = [
            ''' 
			CREATE TABLE IF NOT EXISTS "alumno"(
				"num_matricula" INTEGER NOT NULL,
				"nombre" TEXT NOT NULL,
				"fecha_nacimiento" TEXT NOT NULL,
				"tlf" TEXT NOT NULL,
				PRIMARY KEY ("num_matricula" AUTOINCREMENT)
			);
		''',
        '''
            CREATE TABLE IF NOT EXISTS "profesor"(
                "id_P" INTEGER NOT NULL,
                "NIf_P" TEXT NOT NULL,
                "nombre" TEXT NOT NULL,
                "especialidad" TEXT NOT NULL,
                "tlf" TEXT NOT NULL,
                PRIMARY KEY ("id_P" AUTOINCREMENT)
            );
        ''',
        '''
            CREATE TABLE IF NOT EXISTS "asignatura"(
                "cod_asignatura" INTEGER NOT NULL,
                "nombre" TEXT NOT NULL,
                "id_P" INTEGER NOT NULL,
                PRIMARY KEY ("cod_asignatura" AUTOINCREMENT)
                FOREIGN KEY ("id_P") REFERENCES profesor ("id_P")
            );
        ''',
        '''
            CREATE TABLE IF NOT EXISTS "alumno_asignatura"(
                "cod_Alum_asig" INTEGER NOT NULL,
                "cod_asignatura" INTEGER NOT NULL,
                "num_matricula" INT  NOT NULL,
                PRIMARY KEY ("cod_Alum_asig" AUTOINCREMENT),
                FOREIGN KEY ("cod_asignatura") REFERENCES asignatura ("cod_asignatura"),
                FOREIGN KEY ("num_matricula") REFERENCES alumno ("num_matricula")
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
        bd = connect("BDEjercicio1.db")
        cursor = bd.cursor()
        tablas = [
            """
            INSERT INTO alumno
            (nombre, fecha_nacimiento, tlf)
            VALUES
            ('Manu', '22-2-1997','789456123'),
            ('Gaby', '8-5-1997','789456123'),
            ('Agu', '13-7-1996','789456123');
            """,
            """
            INSERT INTO profesor
            (NIf_P, nombre, especialidad, tlf)
            VALUES
            ('32165498a','Juan', 'Lengua','789456123'),    
            ('32165498a','Pepe', 'Matematicas','789456123');
            """,
            """
            INSERT INTO asignatura
            (nombre, id_P)
            VALUES
            ('Lengua', '1'),
            ('Mates', '2');

            """,
            """
            INSERT INTO alumno_asignatura
            (cod_asignatura, num_matricula)
            VALUES
            ('1', '1'),
            ('1', '2'),
            ('2', '3');
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

def insertaAlumno():
    try:
        bd = connect("BDEjercicio1.db")
        cursor = bd.cursor()
        nombre=input("\nNombre: ")
        fecha=input("\nFecha: ")
        tlf=input("\nTLF: ")
        sentencia= "INSERT INTO alumno (nombre, fecha_nacimiento, tlf) VALUES (?,?,?)"
        cursor.execute(sentencia,[nombre,fecha,tlf])

        bd.commit()  # Guardamos los cambios al terminar el ciclo
        print("Datos insertados correctamente")
    except OperationalError as error:
        print("Error al abrir:", error)
    finally:
        cursor.close()

def insertarProfesor():
    try:
        bd = connect("BDEjercicio1.db")
        cursor = bd.cursor()
        nif=input("\nNIF: ")
        nombre=input("\nNombre: ")
        especialidad=input("\nEspecialidad: ")
        tlf=input("\nTLF: ")
        sentencia= "INSERT INTO profesor (NIf_P, nombre, especialidad, tlf) VALUES (?,?,?,?)"
        cursor.execute(sentencia,[nif,nombre,especialidad,tlf])

        bd.commit()  # Guardamos los cambios al terminar el ciclo
        print("Datos insertados correctamente")
    except OperationalError as error:
        print("Error al abrir:", error)
    finally:
        cursor.close()

def eliminarProfesor():
    try:
        bd = connect("BDEjercicio1.db")
        cursor = bd.cursor()

        # Listar los profesores
        sentencia = "SELECT * FROM profesor;"
        cursor.execute(sentencia)
        empleados = cursor.fetchall()

        print("+{:-<20}+{:-<20}+{:-<20}+{:-<20}+{:-<20}+".format("", "", "", "", ""))
        print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format("id_P", "NIf_P", "nombre", "especialidad", "tlf"))
        print("+{:-<20}+{:-<20}+{:-<20}+{:-<20}+{:-<20}+".format("", "", "", "", ""))

        for id_P, NIf_P, nombre, especialidad, tlf in empleados:
            print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format(id_P, NIf_P, nombre, especialidad, tlf))

        print("+{:-<20}+{:-<20}+{:-<20}+{:-<20}+{:-<20}+".format("", "", "", "", ""))

        idProfe=input("\nId a eliminar: ")
        sentencia= "DELETE FROM profesor WHERE id_P=?"
        cursor.execute(sentencia,[idProfe])
        bd.commit();
        print("Datos eliminados correctamente")
    except OperationalError as error:
        print("Error al abrir:", error)
    finally:
        cursor.close()

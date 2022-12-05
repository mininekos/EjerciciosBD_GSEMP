from sqlite3 import *
from conecionBD import *

DESPEDIR=3
CONTRATAR=8

#Crear BBDD
#crearBD()

#Insertar datos iniciales
#insertarDatos()

for i in range(DESPEDIR):
    eliminarEmpleado()

for i in range(CONTRATAR):
    insertarEmpleado()
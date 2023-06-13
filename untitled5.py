# -*- coding: utf-8 -*-
"""
Created on Wed May 31 19:39:29 2023

@author: Alumno
"""

#Conectarse a BD con PyODBC:

import pyodbc

# Establecer los parámetros de conexión
#Establecer los parámetros de conexión
server = 'localhost'
database = 'empresa'
username = 'root'
password = '1234'


# Establecer la cadena de conexión
connection_string = f"DRIVER={{MySQL ODBC 8.0 Unicode Driver}};SERVER={server};DATABASE={database};UID={username};PWD={password}"
# Establecer la conexión
conn = pyodbc.connect(connection_string)

# Crear un cursor para ejecutar consultas
cursor = conn.cursor()

# Ejecutar una consulta SELECT()
cursor.execute("SELECT * FROM empleado")

# Obtener los resultados de la consulta
results = cursor.fetchall()
print(results)

# Iterar sobre los resultados e imprimirlos
for row in results:
    print(row)

# Cerrar el cursor y la conexión
cursor.close()
conn.close()

del results[4]
print(results)

x = list(map(lambda x: (x, x), results))
print(x)

# -*- coding: utf-8 -*-
"""
Created on Mon May  8 18:09:52 2023

@author: Alumno

import pymysql #1. pip3 install --upgrade pip 2. pip3 install pymysql
import pandas as pd
import numpy as np
import collections
import itertools
from datetime import date, datetime, timedelta
import random

################ MySQL ###################
database = 'mibd'
username = 'root'
password = '1234'
db = pymysql.connect(host="127.0.0.1", user=username, passwd=password, database=database)
cursor = db.cursor()# prepare a cursor object using cursor() method


def generar_fecha_aleat():
    inicio = datetime(1940, 1, 1)
    final = datetime(2023, 1, 1)
    random_date = inicio + (final - inicio) * random.random()
    return random_date



db.autocommit(True)
# prepare a cursor object using cursor() method
cursorMySQL = db.cursor()


cursorMySQL.execute("CREATE DATABASE IF NOT EXISTS musica")
cursorMySQL.execute("select @@version")
output = cursorMySQL .fetchall()
print(output)

cursorMySQL.execute("USE musica")

cursorMySQL.execute(
   " CREATE TABLE  IF NOT EXISTS grupo( "\
      " id int NOT NULL, "\
      " nombre varchar(100) DEFAULT NULL, "\
      " numero_miembros INT DEFAULT NULL, "\
      " fecha_fundacion DATE DEFAULT NULL, "\
      " genero varchar(45) DEFAULT NULL, "\
      " PRIMARY KEY (id) "\
   " ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci "
)

cursorMySQL.execute(
   " CREATE TABLE  IF NOT EXISTS artista( "\
      " id int NOT NULL, "\
      " nombre varchar(65) DEFAULT NULL, "\
      " fecha_nacimiento DATE DEFAULT NULL, "\
      " rol varchar(15) DEFAULT NULL, "\
      " id_grupo INT,  "\
      " PRIMARY KEY (id) "\
   " ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci "
)

   
def insertar_filas_tabla_grupo():    
    lista1= ["Fifty", "Forever", "Crypto", "Amazing", "Smart", "Disgunting", "Hating", "Wisconsin", "Seven", "Green", "Red", "Orange", "White", "Black", "Crips", "Heaven", "Fucking", "Bloody", "Holly", "Blinking", "Shaking", "Disgunting", "Miss", "Mistaken","Mistaking","", "Making", "Moving", "Catastrophic", "Drinking", "Running", "Driving", "Killing", "Changing", "Printing", "Calling", "Building", "Changing", "Spending", "California", "Marihuana", "Sky", "Barbituric", "Pretty", "Closing","Frozen", "Frozen", "Frying", "Flying", "Diving", "Smashing", "Talking", "Eating", "Eighteen", "Breaking", "Breaching"]
    lista2= ["Pacos", "Talibanes", "Tormenta", "Bodega", "Sachos", "Mercenarios", "Cerdos", "Pulpos", "Zombies", "Caballos", "Pijamas", "Payasos",  "Piratas", "Bermudas", "Bichos", "Falling", "Calamares", "Carros", "Corsarios", "Vigo", "Zopenco", "Uruguayos", "Átomos", "Ineptos", "Alguaciles", "Ejecutivos", "Calabazas", "Tomatoes", "Potatoes", "SignalS", "Cows", "Cowboys", "Glasses", "Beaches", "Peaches", "Breaches", "Babies", "Killers", "Torpedo", ]
    generos_musicales = ["pop", "rock", "jazz", "regaeton", "rap", "trap", "country", "hip hop", "punk", "grunge"]
    for i in range(50000):
        parte1 = random.choice (lista1)
        parte2= random.choice (lista2)
        nombre_grupo = parte1+" "+parte2
        #print (nombre_grupo)
        genero = random.choice (generos_musicales)
        cursor.execute("INSERT INTO grupo (id, nombre, numero_miembros, fecha_fundacion, genero) VALUES (%s,%s,%s,%s,%s);",(i, nombre_grupo, random.randint(2, 10), generar_fecha_aleat(), genero))
   
   
def insertar_filas_tabla_artista():    
    lista1=  ["JOSE","ANTONIO","JUAN","MANUEL","FRANCISCO","LUIS", "JAVIER", "MIGUEL","CARLOS","JESUS", "DAVID","DANIEL","PEDRO","ALEJANDRO","MARIA","CARMEN","ANA","ISABEL","DOLORES","PILAR","TERESA","ROSA","JOSEFA","CRISTINA","ANGELES","LAURA","ANTONIA","ELENA","MARTA", "KENIA", "NAHIA", "ENZO", "George", "Charles", "Michael", "James", "Kenneth", "Pauline", "Dorothy", "Jennifer", "Jacqueline", "Sylvia", "Phillip", "Margaret", "Florence", "Catherine","Rose", "Beatrice", "Lillian", "Hilda", "Christine", "Thelma", "Ruth", "Irene", "Nathaniel", "Josephine", "Theresa", "Diana", "Pamela", "Natalie", "Claudia", "Caroline", "Austin","Sheila", "Felix", "Iria", "Lisa", "Rachael", "Lucy", "Lidia", "Iria", "Monica"]
    lista2= ["Garcia", "Rodriguez", "Gonzalez", "Fernandez","Lopez", "Martinez", "Sanchez", "Pérez", "Shevchenko", "Bondarenko","Kovalenko","Boyko","Tkachenko","Kravchenko", "Myroshnychenko", "Litvinenko", "Nazarenko", "Polyakova", "Nykolenko", "Uriburu", "Sagasti", "Yuste", "Costa", "Izaguirre", "Velasco", "Romero", "Moreno", "Ruiz", "Urriaga","Pieldelobo", "Piesplanos", "Pechoabierto", "Escohotado", "Piernavieja", "Parraverde", "Zas", "Chinchurreta", "Piernabierta", "Fajardo",  "Viejobueno","Eguiguren", "Echeverri", "Aramburu", "Goicoechea", "Sagasta", "Berricoechea", "Lizarraga", "Iturbide" ,"Agirregomezkorta", "Gerenabarrena", "Schneider", "Wagner", "Bauer", "Neumann", "Zimmermann", "Einstein", "Wolf", "Taylor", "Wilson", "Robinson", "White", "Green", "Wood", "Cooper", "Turner", "King", "Moore", "Lee", "Watson", "James", "Stuart", "Young", "Lloyd", "Kowalski", "Lewandowski", "Dabrowski", "Tochtomyszewicz", "Iturriberri", "Mendikoetxea", "Agirregomezkorta", "Garai","Zuazubizkar", "Andetxaga", "Beitialarrangoitia", "Barinagarementeria" ,"Agirregomezkorta" ,"Gabikagogeaskoa"  , "GaraiGordobil","Khalifa", "Abubaker", "Benmansour", "Sawadogo", "Alonso", "Carballo" ]
    rol_list = ["solista", "bateria", "bajista", "guitarrista", "pianista"]
    for i in range(500000):
        parte1 = random.choice (lista1)
        parte2= random.choice (lista2)
        parte3= random.choice (lista2)
       
        nombre = parte1+" "+parte2+" "+parte3
        #print (nombre)
        rol = random.choice (rol_list)
        #print(rol)
        cursor.execute("INSERT INTO artista (id, nombre, fecha_nacimiento, rol, id_grupo) VALUES (%s,%s,%s,%s,%s);",(i, nombre, generar_fecha_aleat(), rol, random.randint(0, 50000)))
   
   
   
insertar_filas_tabla_artista()
insertar_filas_tabla_grupo()
   
db.close() # desconecta del servidor local

print("Fin del programa...")
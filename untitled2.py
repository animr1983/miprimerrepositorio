c

   
def insertar_filas_tabla_grupo():    
    lista1= ["Fifty", "Forever", "Crypto", "Amazing", "Smart", "Disgunting", "Hating", "Wisconsin", "Seven", "Green", "Red", "Orange", "White", "Black", "Crips", "Heaven", "Fucking", "Bloody", "Holly", "Blinking", "Shaking", "Disgunting", "Miss", "Mistaken","Mistaking","", "Making", "Moving", "Catastrophic", "Drinking", "Running", "Driving", "Killing", "Changing", "Printing", "Calling", "Building", "Changing", "Spending", "California", "Marihuana", "Sky", "Barbituric", "Pretty", "Closing","Frozen", "Frozen", "Frying", "Flying", "Diving", "Smashing", "Talking", "Eating", "Eighteen", "Breaking", "Breaching"]
    lista2= ["Pacos", "Talibanes", "Tormenta", "Bodega", "Sachos", "Mercenarios", "Cerdos", "Pulpos", "Zombies", "Caballos", "Pijamas", "Payasos",  "Piratas", "Bermudas", "Bichos", "Falling", "Calamares", "Carros", "Corsarios", "Vigo", "Zopenco", "Uruguayos", "Átomos", "Ineptos", "Alguaciles", "Ejecutivos", "Calabazas", "Tomatoes", "Potatoes", "SignalS", "Cows", "Cowboys", "Glasses", "Beaches", "Peaches", "Breaches", "Babies", "Killers", "Torpedo", ]
    generos_musicales = ["pop", "rock", "jazz", "regaeton", "rap", "trap", "country", "hip hop", "punk", "grunge"] 
    for i in range(150000,300000):
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
    for i in range(1000000,2000000):
        parte1 = random.choice (lista1)
        parte2= random.choice (lista2)
        parte3= random.choice (lista2)
       
        nombre = parte1+" "+parte2+" "+parte3
        #print (nombre)
        rol = random.choice (rol_list)
        #print(rol)
        cursor.execute("INSERT INTO artista (id, nombre, fecha_nacimiento, rol, id_grupo) VALUES (%s,%s,%s,%s,%s);",(i, nombre, generar_fecha_aleat(), rol, random.randint(0,300000)))
   
   
   
insertar_filas_tabla_artista()
insertar_filas_tabla_grupo()
   
db.close() # desconecta del servidor local

print("Fin del programa...")






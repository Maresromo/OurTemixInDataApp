import duckdb

#Inicia la conexión en una base de datos existente, y si no existe la crea
con = duckdb.connect("esolmetruoa.db")

con.execute('''
CREATE TABLE IF NOT EXISTS estaciones (
            id_estacion INTEGER PRIMARY KEY,      --ID de la estación
            nombre VARCHAR,                --Nombre de la estacion
            );
''')

#Cerrar la conexión 
con.close()
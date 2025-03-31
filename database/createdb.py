import duckdb

#Inicia la conexión en una base de datos existente, y si no existe la crea
con = duckdb.connect("esolmetruoa.db")

con.execute('''
CREATE TABLE IF NOT EXISTS sensores (
            id_sensor INTEGER PRIMARY KEY,      --ID de la estación
            descripcion VARCHAR,                --Describe qué tipo de sensor es
            );
''')

#Cerrar la conexión 
con.close()
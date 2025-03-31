from unittest import result
import duckdb

con = duckdb.connect("esolmetruoa.db")

result0 = con.execute("SELECT id_sensor FROM sensores;").fetchall()

for row in result0:
    print(row)
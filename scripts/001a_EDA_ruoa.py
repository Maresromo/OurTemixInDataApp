# %%
import pandas as pd
# %%
f = "../data/001_raw/RUOA/Datos_hora/2016_RUOA_HR.csv"
data = pd.read_csv(
    f,
    skiprows=[0,2,3],
    index_col=0,
    parse_dates=True,
    dayfirst=True,
)
data
# %%
del data["RECORD"]
# %%
columnas = data.columns

for columna in columnas:
    if pd.api.types.is_float_dtype(data[columna]):
        print("La columna es flotante")
    else: print("La columna NO es flotante")
# %%
def verificar_tipos_variables(cols = columnas):
    for columna in cols:
        assert type(columna) is int, f"La {columna} no es entero"
    
    print("Todas las columnas pasaron la prueba de tipos")
# %%
verificar_tipos_variables(columnas)
# %%
prueba = data.dtypes
type(prueba)
# %%
prueba
# %%

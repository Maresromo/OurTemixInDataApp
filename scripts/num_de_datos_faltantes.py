# %%
import pandas as pd
import numpy as np
# %%
def read_RUOA(f):
    data = pd.read_csv(
    f,
    skiprows=[0,2,3],
    index_col=0,
    parse_dates=True,
    dayfirst=True,
    )
    del data["RECORD"]
    return data

# %%
# Asegurar que el índice sea datetime
def llenar_Nan(data):
    # Eliminar la primera fila si está completamente vacía
    if data.iloc[0].isna().all():
        data = data.iloc[1:]

    # Asegurarse de que el índice es de tipo datetime
    data.index = pd.to_datetime(data.index)

    # Eliminar duplicados en el índice
    data = data.loc[~data.index.duplicated(keep='first')]

    # Obtener el año del primer dato (asumiendo que todos los datos son del mismo año)
    year = data.index.year[0]

    # Crear el rango de fechas completo para ese año
    start_date = f'{year}-01-01 00:00:00'
    end_date = f'{year}-12-31 23:00:00'
    full_index = pd.date_range(start=start_date, end=end_date, freq='H')

    # Reindexar para llenar los huecos con NaN
    data = data.reindex(full_index)
    
    return data

# %%
def proporcion_faltantes(data):
    total_filas = len(data)
    faltantes = data.isna().sum()  # Por columna
    proporcion_faltantes = faltantes / total_filas
    return print(proporcion_faltantes)
# %%
proporcion_faltantes(data)
# %%
f = "../data/001_raw/RUOA/Datos_hora/2017-RUOA-HR.csv"
data = read_RUOA(f)
data = llenar_Nan(data)
#proporcion_faltantes(data)
data
# %%

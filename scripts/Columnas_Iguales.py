# %%
import pandas as pd
import numpy as np
from glob import glob
# %%
glob("../data/001_raw/ESOLMET/*")
# %%
def read_ruoa(path):
    df = pd.read_csv(path, skiprows=[0,2], 
                     #usecols=[0,1,2,3,8], 
            encoding= 'unicode_escape', index_col=0, parse_dates=True)
    return df
# %%
read_ruoa("../data/001_raw/ESOLMET/2010_ESOLMET.csv")
# %%

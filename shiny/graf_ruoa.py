import plotly.express as px
import pandas as pd
from shiny.express import input, ui
from shinywidgets import render_plotly

f = "../data/001_raw/RUOA/Datos_hora/2016_RUOA_HR.csv"
data = pd.read_csv(
    f,
    skiprows=[0,2,3],
    index_col=0,
    parse_dates=True,
    dayfirst=True,
    )
del data["RECORD"]

ui.page_opts(title="Histograma de RUOA", fillable=True)
with ui.layout_columns():

    @render_plotly
    def plot1():
        return px.histogram(data["Temp_Avg"])

    @render_plotly
    def plot2():
        return px.histogram(data["WSpeed_Avg"])

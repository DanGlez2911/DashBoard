import numpy as np 
import pandas as pd
import plotly.express as px 
import matplotlib.pyplot as plt

siniestros = '/Users/daniel/Downloads/Siniestros.csv'

df_siniestros= pd.read_csv(siniestros, encoding = 'cp1252', sep=',', on_bad_lines= 'warn' )
df_siniestros[['NUMERO DE SINIESTROS']] = df_siniestros[['NUMERO DE SINIESTROS']].apply(lambda x: pd.factorize(x)[0])
df_siniestros = df_siniestros.dropna()


def graficodebarras():
    barras = df_siniestros.groupby('ENTIDAD ')['NUMERO DE SINIESTROS'].sum().reset_index()
    fig = px.bar(barras, x='ENTIDAD ', y='NUMERO DE SINIESTROS', color='ENTIDAD ', height=500, width=1000)
    fig.update_layout(title='Numero de Siniestros registrados por Estado', xaxis_title="Estados", yaxis_title="Numero de Siniestros")
    fig.update_yaxes(title='Numero Siniestros')
    return fig

graficodebarras()



    
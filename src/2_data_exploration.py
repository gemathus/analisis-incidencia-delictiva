import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd
import dateutil
from pprint import pprint
#headers = ;año_hechos;mes_hechos;fecha_hechos;delito;categoria_delito;colonia_hechos;alcaldia_hechos;longitud;latitud;mes_num
parse_dates = ['fecha_hechos']
carpetas_investigacion = pd.read_csv('../data/carpetas_2016_2019.csv', sep=";", parse_dates=True)
carpetas_investigacion['fecha_hechos'] = carpetas_investigacion['fecha_hechos'].apply(dateutil.parser.parse)
pprint(carpetas_investigacion.head())

df_1 = carpetas_investigacion['fecha_hechos'].groupby(carpetas_investigacion['fecha_hechos'].dt.to_period("M")).agg('count')

data = np.array([df_1.index, df_1])
dataset = pd.DataFrame({'Mes':data[0,:],'Carpetas':data[1,:]})
dataset.plot(x='Mes', y='Carpetas').show()
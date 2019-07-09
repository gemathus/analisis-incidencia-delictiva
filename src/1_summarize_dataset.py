import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import dateutil
from pprint import pprint
meses = {"Enero":1, "Febrero":2, "Marzo":3, "Abril":4, "Mayo":5, "Junio":6, "Julio":7, "Agosto":8, "Septiembre":9, "Octubre":10,"Noviembre":11, "Diciembre":12, }
alcaldias_cdmx = ['CUAUHTEMOC', 'IZTAPALAPA', 'GUSTAVO A MADERO', 'BENITO JUAREZ', 'COYOACAN', 'MIGUEL HIDALGO', 'ALVARO OBREGON', 'VENUSTIANO CARRANZA', 'TLALPAN', 'AZCAPOTZALCO','IZTACALCO','XOCHIMILCO','TLAHUAC', 'LA MAGDALENA CONTRERAS', 'CUAJIMALPA DE MORELOS', 'MILPA ALTA']
def main():
    print("Leyendo datos de CSV y convirtinedo a Pandas.DataFrame...")
    carpetas_investigacion = pd.read_csv('../data/carpetas-de-investigacion-pgj-cdmx.csv', delimiter=';')
    print("Desechando datos de años anteriores al 2016")
    carpetas_investigacion = carpetas_investigacion[carpetas_investigacion['año_hechos'] >= 2016]
    print("Convirtiendo columna fecha_hechos a datetime")
    carpetas_investigacion['fecha_hechos'] = carpetas_investigacion['fecha_hechos'].apply(dateutil.parser.parse)

    print("Agregando columna de mes numérico")
    carpetas_investigacion['mes_num'] = carpetas_investigacion['mes_hechos'].map(lambda x: meses[x])
    #valores_2016_a_2018 = carpetas_investigacion[carpetas_investigacion['año_hechos'] < 2019]
    print("Quitando columnas no usadas")
    carpetas_investigacion = carpetas_investigacion.drop(['fiscalía', 
                            'agencia', 
                            'unidad_investigacion',
                            'fecha_inicio',
                            'mes_inicio',
                            'ao_inicio',
                            'calle_hechos',
                            'calle_hechos2',
                            'Geopoint'
                            ], axis=1)

    pprint(carpetas_investigacion.head())
    input("continuar...")
    print("Quitando datos que no sean de la CDMX")
    carpetas_investigacion = carpetas_investigacion[carpetas_investigacion['alcaldia_hechos'].isin(alcaldias_cdmx)]
    pprint(carpetas_investigacion['alcaldia_hechos'].value_counts())
    input("continuar...")
    print("guardando nuevo dataset")
    carpetas_investigacion.to_csv('../data/carpetas_2016_2019.csv', sep=";")
    print("dataset cuardado en '../data/carpetas_2016_2019.csv'")
    input("Presiona cualquier tecla para terminar")
    print("Bye")
    
if __name__ == "__main__":
    main()
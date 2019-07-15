import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, Polygon
import descartes
print("1/6 Leyendo archivo de cuadrantes...")
cuadrantes = gpd.read_file('../shape_files/cuadrantes_con_poblacion/cuadrantes_con_poblacion.shp')

print("2/6 Leyendo carpetas de investigación del 2016 al 2019...")
carpetas = pd.read_csv('../data/carpetas_2016_2019.csv', sep=";")

print("3/6 Creando punto a partir de long y lat.")
geometry = [Point(xy) for xy in zip(carpetas['longitud'],carpetas['latitud'])]
crs = {"init":"epsg:4326"}

print("4/6 Creando dataframe que incluya un punto (objeto de geometría)")
geo_carpetas = gpd.GeoDataFrame(carpetas, geometry = geometry, crs=crs)
cuadrantes = cuadrantes[cuadrantes.geometry.notnull()] #hay un dato nulo

print("5/6 Uniendo dataframes de carpetas y de polígonos de cuadrantes.")
df_carpetas_con_cuadrante = gpd.sjoin(geo_carpetas, cuadrantes, op='within')

print("6/6 Guardando nuevo shapefile en `/data/carpetas_2016_2019_con_cuadrante.shp`.")
df_carpetas_con_cuadrante.to_file('../data/carpetas_2016_2019_con_cuadrante.shp')

#todo: poner referencia a sjoin
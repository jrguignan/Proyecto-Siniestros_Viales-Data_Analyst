import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

def tipo_datos(df): #verifica el tipo de datos y devuelve todos los tipos de datos por cada columna y nulos
    dic = {'Columna': [], 'Tipo_datos': [], '%_nulos': [], 'Nulos': [], 'Largo':[]}
    for column in df.columns: #itera sobre columnas
        tipos_de_datos = df[column].apply(lambda x: type(x).__name__).unique() #nos devuelve sobre la columna los tipos de datos sin repeticion
        isnap = df[column].isna().sum()/df[column].shape[0]*100 # calcula el porcentaje de nans 
        isna = df[column].isna().sum() #calcula la cantidad de nans
        largo_datos = df[column].apply(lambda x: len(str(x))).unique()
        dic['Columna'].append(column) # adjunta datos
        dic['Tipo_datos'].append(tipos_de_datos)
        dic['%_nulos'].append(isnap)
        dic['Nulos'].append(isna)
        dic['Largo'].append(largo_datos)
    
    datf = pd.DataFrame(dic) #genera dataframe para devolver

    return datf


def convertir_a_time(x):
    '''
    Convierte un valor a un objeto de tiempo (time) de Python si es posible.
    '''
    if isinstance(x, str):
        try:
            return datetime.strptime(x, "%H:%M:%S").time()
        except ValueError:
            return None
    elif isinstance(x, datetime):
        return x.time()
    return x


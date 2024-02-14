import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
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


def accidentes_mensuales(df):
    '''
    Crea gráficos de línea para la cantidad de víctimas de accidentes mensuales por año.

    '''
    # Se obtiene una lista de años únicos
    años = df['Anio'].unique()

    # Se define el número de filas y columnas para la cuadrícula de subgráficos
    n_filas = 3
    n_columnas = 2

    # Se crea una figura con subgráficos en una cuadrícula de 2x3
    fig, axes = plt.subplots(n_filas, n_columnas, figsize=(14, 8))

    # Se itera a través de los años y crea un gráfico por año
    for i, year in enumerate(años):
        fila = i // n_columnas
        columna = i % n_columnas
        
        # Se filtran los datos para el año actual y agrupa por mes
        data_mensual = (df[df['Anio'] == year]
                        .groupby('Mes')
                        .agg({'Cantidad victimas':'sum'}))
        
        # Se configura el subgráfico actual
        ax = axes[fila, columna]
        data_mensual.plot(ax=ax, kind='line')
        ax.set_title('Anio ' + str(year)) ; ax.set_xlabel('Mes') ; ax.set_ylabel('Cantidad de Víctimas')
        ax.legend_ = None
        
    # Se muestra y acomoda el gráfico
    plt.tight_layout()
    plt.show()


def cantidad_victimas_mensuales(df):
    '''
    Crea un gráfico de barras que muestra la cantidad de víctimas de accidentes por mes.
    '''
    # Se agrupa por la cantidad de víctimas por mes
    data = df.groupby('Mes').agg({'Cantidad victimas':'sum'}).reset_index()
    
    # Se grafica
    plt.figure(figsize=(6,4))
    ax = sns.barplot(x='Mes', y='Cantidad victimas', data=data)
    ax.set_title('Cantidad de victimas por Mes')
    ax.set_xlabel('Mes') ; ax.set_ylabel('Cantidad de Accidentes')
    
    # Se imprime resumen
    print(f'El mes con menor cantidad de víctimas tiene {data.min()[1]} víctimas')
    print(f'El mes con mayor cantidad de víctimas tiene {data.max()[1]} víctimas')
    
    # Se muestra el gráfico
    plt.show()

def cantidad_victimas_por_dia_semana(df):
    '''
    Crea un gráfico de barras que muestra la cantidad de víctimas de accidentes por día de la semana.
    '''
    # Se convierte la columna 'fecha' a tipo de dato datetime
    df['Fecha'] = pd.to_datetime(df['Fecha'])
    
    # Se extrae el día de la semana (0 = lunes, 6 = domingo)
    df['Día semana'] = df['Fecha'].dt.dayofweek
    
    # Se mapea el número del día de la semana a su nombre
    dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    df['Nombre día'] = df['Día semana'].map(lambda x: dias_semana[x])
    
    # Se cuenta la cantidad de accidentes por día de la semana
    data = df.groupby('Nombre día').agg({'Cantidad victimas':'sum'}).reset_index()
      
    # Se crea el gráfico de barras
    plt.figure(figsize=(6, 3))
    ax = sns.barplot(x='Nombre día', y='Cantidad victimas', data=data, order=dias_semana)
    
    ax.set_title('Cantidad de Accidentes por Día de la Semana') ; ax.set_xlabel('Día de la Semana') ; ax.set_ylabel('Cantidad de Accidentes')
    plt.xticks(rotation=45)
    
    # Se muestran datos resumen
    print(f'El día de la semana con menor cantidad de víctimas tiene {data.min()[1]} víctimas')
    print(f'El día de la semana con mayor cantidad de víctimas tiene {data.max()[1]} víctimas')
    print(f'La diferencia porcentual es de {round((data.max()[1] - data.min()[1]) / data.min()[1] * 100,2)}')
    
    # Se muestra el gráfico
    plt.show()

def crea_categoria_momento_dia(hora):
  """
  Devuelve la categoría de tiempo correspondiente a la hora proporcionada.

  Parameters:
    hora: La hora a clasificar.

  Returns:
    La categoría de tiempo correspondiente.
  """
  if hora.hour >= 6 and hora.hour <= 10:
    return "Mañana"
  elif hora.hour >= 11 and hora.hour <= 13:
    return "Medio día"
  elif hora.hour >= 14 and hora.hour <= 18:
    return "Tarde"
  elif hora.hour >= 19 and hora.hour <= 23:
    return "Noche"
  else:
    return "Madrugada"

def cantidad_accidentes_por_categoria_tiempo(df):
    '''
    Calcula la cantidad de accidentes por categoría de tiempo y muestra un gráfico de barras.
    '''
    # Se aplica la función crea_categoria_momento_dia para crear la columna 'categoria_tiempo'
    df['Categoria tiempo'] = df['Hora'].apply(crea_categoria_momento_dia)

    # Se cuenta la cantidad de accidentes por categoría de tiempo
    data = df['Categoria tiempo'].value_counts().reset_index()
    data.columns = ['Categoria tiempo', 'Cantidad accidentes']

    # Se calculan los porcentajes
    total_accidentes = data['Cantidad accidentes'].sum()
    data['Porcentaje'] = (data['Cantidad accidentes'] / total_accidentes) * 100
    
    # Se crea el gráfico de barras
    plt.figure(figsize=(6, 4))
    ax = sns.barplot(x='Categoria tiempo', y='Cantidad accidentes', data=data)

    ax.set_title('Cantidad de Accidentes por Categoría de Tiempo') ; ax.set_xlabel('Categoría de Tiempo') ; ax.set_ylabel('Cantidad de Accidentes')

    # Se agrega las cantidades en las barras
    for index, row in data.iterrows():
        ax.annotate(f'{row["Cantidad accidentes"]}', (index, row["Cantidad accidentes"]), ha='center', va='bottom')

    # Se muestra el gráfico
    plt.show()

def cantidad_accidentes_por_horas_del_dia(df):
    '''
    Genera un gráfico de barras que muestra la cantidad de accidentes por hora del día.
    '''
    # Se extrae la hora del día de la columna 'hora'
    df['Hora del día'] = df['Hora'].apply(lambda x: x.hour)

    # Se cuenta la cantidad de accidentes por hora del día
    data = df['Hora del día'].value_counts().reset_index()
    data.columns = ['Hora del día', 'Cantidad de accidentes']

    # Se ordena los datos por hora del día
    data = data.sort_values(by='Hora del día')

    # Se crea el gráfico de barras
    plt.figure(figsize=(12, 4))
    ax = sns.barplot(x='Hora del día', y='Cantidad de accidentes', data=data)

    ax.set_title('Cantidad de Accidentes por Hora del Día') ; ax.set_xlabel('Hora del día') ; ax.set_ylabel('Cantidad de accidentes')

    # Se agrega las cantidades en las barras
    for index, row in data.iterrows():
        ax.annotate(f'{row["Cantidad de accidentes"]}', (row["Hora del día"], row["Cantidad de accidentes"]), ha='center', va='bottom')

    # Se muestra el gráfico
    plt.show()

def cantidad_accidentes_semana_fin_de_semana(df):
    '''
    Genera un gráfico de barras que muestra la cantidad de accidentes por tipo de día (semana o fin de semana).
    '''
    # Se convierte la columna 'fecha' a tipo de dato datetime
    df['Fecha'] = pd.to_datetime(df['Fecha'])
    
    # Se extrae el día de la semana (0 = lunes, 6 = domingo)
    df['Dia semana'] = df['Fecha'].dt.dayofweek
    
    # Se crea una columna 'tipo_dia' para diferenciar entre semana y fin de semana
    df['Tipo de día'] = df['Dia semana'].apply(lambda x: 'Fin de Semana' if x >= 5 else 'Semana')
    
    # Se cuenta la cantidad de accidentes por tipo de día
    data = df['Tipo de día'].value_counts().reset_index()
    data.columns = ['Tipo de día', 'Cantidad de accidentes']
    
    # Se crea el gráfico de barras
    plt.figure(figsize=(6, 4))
    ax = sns.barplot(x='Tipo de día', y='Cantidad de accidentes', data=data)
    
    ax.set_title('Cantidad de accidentes por tipo de día') ; ax.set_xlabel('Tipo de día') ; ax.set_ylabel('Cantidad de accidentes')
    
    # Se agrega las cantidades en las barras
    for index, row in data.iterrows():
        ax.annotate(f'{row["Cantidad de accidentes"]}', (index, row["Cantidad de accidentes"]), ha='center', va='bottom')
    
    # Se muestra el gráfico
    plt.show()

def distribucion_edad(df):
    '''
    Genera un gráfico con un histograma y un boxplot que muestran la distribución de la edad de los involucrados en los accidentes.
    '''

    #Borro los SD
    df.drop(df[df['Edad']=='SD'].index,inplace=True)
    # Se crea una figura con un solo eje x compartido
    fig, ax = plt.subplots(2, 1, figsize=(12, 6), sharex=True)
    
    # Se grafica el histograma de la edad
    sns.histplot(df['Edad'], kde=True, ax=ax[0])
    ax[0].set_title('Histograma de Edad') ; ax[0].set_ylabel('Frecuencia')
    
    # Se grafica el boxplot de la edad
    sns.boxplot(x=df['Edad'], ax=ax[1])
    ax[1].set_title('Boxplot de Edad') ; ax[1].set_xlabel('Edad')
    
    # Se ajusta y muestra el gráfico
    plt.tight_layout()
    plt.show()
    
def distribucion_edad_por_anio(df):
    '''
    Genera un gráfico de boxplot que muestra la distribución de la edad de las víctimas de accidentes por año.
    '''
    # Se crea el gráfico de boxplot
    plt.figure(figsize=(12, 6))
    sns.boxplot(x='Anio', y='Edad', data=df)
    
    plt.title('Boxplot de Edades de Víctimas por Año') ; plt.xlabel('Anio') ; plt.ylabel('Edad de las Víctimas')
     
    # Se muestra el gráfico
    plt.show()

def cantidades_accidentes_por_anio_y_sexo(df):
    '''
    Genera un gráfico de barras que muestra la cantidad de accidentes por año y sexo.
    '''
    # Se crea el gráfico de barras
    plt.figure(figsize=(12, 4))
    sns.barplot(x='Anio', y='Edad', hue='Sexo', data=df,)
    
    plt.title('Cantidad de Accidentes por Año y Sexo')
    plt.xlabel('Anio') ; plt.ylabel('Edad de las víctimas') ; plt.legend(title='Sexo')
    
    # Se muestra el gráfico
    plt.show()
    


def edad_y_rol_victimas(df):
    '''
    Genera un gráfico de la distribución de la edad de las víctimas por rol.
    '''
    df.drop(df[df['Rol']=='SD'].index, inplace=True)
    plt.figure(figsize=(8, 4))
    sns.boxplot(y='Rol', x='Edad',data=df)
    plt.title('Edades por Condición')
    plt.show()
    
def distribucion_edad_por_victima(df):

    '''
    Genera un gráfico de la distribución de la edad de las víctimas por tipo de vehículo.
    '''
    #df.drop(df[df['Victima']=='SD'].index, inplace=True)
    # Se crea el gráfico de boxplot
    plt.figure(figsize=(14, 6))
    sns.boxplot(x='Victima', y='Edad', data=df)
    
    plt.title('Boxplot de Edades de Víctimas por tipo de vehículo que usaba') ; plt.xlabel('Tipo de vehiculo') ; plt.ylabel('Edad de las Víctimas')
     
    plt.show()
    
def cantidad_accidentes_sexo(df):
    '''
    Genera un resumen de la cantidad de accidentes por sexo de los conductores.

    Esta función toma un DataFrame como entrada y genera un resumen que incluye:

    * Un gráfico de barras que muestra la cantidad de accidentes por sexo de los conductores en orden descendente.
    * Un DataFrame que muestra la cantidad y el porcentaje de accidentes por sexo de los conductores.
    '''
    # Se convierte la columna 'fecha' a tipo de dato datetime
    df['Fecha'] = pd.to_datetime(df['Fecha'])
    
    # Se extrae el día de la semana (0 = lunes, 6 = domingo)
    df['Dia semana'] = df['Fecha'].dt.dayofweek
    
    # Se crea una columna 'tipo_dia' para diferenciar entre semana y fin de semana
    df['Tipo de día'] = df['Dia semana'].apply(lambda x: 'Fin de Semana' if x >= 5 else 'Semana')
    
    # Se cuenta la cantidad de accidentes por tipo de día
    data = df['Tipo de día'].value_counts().reset_index()
    data.columns = ['Tipo de día', 'Cantidad de accidentes']
    
    # Se crea el gráfico de barras
    plt.figure(figsize=(6, 4))
    ax = sns.barplot(x='Tipo de día', y='Cantidad de accidentes', data=data)
    
    ax.set_title('Cantidad de accidentes por tipo de día') ; ax.set_xlabel('Tipo de día') ; ax.set_ylabel('Cantidad de accidentes')
    
    # Se agrega las cantidades en las barras
    for index, row in data.iterrows():
        ax.annotate(f'{row["Cantidad de accidentes"]}', (index, row["Cantidad de accidentes"]), ha='center', va='bottom')
    
    # Se muestra el gráfico
    plt.show()

def cantidad_victimas_sexo_rol_victima(df):
    '''
    Genera un resumen de la cantidad de víctimas por sexo, rol y tipo de vehículo en un accidente de tráfico.

    Esta función toma un DataFrame como entrada y genera un resumen que incluye:

    * Gráficos de barras que muestran la cantidad de víctimas por sexo, rol y tipo de vehículo en orden descendente.
    * DataFrames que muestran la cantidad y el porcentaje de víctimas por sexo, rol y tipo de vehículo.
    '''
    # Se crea el gráfico
    fig, axes = plt.subplots(1, 3, figsize=(15, 4))

    # Gráfico 1: Sexo
    sns.countplot(data=df, x='Sexo', ax=axes[0])
    axes[0].set_title('Cantidad de víctimas por sexo') ; axes[0].set_ylabel('Cantidad de víctimas')

    # Se define una paleta de colores personalizada (invierte los colores)
    colores_por_defecto = sns.color_palette()
    colores_invertidos = [colores_por_defecto[0], colores_por_defecto[1]]
    
    # Gráfico 2: Rol
    df_rol = df.groupby(['Rol', 'Sexo']).size().unstack(fill_value=0)
    df_rol.plot(kind='bar', stacked=True, ax=axes[1], color=colores_invertidos)
    axes[1].set_title('Cantidad de víctimas por rol') ; axes[1].set_ylabel('Cantidad de víctimas') ; axes[1].tick_params(axis='x', rotation=45)
    axes[1].legend().set_visible(False)
    
    # Gráfico 3: Tipo de vehículo
    df_victima = df.groupby(['Victima', 'Sexo']).size().unstack(fill_value=0)
    df_victima.plot(kind='bar', stacked=True, ax=axes[2], color=colores_invertidos)
    axes[2].set_title('Cantidad de víctimas por tipo de vehículo') ; axes[2].set_ylabel('Cantidad de víctimas') ; axes[2].tick_params(axis='x', rotation=45)
    axes[2].legend().set_visible(False)

    # Se muestran los gráficos
    plt.show()
    

def cantidad_victimas_participantes(df):
    '''
    Genera un resumen de la cantidad de víctimas por número de participantes en un accidente de tráfico.

    Esta función toma un DataFrame como entrada y genera un resumen que incluye:

    * Un gráfico de barras que muestra la cantidad de víctimas por número de participantes en orden descendente.
    * Un DataFrame que muestra la cantidad y el porcentaje de víctimas por número de participantes.
    '''
    # Se ordenan los datos por 'Participantes' en orden descendente por cantidad
    ordenado = df['Participantes'].value_counts().reset_index()
    ordenado = ordenado.rename(columns={'Cantidad': 'participantes'})
    ordenado = ordenado.sort_values(by='count', ascending=False)
    
    plt.figure(figsize=(15, 4))
    
    # Se crea el gráfico de barras
    ax = sns.barplot(data=ordenado, x='Participantes', y='count', order=ordenado['Participantes'])
    ax.set_title('Cantidad de víctimas por participantes')
    ax.set_ylabel('Cantidad de víctimas')
    # Rotar las etiquetas del eje x a 45 grados
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment='right')

    # Se muestra el gráfico
    plt.show()
    

def cantidad_acusados(df):
    '''
    Genera un resumen de la cantidad de acusados en un accidente de tráfico.

    Esta función toma un DataFrame como entrada y genera un resumen que incluye:

    * Un gráfico de barras que muestra la cantidad de acusados en orden descendente.
    * Un DataFrame que muestra la cantidad y el porcentaje de acusados.
    '''
    df.drop(df[df['Acusado']=='SD'].index, inplace=True)
    # Se ordenan los datos por 'Participantes' en orden descendente por cantidad
    ordenado = df['Acusado'].value_counts().reset_index()
    ordenado = ordenado.rename(columns={'Cantidad': 'Acusado'})
    ordenado = ordenado.sort_values(by='count', ascending=False)
    
    plt.figure(figsize=(15, 4))
    
    # Crear el gráfico de barras
    ax = sns.barplot(data=ordenado, x='Acusado', y='count', order=ordenado['Acusado'])
    ax.set_title('Cantidad de acusados en los hechos') ; ax.set_ylabel('Cantidad de acusados') 
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment='right')

    # Se muestra el gráfico
    plt.show()

def accidentes_tipo_de_calle(df):
    '''
    Genera un resumen de los accidentes de tráfico por tipo de calle y cruce.

    Esta función toma un DataFrame como entrada y genera un resumen que incluye:

    * Un gráfico de barras que muestra la cantidad de víctimas por tipo de calle.
    * Un gráfico de barras que muestra la cantidad de víctimas en cruces.
    * Un DataFrame que muestra la cantidad y el porcentaje de víctimas por tipo de calle.
    * Un DataFrame que muestra la cantidad y el porcentaje de víctimas en cruces.
    '''
    
    # Se crea el gráfico
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))

    sns.countplot(data=df, x='Tipo de calle', ax=axes[0])
    axes[0].set_title('Cantidad de víctimas por tipo de calle') ; axes[0].set_ylabel('Cantidad de víctimas')

    sns.countplot(data=df, x='Cruce', ax=axes[1])
    axes[1].set_title('Cantidad de víctimas en cruces') ; axes[1].set_ylabel('Cantidad de víctimas')
    
    # Mostramos los gráficos
    plt.show()
![Power Bi](https://img.shields.io/badge/power_bi-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Pandas](https://img.shields.io/badge/-Pandas-333333?style=flat&logo=pandas)
![Numpy](https://img.shields.io/badge/-Numpy-333333?style=flat&logo=numpy)
![Seaborn](https://img.shields.io/badge/-Seaborn-333333?style=flat&logo=seaborn)
![Matplotlib](https://img.shields.io/badge/-Matplotlib-333333?style=flat&logo=matplotlib)


![henry](https://github.com/jrguignan/Proyecto-Siniestros_Viales-Data_Analyst/blob/main/images/Logo%20HENRY.png)

# Proyecto Siniestros Viales - Data Analyst
# Data Science & Data Analyst (PI-DA) 

<p align="center">
<img src="https://github.com/jrguignan/Proyecto-Siniestros_Viales-Data_Analyst/blob/main/images/SiniestrosV.jpeg"  height=300>
</p>
---

# Índice Rápido
* [Introducción](#Introducción)
* [Contexto](#Contexto)
* [Rol a desarrollar](#Rol-a-desarrollar)
* [Datos](#Datos)
* [Tareas Desarrolladas en Python](#Tareas-Desarrolladas-en-Python)
  * [ETL](#ETL)
  * [EDA](#EDA)
* [Tareas Desarrolladas en Power BI](#Tareas-Desarrolladas-en-Power-BI) 
  * [Dashboar](#Dashboar)
    * [Análisis Temporal](#Análisis-Temporal) 
    * [Análisis por Partes Involucradas](#Análisis-por-Partes-Involucradas) 
    * [Análisis por ubicación](#Análisis-por-Ubicación) 
  * [KPIs](#KPIs)   
* [Conclusiones y Recomendaciones](#Conclusiones-y-Recomendaciones)
* [Requerimientos](#Requerimientos)
* [Autor](#Autor)


# Introducción                  [<sup> Volver al Índice </sup>](#Índice-Rápido)

En este proyecto se simula el rol de un Data Analyst que forma parte del equipo de analistas de datos de una empresa consultora a la cual el **Observatorio de Movilidad y Seguridad Vial (OMSV)**, que es un centro de estudios que se encuentra bajo la órbita de la Secretaría de Transporte del Gobierno de la Ciudad Autónoma de Buenos Aires (CABA), les solicitó la elaboración de un proyecto de análisis de datos. 

Se espera como productos finales un reporte de las tareas realizadas y las principales conclusiones, asi como  la presentación de un dashboard interactivo que facilite la interpretación de la información y su análisis. <br>

# Contexto  [<sup> Volver al Índice </sup>](#Índice-Rápido)
En Argentina, cada año mueren cerca de 4.000 personas en siniestros viales. Aunque muchas jurisdicciones han logrado disminuir la cantidad de accidentes de tránsito, esta sigue siendo la principal causa de muertes violentas en el país.
Los informes del Sistema Nacional de Información Criminal (SNIC), del Ministerio de Seguridad de la Nación, revelan que entre 2018 y 2022 se registraron 19.630 muertes en siniestros viales en todo el país. Estas cifras equivalen a 11 personas por día que resultaron víctimas fatales por accidentes de tránsito. <br>

# Rol a desarrollar  [<sup> Volver al Índice </sup>](#Índice-Rápido)
El Observatorio de Movilidad y Seguridad Vial (OMSV), centro de estudios que se encuentra bajo la órbita de la ***Secretaría de Transporte*** del Gobierno de la Ciudad Autónoma de Buenos Aires, nos solicita la elaboración de un proyecto de anális de datos, con el fin de generar información que le permita a las autoridades locales tomar medidas para disminuir la cantidad de víctimas fatales de los siniestros viales.
Para ello, nos disponibilizan un dataset sobre homicidios en siniestros viales acaecidos en la Ciudad de Buenos Aires durante el periodo 2016-2021. <br>


# [Datos](https://github.com/jrguignan/Proyecto-Siniestros_Viales-Data_Analyst/tree/main/datasets)  [<sup> Volver al Índice </sup>](#Índice-Rápido)
Se pone a nuestra disposición un par de datasets sobre homicidios en siniestros viales acaecidos en la Ciudad de Buenos Aires durante el período 2016-2021, que se puede encontar en: [Datasets Originales](https://data.buenosaires.gob.ar/dataset/victimas-siniestros-viales)

Para este proyecto se proporcionaron dos archivos XLSX **homicidios** y **lesiones**


* **homicidios** contiene dos hojas llamadas: **HECHOS** y **VICTIMAS** <br>
El archivo posee informacion detallada de tiempo, lugar y datos de los participaentes del suceso. Ambas hojas poseen informacion complementaria entre si.


* **lesiones**  contiene una hoja llamada **VICTIMAS**<br>
Posee informacion similar al archivo anterior. Tiene mas datos, pero le falta mucha información en sus columnas, resultando poco útil.<br>


Para descargar los datasets completos que se utilizaron en este proyecto, se puede descargar también del siguiente link: [Datasets](https://drive.google.com/drive/folders/1SG-1IFA7Uc-iXp_wRLJbg6XDxlSSu3da?usp=sharing) <br>


_Nota_: El dataframe que se creo a partir del archivo lesiones, se le colocó el nombre de **victimas**.


# Tareas Desarrolladas en [Python](https://docs.python.org/es/3/library/index.html)  
## [ETL](https://github.com/jrguignan/Proyecto-Siniestros_Viales-Data_Analyst/blob/main/ETL%20-%20EDA.ipynb) [<sup> Volver al Índice </sup>](#Índice-Rápido)

- Se unieron las dos hojas del archivo homicidios.
- Se crearon los dataframe **df1_homicidios** y **df2_victimas**.
- Se cambió el nombre de algunas columnas.
- Se verificó cada una de las columnas, en busca de valores faltantes o atípicos.
- Se llenó los valores faltantes con SD y se cambió los tipos de datos atípicos.
- Se creó la columna **Nombre dia** , **Categoria tiempo** y **Tipo de dia** , para facilitar el análisis de datos.
- Se optó por eliminar los SD de la columna **Edad**. 
- Se guardaron los dataframe en archivos .csv [**df1_clean**](https://github.com/jrguignan/Proyecto-Siniestros_Viales-Data_Analyst/blob/main/dataframe/df1_clean.csv) y [**df2_clean**](https://github.com/jrguignan/Proyecto-Siniestros_Viales-Data_Analyst/blob/main/dataframe/df2_clean.csv), en el [directorio](https://github.com/jrguignan/Proyecto-Siniestros_Viales-Data_Analyst/tree/main/dataframe).

_Recomendaciones_: De ser posible es mucho mas fácil realizar el ETL en Power BI.

## [EDA](https://github.com/jrguignan/Proyecto-Siniestros_Viales-Data_Analyst/blob/main/ETL%20-%20EDA.ipynb)  [<sup> Volver al Índice </sup>](#Índice-Rápido)

Se procedió a realizar un análisis exploratorio exahustivo (EDA), con la finalidad de encontrar patrones que permitan generar información que le permita a las autoridades locales tomar medidas para disminuir la cantidad de víctimas fatales. dentro de este analisis se destaca:

- La Cantidad de victimas por mes del año.
- La Cantidad de accidentes por horario del día.
- Boxplot de edad.
- Cantidad de victimas por sexo y rol.
- Cantidad de Acusados en los accidentes.
- Catidad de victimas por tipo de calle - cruce.

# Tareas Desarrolladas en [Power BI](https://www.microsoft.com/es-es/power-platform/products/power-bi/)  [<sup> Volver al Índice </sup>](#Índice-Rápido)
## [ETL](https://github.com/jrguignan/Proyecto-Sistema_Recomendaciones-API/blob/main/ETL.ipynb)
- Se verificó  y corrigió los tipos de datos de los dos datasets **df_homicidios**  y **df_Victimas**
- Se reordenaron las columnas
- Se hizo web scraping de [https://es.wikipedia.org/wiki/Buenos_Aires](https://es.wikipedia.org/wiki/Buenos_Aires), para tener la poblacion de Buenos Aires. directo en Power Bi, con la herramienta **Obtener Datos (Web)**


## [Dashboard](https://github.com/jrguignan/Proyecto-Sistema_Recomendaciones-API/blob/main/ETL.ipynb)  [<sup> Volver al Índice </sup>](#Índice-Rápido)
### [Análisis Temporal](https://github.com/jrguignan/Proyecto-Siniestros_Viales-Data_Analyst/blob/main/Siniestros_Viales.pbix)  

Dentro del análisis temporal, se abordo el estudio de la distribucion de los años, meses, dias y franjas horarias de los accidentes.

Dando como resultados mas significativos que el mes de Diciembre es el mas afectado por accidentes, asi como los fines de semana no tienen una variacion significativa, pero si lo tienen las franjas horarias, siendo la mañana la franja horaria con mayor cantidad de accidentes.

![Analisis Temporal](https://github.com/jrguignan/Proyecto-Siniestros_Viales-Data_Analyst/blob/main/images/PBI_porTiempo.jpg)

### [Análisis por Partes Involucradas](https://github.com/jrguignan/Proyecto-Siniestros_Viales-Data_Analyst/blob/main/Siniestros_Viales.pbix)  [<sup> Volver al Índice </sup>](#Índice-Rápido)

En este apartado se logro investigar con exito que los accidentes tienen como victimas principalmente a los conductores de motos y a los peatones, y como principales acusados a los autos y pasajeros de transporte publico. Tambien se puede ver que los hombres tieen mayores probabilidades de tener accidentes, asi como las personas de rango etario de entre 16 y 35 años.

![Analisis de accidente](https://github.com/jrguignan/Proyecto-Siniestros_Viales-Data_Analyst/blob/main/images/PBI_porVictima.jpg)

### [Análisis por ubicacion](https://github.com/jrguignan/Proyecto-Siniestros_Viales-Data_Analyst/blob/main/Siniestros_Viales.pbix)  [<sup> Volver al Índice </sup>](#Índice-Rápido)

Siguiendo con el analisis, podemos verificar que existe una correlacion significativa entre los lugares de los accidentes, siendo mayormente localizados en cruces de avenidas.

![Analisis por ubicacion](https://github.com/jrguignan/Proyecto-Siniestros_Viales-Data_Analyst/blob/main/images/PBI_porUbicacion.jpg)

## [KPIs](https://github.com/jrguignan/Proyecto-Sistema_Recomendaciones-API/blob/main/ETL.ipynb)  [<sup> Volver al Índice </sup>](#Índice-Rápido)

* *Reducir en un 10% la tasa de homicidios en siniestros viales de los últimos seis meses, en CABA, en comparación con la tasa de homicidios en siniestros viales del semestre anterior*

    Las tasas de mortalidad relacionadas con siniestros viales suelen ser un indicador crítico de la seguridad vial en una región. Se define como **Tasa de homicidios en siniestros viales** al número de víctimas fatales en accidentes de tránsito por cada 100,000 habitantes en un área geográfica durante un período de tiempo específico, en este caso se toman 6 meses. Su fórmula es:

    $\text{Tasa de homicidios en siniestros viales} = \frac{\text{Número de homicidios en siniestros viales}}{\text{Población total}}·100,000$

    Como *Población Total* se calculó la población para el año 2021 a partir de los censos poblacionales del año 2010 y 2022.

    En este caso, para el año 2021, la *Tasa de homicidios en siniestros viales* fue de 1.61 lo que significa que, durante los primeros 6 meses del año 2021, hubo aproximadamente 1.61 homicidios en accidentes de tránsito por cada 100,000 habitantes. Ahora, el objetivo planteado es reducir esta tasa para el siguiente semestre de 2021 en un 10%, esto es **1.45**. Cuando se calcula el KPI para este período se obtiene que la *Tasa de homicidios en siniestros viales* fue de **1.32**, lo que significa que para el segundo semestre de 2021 se cumple con el objetivo propuesto.

* *Reducir en un 7% la cantidad de accidentes mortales de motociclistas en el último año, en CABA, respecto al año anterior*

    Como se vio en el análisis exploratorio, el 42% de las víctimas mortales se transportaban en moto al momento del hecho. Por lo que se consideró importante proponer el monitoreo de la cantidad de accidentes mortales en este tipo de conductor. Para ello se define a la **Cantidad de accidentes mortales de motociclistas** como el número absoluto de accidentes fatales en los que estuvieron involucradas víctimas que viajaban en moto en un determinado periodo temporal. La fórmula para medir la evolución de los accidentes mortales con víctimas en moto es:

    $\text{Cantidad de accidentes mortales de motociclistas} = -\frac{\text{Víctimas moto año anterior - Víctimas moto año actual}}{\text{Víctimas moto año anterior}}·100$

    Donde:
    - $\text{Víctimas moto año anterior}$: Número de accidentes mortales con víctimas en moto en el año anterior
    - $\text{Víctimas moto año actual}$: Número de accidentes mortales con víctimas en moto en el año actual 

    Para este caso, se toma como año actual al año 2021 y como año anterior al año 2020. En primer lugar, se calculó la *Cantidad de accidentes mortales de motociclistas* para el año 2020, el cual resultó de -44.18, de esta manera el objetivo a cumplir es de **-41.09** (es decir, la reducción del 7% de la cantidad de accidentes para 2020). El calcular la *Cantidad de accidentes mortales de motociclistas* para el año 2021 resultó de **87.50** lo que significa que aumentó un 64% la cantidad de muertes de conductores de motociclistas respecto del 2021.

* *Reducir en un 10% la tasa de homicidios en las avenidas en el último año, en CABA, respecto al año anterior*

    Como se vio en el análisis exploratorio, el 62% de las víctimas mortales transitaban por avenidas al momento del hecho. Se define a la **Tasa de homicidios en las avenidas** al número de víctimas fatales en accidentes de tránsito en avenidas por cada 100,000 habitantes en un área geográfica durante un período de tiempo específico, en este caso anual. Su fórmula es:

    $\text{Tasa de homicidios en las avenidas} = \frac{\text{Número de accidentes mortales con víctimas ocurridas en avenidas}}{\text{Total de la población}}·100000$

    En primer lugar se calculó la *Tasa de homicidios en las avenidas* para el año 2020, la cual resultó en 1.48. De esta se pudo determinar el objetivo a cumplir al año siguiente, que resultó en **1.33** (es decir, la reducción del 10% de la tasa de homicios respecto del 2020). Finalmente, al calcular la *Tasa de homicidios en las avenidas* para el año 2021, la misma resultó de **1.90**, lo que significa que se superó el objetivo, aumentando la tasa de homicidios en avenidas respecto al año anterior.

![KPIs](https://github.com/jrguignan/Proyecto-Siniestros_Viales-Data_Analyst/blob/main/images/KPIs.jpg)

Se guardaron las medidas usadas en Power BI en el siguiente [archivo](https://github.com/jrguignan/Proyecto-Siniestros_Viales-Data_Analyst/blob/main/Medidas%20KPIs.txt)



# Conclusiones y Recomendaciones  [<sup> Volver al Índice </sup>](#Índice-Rápido)

Entre los años 2016 a 2021 se registraron 618 víctimas fatales en accidentes de tránsito. Aproximadamente el 70% de las víctimas se registraron durante la semana. En cuanto a la franja horaria, alrededor del 12% de los hechos ocurre entre las 6 y las 8 de la mañana, pero durante los fines de semana. Diciembre es el mes que resulta con el máximo de fallecimientos en el período analizado.

Alrededor del 77% de las víctimas fatales fueron de sexo masculino, de los cuales casi el 50% tenía entre 25 y 44 años de edad. En relación al tipo de usuario, el 42% fueron motociclistas. El 62% de los homicidios ocurrió en algún punto de las avenidas de CABA, siendo el 82% de ellos en un cruce de la autopista con alguna otra calle. En ese sentido, el 75% de los hechos ocurrieron en cruces de calles.

Finalmente, para el segundo semestre del año 2021, se cumplió con el objetivo de bajar la tasa de homicidios en siniestros viales, pero no se cumplieron los objetivos de reducir la cantidad de accidentes mortales en motociclistas ni en avenidas para el año 2021 respecto del año 2020.

En función de lo anterior, se hacen las siguientes recomendaciones:

* Realizar campañas puntuales, en avenidas y calles, con enfasis en los cruces.
* Reforzar las campañas de seguridad vial entre los días viernes a lunes, intensificando particularmente en el mes de Diciembre.
* Dirigir las campañas de seguridad hacia el sexo masculino, especialmente en cuanto a conducción de moto y automoviles.
* Hacer campañas para el correcto uso de los medios de transportes y y vias por parte de los peatones.
* Seguir generando y monitoreando la data de los accidentes, para poder hacer un seguimiento de los objetivos.


# Requerimientos  [<sup> Volver al Índice </sup>](#Índice-Rápido)
- [Power BI](https://www.microsoft.com/es-es/power-platform/products/power-bi/)
- [Python](https://docs.python.org/es/3/library/index.html)
- [Pandas](https://pandas.pydata.org/)
- [NumPy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)
- [Seaborn](https://seaborn.pydata.org/)



# Autor  [<sup> Volver al Índice </sup>](#Índice-Rápido)
- José R. Guignan
- Mail: joserguignan@gmail.com
- Linkedin: [https://www.linkedin.com/in/jrguignan](https://www.linkedin.com/in/jrguignan)

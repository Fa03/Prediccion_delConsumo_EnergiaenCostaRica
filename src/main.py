"""IMPORTACION DE LIBRERIAS"""

from src.helpers.verificacionLibrerias import libreriasinstaladas

# Uso de la clase libreriasinstaladas
verificar_librerias = libreriasinstaladas(['importlib.util','subprocess','sys','pandas','matplotlib','seaborn','sqlalchemy','pyodbc',
                                           'urllib'])
verificar_librerias.instalar_librerias()

from src.datos.datos import unionArchivos
from src.eda.exploracion_archivos import EDA_Datos
from src.basedatos.conexion_basedatos import conexion_basedatos



#Variables para usar clase unionArchivos
ruta = "C:/Users/fab_t/OneDrive/CUC/PrograII/Proyecto5_Predicción_delConsumode_EnergíaenCostaRica/data/raw"
columnas_eliminar = ["Expediente", "Resolución", "Fecha de Publicación", "Pliego"]

# Uso de la clase unionArchivos
obj_union_archivos = unionArchivos(ruta, columnas_eliminar)
df_unido = obj_union_archivos.union()
# print(df_unido) # Código solo para pruebas de ejecución (por eso se comenta)

# Uso de la clase exploración_archivos

obj_eda = EDA_Datos(df_unido)

"""LIMPIEZA DE DATOS"""
obj_eda.valores_nulos()
cols = ['Mes', 'Empresa', 'Tipo Tarifa', 'Descripción Tarifa', 'Bloque']
obj_eda.eliminar_espacios(cols)

""" EJECUTAR ANÁLISIS EDA """
obj_eda.resumen_general()
print("Diccionario de cardinalidades: \n",obj_eda.cardinalidades(cols),"\n") #diccionario de cardinalidades
obj_eda.zscore_outliers()
print("Top 5 de tarifas por Descripción Tarifa",obj_eda.top_tarifas_por('Descripción Tarifa'),"\n")

"""VISUALIZACIÓN DE DATOS EDA"""
obj_eda.distribucion_tarifas() #gráfico de barras
obj_eda.correlaciones_numericas() #gráfico de calor
obj_eda.tarifas_por_bloque() # gráfico de barras
obj_eda.plot_box_tarifa() #gráfico de boxplot

"""  CONEXIÓN A LA BASE DE DATOS Y CARGA DE DATOS"""

# Parámetros de conexión a la base de datos SQL Server
driver = 'ODBC Driver 17 for SQL Server'
server = 'AZUSFA\\FA_LOCALSERVER'
database = 'Consumo_Energia_JASEC'
username = 'RemoteUser'
password = 'Intento900@'

obj_connect_bd = conexion_basedatos(driver, server, database, username, password)
obj_connect_bd.conectar()

nombre_tabla = "Datos_JASEC"

# Verificacion de existeencia, creación y llenado de tabla en SQL Server
# obj_connect_bd.insertar_dataframe(obj_eda.df, nombre_tabla) # ### COMENTADO PARA EVITAR DUPLOCAR DATOS EN LA TABLA



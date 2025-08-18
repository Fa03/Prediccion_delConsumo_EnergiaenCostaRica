"""IMPORTACION DE LIBRERIAS"""

from src.helpers.verificacionLibrerias import libreriasinstaladas

# Uso de la clase libreriasinstaladas
verificar_librerias = libreriasinstaladas(['importlib.util','subprocess','sys','pandas','matplotlib','seaborn','urllib','sqlalchemy',])
verificar_librerias.instalar_librerias()

from src.datos.datos import unionArchivos
from src.eda.exploracion_archivos import EDA_Datos

#Variables para usar clase unionArchivos
ruta = "C:/Users/fab_t/OneDrive/CUC/PrograII/Proyecto5_Predicción_delConsumode_EnergíaenCostaRica/data/raw"
columnas_eliminar = ["Expediente", "Resolución", "Fecha de Publicación", "Pliego"]

# Uso de la clase unionArchivos
obj_union_archivos = unionArchivos(ruta, columnas_eliminar)
df_unido = obj_union_archivos.union()
# print(df_unido) # Código solo para pruebas de ejecución (por eso se comenta)

"""Visualización de datos EDA"""

# Uso de la clase exploración_archivos

obj_eda = EDA_Datos(df_unido)

# Ejecutar análisis
obj_eda.resumen_general()
obj_eda.valores_nulos()
obj_eda.distribucion_tarifas()
obj_eda.correlaciones_numericas()
obj_eda.tarifas_por_bloque()




from datos import *
from helpers import *
from src.datos.datos import unionArchivos
from src.helpers.verificacionLibrerias import libreriasinstaladas

# Uso de la clase libreriasinstaladas
verificar_librerias = libreriasinstaladas(['importlib.util','subprocess','sys','pandas'])
verificar_librerias.instalar_librerias()

#Variables para usar clase unionArchivos
ruta = "C:/Users/fab_t/OneDrive/CUC/PrograII/Proyecto5_Predicción_delConsumode_EnergíaenCostaRica/data/raw"
columnas_eliminar = ["Expediente", "Resolución", "Fecha de Publicación", "Pliego"]

# Uso de la clase unionArchivos
obj_union_archivos = unionArchivos(ruta, columnas_eliminar)
df_unido = obj_union_archivos.union()
# print(df_unido) # Código solo para pruebas de ejecución (por eso se comenta)




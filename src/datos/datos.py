import pandas as pd
import os

# Ruta de los archivos Excel
carpeta = "C:/Users/fab_t/OneDrive/CUC/PrograII/Proyecto5_Predicción_delConsumode_EnergíaenCostaRica/data/raw"
archivos = [f for f in os.listdir(carpeta) if f.endswith(".xlsx")]

# Eliminar columnas sin valores
columnas_a_eliminar = ["Expediente", "Resolución", "Fecha de Publicación", "Pliego"]

# DataFrames columnas eliminadas
dataframes_limpios = []

# Iterar sobre cada archivo
for archivo in archivos:
    ruta_completa = os.path.join(carpeta, archivo)

    # Leer el archivo
    df = pd.read_excel(ruta_completa)

    # Eliminar columnas seleccionadas
    columnas_presentes = [col for col in columnas_a_eliminar if col in df.columns]
    df_limpio = df.drop(columns=columnas_presentes)

    # Agregar al listado
    dataframes_limpios.append(df_limpio)

# Union de archivos
df_final = pd.concat(dataframes_limpios, ignore_index=True)

# Guardar archivo
df_final.to_excel("datos_unificados.xlsx", index=False)

print("DataFrame final listo con", df_final.shape[0], "filas y", df_final.shape[1], "columnas.")
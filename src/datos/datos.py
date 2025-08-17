import pandas as pd
import os

class unionArchivos:
    def __init__(self, carpeta, columnasEliminar):
        self.carpeta = carpeta
        self.archivos = [f for f in os.listdir(carpeta) if f.endswith(".xlsx")]
        self.columnasEliminar = columnasEliminar

    def union(self):
        # DataFrames columnas eliminadas
        dataframes_limpios = []

        # Iterar sobre cada archivo
        for archivo in self.archivos:
            ruta_completa = os.path.join(self.carpeta, archivo)

            # Leer el archivo
            df = pd.read_excel(ruta_completa)

            # Eliminar columnas seleccionadas
            columnas_presentes = [col for col in self.columnasEliminar if col in df.columns]
            df_limpio = df.drop(columns=columnas_presentes)

            # Agregar al listado
            dataframes_limpios.append(df_limpio)

        # Union de archivos
        df_final = pd.concat(dataframes_limpios, ignore_index=True)

        # Guardar archivo
        df_final.to_excel("C:/Users/fab_t/OneDrive/CUC/PrograII/Proyecto5_Predicción_delConsumode_EnergíaenCostaRica/data/processed/datos_unificados.xlsx", index=False)

        print("DataFrame final listo con", df_final.shape[0], "filas y", df_final.shape[1], "columnas. \n")

        return df_final
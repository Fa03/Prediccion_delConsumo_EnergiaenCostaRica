import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

class EDA_Datos:
    def __init__(self, df_datos):
        self.df = df_datos

    def resumen_general(self):
        """Muestra información básica del DataFrame"""
        try:
            print("\n Primeras 10 filas:")
            print(self.df.head(n=10))
            print("\n Información general:")
            print(self.df.info())
            print("\n Estadísticas descriptivas:")
            print(self.df.describe(include='all'))
        except Exception as e:
            print(f"Error en resumen_general: {e}")

    def valores_nulos(self):
        """Revisa valores nulos por columna"""
        try:
            print("\n Valores nulos por columna:")
            print(self.df.isnull().sum(),"\n")
        except Exception as e:
            print(f"Error en valores_nulos: {e}")

    def distribucion_tarifas(self):
        """Visualiza la distribución de tarifas"""
        try:
            plt.figure(figsize=(10, 6))
            sns.histplot(self.df['Tarifa'], bins=30, kde=True, color='skyblue')
            plt.title("Distribución de las Tarifas")
            plt.xlabel("Tarifa")
            plt.ylabel("Frecuencia")
            plt.grid(True)
            plt.show()
        except KeyError:
            print("La columna 'Tarifa' no existe en el DataFrame.")
        except Exception as e:
            print(f"Error en distribucion_tarifas: {e}")

    def correlaciones_numericas(self):
        """Muestra mapa de calor de correlaciones numéricas"""
        try:
            numeric_df = self.df.select_dtypes(include='number')
            if numeric_df.empty:
                raise ValueError("No hay columnas numéricas para correlacionar.")
            corr = numeric_df.corr()
            plt.figure(figsize=(8, 6))
            sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
            plt.title("Mapa de Correlaciones")
            plt.show()
        except Exception as e:
            print(f"Error en correlaciones_numericas: {e}")

    def tarifas_por_bloque(self):
        """Gráfico de barras de tarifas promedio por bloque"""
        try:
            bloque_tarifa = self.df.groupby('Bloque')['Tarifa'].mean().sort_values()
            plt.figure(figsize=(10, 5))
            bloque_tarifa.plot(kind='bar', color='coral')
            plt.title("Tarifa Promedio por Bloque")
            plt.ylabel("Tarifa Promedio")
            plt.xlabel("Bloque")
            plt.grid(True)
            plt.show()
        except KeyError as e:
            print(f"Faltan columnas necesarias ('Bloque' o 'Tarifa'): {e}")
        except Exception as e:
            print(f"Error en tarifas_por_bloque: {e}")

    # ++++++++++++++  Nuevo +++++++++++

    def eliminar_espacios(self, cols):
        """Elimina espacios en blanco de las columnas de texto"""
        for col in cols:
            if col in self.df.columns:
                self.df[col] = self.df[col].astype(str).str.strip()


    def cardinalidades(self, columnas):
        """Cardinalidad de columnas categóricas clave, la cantidad de valore distintos en una misma columna"""
        resultado = {}
        for col in columnas:
            if col in self.df.columns:
                resultado[col] = self.df[col].nunique(dropna=True)
        return resultado

    def plot_box_tarifa(self, title: str = "Boxplot de Tarifa"):
        """Boxplot global de tarifa."""
        plt.figure()
        plt.boxplot(self.df['Tarifa'].dropna(), vert=True)
        plt.title(title)
        plt.ylabel("Tarifa")
        plt.show()

    def zscore_outliers(self, limite = 3):
        """Marca outliers por z-score en 'Tarifa'. Devuelve df con columnas extra: zscore, es_outlier."""
        serie = self.df['Tarifa'].astype(float)
        mu = np.nanmean(serie)
        sigma = np.nanstd(serie)
        z = (serie - mu) / (sigma if sigma != 0 else np.nan)
        # Nuevo data frame creado con columnas extra
        out = self.df.copy()
        out['zscore_tarifa'] = z
        out['es_outlier'] = np.abs(z) > limite
        print("DataFrame con columnas extra zscore y es_outlier:")
        print(out.head(n=10),"\n")

        conteo_outliers = out['es_outlier'].value_counts()
        print("Conteo de valores en columna 'es_outlier':",conteo_outliers)

        # Crear un nuevo DataFrame con solo las filas True
        df_solo_outliers = out[out['es_outlier'] == True]
        print("\nDataFrame con solo outliers (es_outlier == True):")
        print(df_solo_outliers.head())

        return out

    def top_tarifas_por(self, por, n = 5, mayores = True) -> pd.DataFrame:
        """Top N tarifas (mayores o menores) por categoría."""
        if por not in self.df.columns:
            raise ValueError(f"La columna '{por}' no existe.")
        orden = False if mayores else True
        return (self.df
                .sort_values([por, 'Tarifa'], ascending=[True, orden])
                .groupby(por, as_index=False)
                .head(n))
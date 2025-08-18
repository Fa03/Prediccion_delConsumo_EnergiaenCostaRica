import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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
            print(self.df.isnull().sum())
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
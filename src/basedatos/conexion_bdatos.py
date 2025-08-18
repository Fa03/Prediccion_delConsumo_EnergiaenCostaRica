# import urllib
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy import create_engine, text
#
#
# driver = 'ODBC Driver 17 for SQL Server'
# server = 'AZUSFA\FA_LOCALSERVER'
# database = 'ADCDC_BD'
# username = 'TEST4'
# password = 'ContrasenaSegura123!'
#
# params = urllib.parse.quote_plus(
#     f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'
# )

from sqlalchemy import create_engine, inspect
import pandas as pd

class BaseDatosSQL:
    def __init__(self, conexion_str: str):
        """
        Inicializa la conexión a la base de datos.
        Ejemplo de conexión_str:
        - SQLite: 'sqlite:///mi_base.db'
        - SQL Server: 'mssql+pyodbc://usuario:clave@DSN'
        - PostgreSQL: 'postgresql://usuario:clave@localhost:5432/mi_base'
        """
        try:
            self.engine = create_engine(conexion_str)
            self.inspector = inspect(self.engine)
            print("Conexión establecida correctamente.")
        except Exception as e:
            print(f"Error al conectar con la base de datos: {e}")
            self.engine = None

    def tabla_existe(self, nombre_tabla: str) -> bool:
        """Verifica si la tabla ya existe en la base de datos"""
        try:
            return nombre_tabla in self.inspector.get_table_names()
        except Exception as e:
            print(f"Error al verificar existencia de la tabla: {e}")
            return False

    def insertar_dataframe(self, df: pd.DataFrame, nombre_tabla: str):
        """Inserta el DataFrame en la tabla especificada. Crea la tabla si no existe."""
        if self.engine is None:
            print("No hay conexión activa con la base de datos.")
            return

        try:
            existe = self.tabla_existe(nombre_tabla)
            df.to_sql(nombre_tabla, con=self.engine, if_exists='append' if existe else 'replace', index=False)
            print(f"Datos insertados en la tabla '{nombre_tabla}' ({'append' if existe else 'replace'}).")
        except Exception as e:
            print(f"Error al insertar datos en la tabla '{nombre_tabla}': {e}")
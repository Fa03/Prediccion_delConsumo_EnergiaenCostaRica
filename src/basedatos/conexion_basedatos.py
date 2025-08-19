
from sqlalchemy import create_engine, text, MetaData, Table, Column, String, Integer, Float, create_engine, inspect, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
import urllib

class conexion_basedatos:
    def __init__(self, driver, server, database, username, password):
        self.driver = driver
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.engine = None
        self.Session = None
        self.session = None


    def conectar(self):
        """Conecta a la base de datos SQL Server"""
        try:
            params = urllib.parse.quote_plus(
                f'DRIVER={self.driver};SERVER={self.server};DATABASE={self.database};UID={self.username};PWD={self.password}'
            )
            connection_string = f"mssql+pyodbc:///?odbc_connect={params}"
            self.engine = create_engine(connection_string, echo=False, future=True)
            self.Session = sessionmaker(bind=self.engine)
            self.session = self.Session()
            print("Conexión establecida con la base de datos.")
        except Exception as e:
            print(f"Error al conectar con SQL Server: {str(e)}")

    def tabla_existe(self, nombre_tabla):
        """Verifica si la tabla ya existe en la base de datos"""
        try:
            inspector = inspect(self.engine)
            return inspector.has_table(table_name=nombre_tabla)
        except Exception as e:
            print(f" Error al verificar existencia de la tabla '{nombre_tabla}' no existe en la BD: {e}")
            return False

    def crear_tabla(self, nombre_tabla, columnas_dict):
        """
        Crea una tabla en la base de datos con los nombres y tipos de columnas especificados.
        columnas_dict debe tener formato: {"col1": String, "col2": Integer, ...}
        """
        if self.engine is None:
            print("No hay conexión activa con la base de datos.")
            return

        try:
            metadata = MetaData()
            columnas = [Column(nombre, tipo) for nombre, tipo in columnas_dict.items()]
            tabla = Table(nombre_tabla, metadata, *columnas)
            metadata.create_all(self.engine)
            print(f"Tabla '{nombre_tabla}' creada exitosamente.\n")
        except Exception as e:
            print(f"Error al crear la tabla '{nombre_tabla}': {e}")

    def insertar_dataframe(self, df, nombre_tabla):
        """Inserta el DataFrame en la tabla especificada. Crea la tabla si no existe."""
        if self.engine is None:
            print("No hay conexión activa con la base de datos.")
            return

        try:
            existe = self.tabla_existe(nombre_tabla)
            if not existe:
                # Inferir tipos básicos desde el DataFrame
                tipo_map = {
                    "object": String,
                    "int64": Integer,
                    "float64": Float,
                    "bool": Integer,
                    "datetime64[ns]": String
                }
                columnas_dict = {
                    col: tipo_map.get(str(df[col].dtype), String)
                    for col in df.columns
                }
                self.crear_tabla(nombre_tabla, columnas_dict)

            df.to_sql(nombre_tabla, con=self.engine, if_exists='append', index=False)
            print(f"Datos insertados en la tabla '{nombre_tabla}'.")
        except Exception as e:
            print(f" Error al insertar datos en la tabla '{nombre_tabla}': {e} \n")

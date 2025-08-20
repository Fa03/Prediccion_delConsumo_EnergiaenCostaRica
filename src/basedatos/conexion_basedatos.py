
from sqlalchemy import create_engine, text, MetaData, Table, Column, String, Integer, Float, create_engine, inspect, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
import urllib
import requests
from sqlalchemy import Column, Integer, Date, String, UniqueConstraint
from sqlalchemy.orm import declarative_base
from src.basedatos import conexion_basedatos
from datetime import date  # Ensure proper date conversion
import os  # Added to read configuration from environment

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
            return self.session, self.engine  # Return session and engine for callers
        except Exception as e:
            print(f"Error al conectar con SQL Server: {str(e)}")
            raise

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

def conectar():
    """
    Función a nivel de módulo para obtener (session, engine).
    Lee la configuración desde variables de entorno si están definidas,
    con valores predeterminados para compatibilidad.
    """
    driver = os.getenv('DB_DRIVER', 'ODBC Driver 17 for SQL Server')
    server = os.getenv('DB_SERVER', 'AZUSFA\\FA_LOCALSERVER')
    database = os.getenv('DB_DATABASE', 'Consumo_Energia_JASEC')
    username = os.getenv('DB_USERNAME', 'RemoteUser')
    password = os.getenv('DB_PASSWORD', 'Intento900@')

    conn = conexion_basedatos(driver, server, database, username, password)
    return conn.conectar()

Base = declarative_base()
class Feriado(Base):
    __tablename__ = 'Feriados'
    id = Column(Integer, primary_key=True, autoincrement=True)
    fecha = Column(Date, unique=True, nullable=False)
    nombre = Column(String(255), nullable=False)
    descripcion = Column(String(500), nullable=True)
    __table_args__ = (UniqueConstraint('fecha', name='uq_feriado_fecha'),)

    def exportar_desde_api(year: int, mes: int = None):
        # Construir URL del API
        url = f"http://localhost:8000/feriados/{year}"
        if mes:
            url += f"?mes={mes}"

        # Obtener datos del API
        response = requests.get(url)
        response.raise_for_status()
        payload = response.json()
        feriados = payload.get("feriados", [])

        # Obtener sesión y engine desde el módulo externo
        session, engine = conexion_basedatos.conectar()

        # Crear tabla si no existe
        Base.metadata.create_all(engine)

        nuevos = 0
        try:
            for f in feriados:
                # Asegurar que 'fecha' sea un date (YYYY-MM-DD esperado)
                try:
                    fecha_val = f.get("fecha")
                    if isinstance(fecha_val, str):
                        fecha_val = date.fromisoformat(fecha_val)
                except Exception as parse_err:
                    # Saltar registros con fecha inválida
                    print(f"Fecha inválida '{f.get('fecha')}', se omite: {parse_err}")
                    continue

                existe = session.query(Feriado).filter_by(fecha=fecha_val).first()
                if not existe:
                    nuevo = Feriado(
                        fecha=fecha_val,
                        nombre=f.get("nombre", ""),
                        descripcion=f.get("descripcion")
                    )
                    session.add(nuevo)
                    nuevos += 1

            session.commit()
            print(f"{nuevos} feriados insertados en la base de datos.")
        except Exception as db_err:
            session.rollback()
            raise
        finally:
            session.close()

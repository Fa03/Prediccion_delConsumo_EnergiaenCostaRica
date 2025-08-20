# exportador_sql.py
import requests
from sqlalchemy import Column, Integer, Date, String, UniqueConstraint
from sqlalchemy.orm import declarative_base
from src.basedatos import conexion_basedatos

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
    feriados = response.json()["feriados"]

    # Obtener sesión y engine desde el módulo externo
    session, engine = conexion_basedatos()

    # Crear tabla si no existe
    Base.metadata.create_all(engine)

    # Insertar evitando duplicados
    nuevos = 0
    for f in feriados:
        existe = session.query(Feriado).filter_by(fecha=f["fecha"]).first()
        if not existe:
            nuevo = Feriado(
                fecha=f["fecha"],
                nombre=f["nombre"],
                descripcion=f["descripcion"]
            )
            session.add(nuevo)
            nuevos += 1

    session.commit()
    session.close()
    print(f"{nuevos} feriados insertados en la base de datos.")

# Ejemplo de uso
# if __name__ == "__main__":
#     exportar_desde_api(year=2025, mes=8)
# feriado_loader.py
from src.api.llamado_api import Feriado


class FeriadoLoader:
    def __init__(self, start_year: int, end_year: int):
        self.start_year = start_year
        self.end_year = end_year

    def cargar_feriados(self):
        for year in range(self.start_year, self.end_year + 1):
            for month in range(1, 13):
                print(f"Cargando feriados del año {year}, mes {month}...")
                self._exportar_feriados(year, month)

    def _exportar_feriados(self, year: int, month: int):
        # Aquí se llama al método real de exportación
        # Se asume que Feriado está importado desde otro módulo
        from feriado import Feriado  # Importación local para evitar dependencias circulares
        Feriado.exportar_desde_api(year=year, mes=month)
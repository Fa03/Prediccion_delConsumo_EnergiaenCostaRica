
# Código para Verificar e Instalar Librerías
# Librerías propias de la clase

import importlib.util
import subprocess
import sys

class libreriasinstaladas:
    def __init__(self, lista_librerias):
        self.lista_librerias = lista_librerias

    def verificar_instalar_libreria(self, nombre_paquete):
        # Verifica si el paquete está instalado
        paquete_instalado = importlib.util.find_spec(nombre_paquete) is not None

        if not paquete_instalado:
            print(f"Instalando {nombre_paquete}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", nombre_paquete])
        else:
            print(f"{nombre_paquete} ya está instalado.")

    # Ciclo recorre lista librerías
    def instalar_librerias(self):
        for libreria in self.lista_librerias:
            self.verificar_instalar_libreria(libreria)


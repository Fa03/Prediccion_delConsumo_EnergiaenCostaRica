import importlib.util
import subprocess
import sys

class libreriasinstaladas:
    def __init__(self, lista_librerias):
        self.lista_librerias = lista_librerias

    def verificar_instalar_libreria(self, nombre_paquete):
        try:
            # Verifica si el paquete está instalado
            paquete_instalado = importlib.util.find_spec(nombre_paquete) is not None

            if not paquete_instalado:
                print(f"Instalando {nombre_paquete}...")
                subprocess.check_call([sys.executable, "-m", "pip", "install", nombre_paquete])
                print(f"{nombre_paquete} instalado correctamente.")
            else:
                print(f"{nombre_paquete} ya está instalado.")
        except subprocess.CalledProcessError as e:
            print(f"Error al instalar {nombre_paquete}: {e}")
        except Exception as e:
            print(f"Error inesperado con {nombre_paquete}: {e}")

    def instalar_librerias(self):
        for libreria in self.lista_librerias:
            try:
                self.verificar_instalar_libreria(libreria)
            except Exception as e:
                print(f"Error al procesar la librería {libreria}: {e}")
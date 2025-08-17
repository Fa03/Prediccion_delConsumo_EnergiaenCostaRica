
# Código para Verificar e Instalar Librerías

import importlib.util
import subprocess
import sys

def verificar_instalar_libreria(nombre_paquete):
    # Verifica si el paquete está instalado
    paquete_instalado = importlib.util.find_spec(nombre_paquete) is not None

    if not paquete_instalado:
        print(f"Instalando {nombre_paquete}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", nombre_paquete])
    else:
        print(f"{nombre_paquete} ya está instalado.")

# Ejemplo de uso:
verificar_instalar_libreria("math")  # 'math' es parte de la librería estándar, no requiere instalación
verificar_instalar_libreria("numpy")  # Verifica e instala 'numpy' si es necesario

# Importación segura después de verificar
import math
import numpy as np

print("¡Librerías listas para usarse!")


# Explicación del Código
# 1. Usa importlib.util.find_spec() para verificar si la librería está instalada.
# 2. Si no está instalada, usa subprocess.check_call() para ejecutar pip install automáticamente.
# 3. Luego importa la librería de manera segura.
#📌 Nota: La librería math es parte del núcleo de Python, por lo que no necesita instalación, pero este código funciona para librerías externas.
# Déjame saber si quieres ajustar algo. ¡Me encanta apoyar tu eficiencia en Python! 🚀

# 🔌 Análisis del Consumo Eléctrico en Cartago — JASEC⚡

Este proyecto presenta un estudio del consumo de electricidad en la provincia de Cartago, Costa Rica, utilizando datos disponibles en la página de AREEP. Se emplearon herramientas de análisis de datos en Python para explorar, limpiar y visualizar la información, con el objetivo de entender patrones de consumo y facilitar la toma de decisiones informadas.

---

## 📊 Objetivos del Proyecto

- Conectar a una base de datos SQL Server que contiene registros históricos de consumo eléctrico.
- Realizar un análisis exploratorio de datos (EDA) para identificar tendencias, anomalías y estacionalidad.
- Limpiar y transformar los datos para su análisis y visualización.
- Utilizar una API externa para enriquecer los datos con información de fechas (feriados, días especiales).
- Integrar los datos obtenidos vía API en la base de datos SQL Server.
- Presentar los resultados en un Jupyter Notebook con visualizaciones interactivas.

---

## 🧑🏻‍💻 Tecnologías Utilizadas

| Herramienta     | Propósito                                      |
|-----------------|------------------------------------------------|
| Python          | Lenguaje principal para análisis y conexión    |
| SQL Server      | Almacenamiento de datos                        |
| SQLAlchemy      | ORM para conexión y manipulación de datos      |
| Pandas          | Limpieza y transformación de datos             |
| Matplotlib / Seaborn | Visualización de datos                    |
| FastAPI         | Consumo de API externa                         |
| PyODBC          | Conexión directa a SQL Server                  |
| Jupyter Notebook| Presentación de resultados                     |

---

## 🏗️ Estructura del Proyecto

📁 jasec-cartago-electricity/  
├── src/  
│  ├── datos/  
│  ├── basedatos/  
│  ├──api/  
│  ├── eda/  
│  ├── visualizaciones/  
│  ├── modelos/  
│  ├── helpers/  
│  └── main.py  
│  
├── notebooks/  
│  └── exploracion_inicial.ipynb  
│  
├── data/  
│    └── raw  
│    └── processed  
└── 

---

---

## ⬇️ Uso de API

Se creo un API para obtener información sobre días feriados desde la libreria **Holidays** que podrían influir en el consumo eléctrico. Estos datos fueron integrados a la base de datos SQL Server para su análisis conjunto.

---

## 📈 Resultados

El notebook principal (`exploracion_inicial.ipynb`) incluye:

- Valores nulos.
- Primeras 10 filas del dataframe.
- Información general del dataframe.
- Estadísticas descriptivas.
- Outliers.
- Gráficos.
  
---

 **Contacto**  
¿Te interesa colaborar o extender este análisis?  
Podés escribir a [303650023@cuc.cr] o abrir un issue en este repositorio.  

---

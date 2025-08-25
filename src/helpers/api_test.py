#
#
# import requests
#
# # Endpoint JSON
# url_json = "http://localhost:8000/feriados/2025?mes=8"
#
# def fetch_json(url: str):
#     try:
#         resp = requests.get(url, timeout=10)
#         resp.raise_for_status()
#     except requests.RequestException as e:
#         print(f"Error al llamar {url}: {e}")
#         return None
#     try:
#         return resp.json()
#     except ValueError:
#         # No fue JSON (por ejemplo HTML o texto)
#         print(f"La respuesta no es JSON. Content-Type: {resp.headers.get('Content-Type')}")
#         print("Cuerpo (primeros 500 chars):")
#         print(resp.text[:500])
#         return None
#
# data = fetch_json(url_json)
#
# if data is None:
#     # Ya se imprimió un mensaje descriptivo
#     raise SystemExit(1)
#
# if not isinstance(data, dict) or "feriados" not in data or not isinstance(data["feriados"], list):
#     print("La respuesta no contiene la clave 'feriados' con el formato esperado.")
#     print("Respuesta recibida:")
#     print(data)
#     raise SystemExit(1)
#
# for f in data["feriados"]:
#     # Manejar faltantes defensivamente
#     print(f.get("descripcion", f))
#
# # Endpoint HTML
# url_html = "http://localhost:8000/feriados/html/2025?mes=8"
# try:
#     html_resp = requests.get(url_html, timeout=10)
#     html_resp.raise_for_status()
#     html = html_resp.text
# except requests.RequestException as e:
#     print(f"Error al obtener HTML desde {url_html}: {e}")
#     raise SystemExit(1)
#
# print(html)


import requests

# Endpoint JSON
url_json = "http://localhost:8000/feriados/2025?mes=9"
response = requests.get(url_json)
data = response.json()

for f in data["feriados"]:
    print(f["descripcion"])

# Endpoint HTML
url_html = "http://localhost:8000/feriados/html/2025?mes=8"
html = requests.get(url_html).text
print(html)
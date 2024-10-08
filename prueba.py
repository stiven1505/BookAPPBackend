import requests

url = 'https://bookappbackend-31ic.onrender.com/run-migrations/'  # Cambia esto según sea necesario
response = requests.post(url)

# Verifica el estado de la respuesta
print(f"Status Code: {response.status_code}")
print(f"Response Text: {response.text}")  # Imprimir el texto de la respuesta

if response.status_code == 200:
    try:
        print(response.json())
    except ValueError:
        print("La respuesta no es un JSON válido.")
else:
    print("Error en la solicitud:", response.status_code, response.text)

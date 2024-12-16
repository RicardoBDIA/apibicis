import time
import requests
from pymongo import MongoClient

# Configuración
API_URL = "https://api.citybik.es/v2/networks/bicicorunha"
MONGO_URI = "mongodb://localhost:27017/"
DATABASE_NAME = "citybikes"
COLLECTION_NAME = "stations"
INTERVAL_SECONDS = 300  # Intervalo de 5 minutos

# Conexión a MongoDB
client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

def fetch_and_store_data():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()

        # Verificar si se obtuvieron estaciones
        stations = data.get("network", {}).get("stations", [])
        if not stations:
            print("No se encontraron datos de estaciones.")
            return

        # Agregar timestamp global a cada registro
        for station in stations:
            station["global_timestamp"] = time.time()

        # Insertar los datos en MongoDB
        collection.insert_many(stations)
        print(f"Se insertaron {len(stations)} registros en la base de datos.")
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con la API: {e}")
    except Exception as e:
        print(f"Error al insertar datos en MongoDB: {e}")

if __name__ == "__main__":
    print("Iniciando la recolección de datos...")
    try:
        while True:
            fetch_and_store_data()
            time.sleep(INTERVAL_SECONDS)
    except KeyboardInterrupt:
        print("Ejecución interrumpida por el usuario.")
    finally:
        client.close()

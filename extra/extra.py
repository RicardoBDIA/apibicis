import time
import requests
from pymongo import MongoClient
import pymongo

# Configuración
API_URL = "https://api.chucknorris.io/jokes/random"
MONGO_URI = "mongodb://localhost:27017/"
DATABASE_NAME = "chuck_norris_db"
COLLECTION_NAME = "jokes"
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

        # Extraemos los campos que queremos almacenar
        joke = {
            "icon_url": data.get("icon_url"),
            "id": data.get("id"),
            "url": data.get("url"),
            "value": data.get("value")
        }
        print(joke)
        # Insertar los datos en MongoDB
        collection.insert_one(joke)
        print(f"Se insertaron {len(joke)} registros en la base de datos.")
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con la API: {e}")
    except pymongo.errors.PyMongoError as e:
        print(f"Error al insertar datos en MongoDB: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")


print("Iniciando la recolección de datos...")
try:
    while True:
        fetch_and_store_data()
        time.sleep(INTERVAL_SECONDS)
except KeyboardInterrupt:
    print("Ejecución interrumpida por el usuario.")
finally:
    client.close()
import pandas as pd
from pymongo import MongoClient

def export_data():
    try:
        # Conexión a MongoDB
        client = MongoClient('mongodb://localhost:27017/')
        db = client['citybikes']
        collection = db['stations']

        # Leer los datos de MongoDB
        data = list(collection.find({}))
        df = pd.DataFrame(data)

        # Convertir la columna '_id' a tipo string
        if '_id' in df.columns:
            df['_id'] = df['_id'].astype(str)

        # Desanidar el campo "extra"
        if 'extra' in df.columns:
            extra_df = pd.json_normalize(df['extra'])  # Extrae los campos anidados
            df = pd.concat([df, extra_df], axis=1)    # Combina los campos planos con los anidados

        # Seleccionar las columnas necesarias
        columns = [
            'id', 'name', 'timestamp', 'free_bikes', 'empty_slots', 
            'uid', 'last_updated', 'slots', 'normal_bikes', 'ebikes'
        ]
        df = df[columns]

        # Exportar a CSV
        df.to_csv('stations_data.csv', index=False)
        print("Datos exportados correctamente a CSV.")

        # Exportar a Parquet
        df.to_parquet('stations_data.parquet', index=False)
        print("Datos exportados correctamente a Parquet.")

    except Exception as e:
        print(f"Error al exportar los datos: {e}")

if __name__ == "__main__":
    export_data()

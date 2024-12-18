
# **Proyecto: CityBikes Data Collector**

Este proyecto permite recolectar, almacenar y analizar información sobre estaciones de alquiler de bicicletas utilizando la API de [CityBikes](https://citybik.es/).  
Actualmente, el código está configurado para recopilar datos únicamente de la ciudad de A Coruña, España. Está dividido en dos scripts principales, uno para la recolección de datos y otro para la exportación en varios formatos (CSV y Parquet). Además, incluye opciones avanzadas como la dockerización y el despliegue en la nube.

---

## **1. Funcionalidades del proyecto**

### **Parte básica**
1. **Script 1: Recolección de datos**  
   - Se conecta a la API de CityBikes cada 3 minutos para obtener información actualizada de las estaciones.
   - Almacena los datos en una base de datos MongoDB.
   - Funciona de manera continua hasta que se detiene manualmente.

2. **Script 2: Exportación de datos**  
   - Lee los datos almacenados en MongoDB y los carga en un dataframe de Pandas.
   - Exporta los datos en los formatos:
     - CSV (`output.csv`)
     - Parquet (`output.parquet`)
   - Incluye únicamente los campos clave de las estaciones:
     - `id`, `name`, `timestamp`, `free_bikes`, `empty_slots`, `uid`, `last_updated`, `slots`, `normal_bikes`, `ebikes`.

### **Parte avanzada**
1. Dockerización del **script 1**.
2. Configuración de un servidor MongoDB en un contenedor Docker.
3. Publicación de la imagen Docker en Docker Hub.
4. Despliegue del proyecto en la nube (OpenStack).
5. Automatización del despliegue mediante GitHub Actions.

### **Extra**
- Un script adicional que recolecta chistes desde la API de [Chuck Norris Jokes](https://api.chucknorris.io/jokes/random) y los almacena en MongoDB.

---

## **2. Requisitos previos**

### **Software necesario**
1. **Python** (3.8 o superior)
2. **MongoDB** (local o en contenedor Docker)
3. **Docker**

### **Dependencias Python**
Instala las dependencias necesarias desde el archivo `requirements.txt` ejecutando:  
```bash
pip install -r requirements.txt
```

### **Configuración de MongoDB**
#### **Modo local:**
Asegúrate de que MongoDB esté corriendo en `localhost:27017`.  
#### **Modo Docker:**
Si prefieres usar Docker para MongoDB, ejecuta el siguiente comando:  
```bash
docker run -d --name mongodb -p 27017:27017 mongo:6.0
```

---

## **3. Ejecución del proyecto**

### **Script 1: Recolección de datos**
Este script conecta a la API de CityBikes y almacena los datos en MongoDB cada 3 minutos.  

**Ejecución:**
```bash
python script1_citybikes.py
```

**Parámetros configurables:**
- Intervalo de tiempo entre cada recolección (en segundos).
- URI de la base de datos MongoDB (por defecto: `mongodb://localhost:27017`).

**Control de errores:**
- Maneja desconexiones de la API y problemas de escritura en MongoDB.
- Si el script se detiene y reinicia, continúa recopilando datos desde el estado actual.

---

### **Script 2: Exportación de datos**
Este script extrae los datos desde MongoDB y los exporta en los formatos CSV y Parquet.  

**Ejecución:**
```bash
python script2_export.py
```

**Formatos de exportación:**
- `output.csv`
- `output.parquet`

**Campos incluidos en los datos exportados:**
- `id`, `name`, `timestamp`, `free_bikes`, `empty_slots`, `uid`, `last_updated`, `slots`, `normal_bikes`, `ebikes`.

---

### **Extra: Recolección de chistes (Chuck Norris)**
Este script conecta a la API de [Chuck Norris Jokes](https://api.chucknorris.io/jokes/random) y guarda los chistes en MongoDB.  

**Ejecución:**
```bash
python chuck_norris_collector.py
```

---

## **4. Parte avanzada y en otros entornos**

### **Dockerización del Script 1**
Se incluye un archivo `Dockerfile` para ejecutar el script 1 dentro de un contenedor Docker.

**Construcción de la imagen:**
```bash
docker build -t citybikes-collector .
```

**Ejecución del contenedor:**
```bash
docker run -d --name citybikes-app citybikes-collector
```

---

### **Servidor MongoDB en Docker**
Si prefieres usar MongoDB en un contenedor:
```bash
docker run -d --name mongodb -p 27017:27017 mongo:6.0
```

---

### **Publicación en Docker Hub**
1. Inicia sesión en Docker Hub:
   ```bash
   docker login
   ```
2. Publica la imagen:
   ```bash
   docker tag citybikes-collector <tu_usuario>/citybikes-collector
   docker push <tu_usuario>/citybikes-collector
   ```

---

### **Despliegue en OpenStack**
1. Configura una instancia en OpenStack con Docker instalado.
2. Lanza los contenedores de MongoDB y CityBikes desde las imágenes publicadas.

---

### **Automatización desde GitHub**
Configura un archivo `.github/workflows/docker.yml` en tu repositorio para automatizar la construcción y publicación de la imagen en Docker Hub.

---

## **5. Consideraciones finales**

### **Control de errores**
- La aplicación maneja errores de conectividad tanto con la API como con MongoDB.
- Si se reinicia el script, evita duplicar registros.

### **Buenas prácticas**
- Código modular y comentado.
- Manejo de configuraciones mediante variables de entorno (para no incluir datos sensibles en el código).

### **Privacidad**
No se incluyen datos sensibles como contraseñas o claves API en el repositorio.

---

## **6. Estructura del proyecto**
```plaintext
.
├── script1_citybikes.py        # Recolecta datos de la API de CityBikes
├── script2_export.py           # Exporta datos desde MongoDB
├── chuck_norris_collector.py   # Extra opcional: Recolecta chistes de Chuck Norris
├── requirements.txt            # Dependencias de Python
├── Dockerfile                  # Dockerización del Script 1
├── README.md                   # Documentación del proyecto
```

---

## **7. Recursos**
- [CityBikes API](https://citybik.es/)
- [MongoDB Documentation](https://www.mongodb.com/docs/)
- [Docker Documentation](https://docs.docker.com/)
- [Chuck Norris API](https://api.chucknorris.io/)


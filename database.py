import psycopg2
from dotenv import load_dotenv
import os

# Carga las variables del archivo .env
load_dotenv()

def get_connection():
    """
    Crea y retorna una conexión a la base de datos NovaTech.
    Esta función será usada por todos los demás módulos del proyecto.
    """
    connection = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )
    return connection

def test_connection():
    """
    Prueba que la conexión a la base de datos funcione correctamente.
    """
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT version();")
        version = cursor.fetchone()
        print(f"✅ Conexión exitosa a NovaTech DB")
        print(f"📦 PostgreSQL version: {version[0]}")
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"❌ Error de conexión: {e}")

# Ejecuta la prueba cuando corres este archivo directamente
if __name__ == "__main__":
    test_connection()
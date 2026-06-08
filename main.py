from database import get_connection
from copilot import generate_sql

def ask(question):
    """
    Recibe una pregunta en español, genera el SQL y ejecuta en la BD.
    """
    print(f"\n🔍 Pregunta: {question}")
    
    # Paso 1: Generar SQL con IA
    sql = generate_sql(question)
    print(f"📝 SQL generado:\n{sql}")
    
    # Paso 2: Ejecutar SQL en PostgreSQL
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        cursor.close()
        conn.close()
        
        # Paso 3: Mostrar resultados
        print(f"\n✅ Resultado:")
        print(" | ".join(columns))
        print("-" * 50)
        for row in results:
            print(" | ".join(str(val) for val in row))
            
    except Exception as e:
        print(f"❌ Error ejecutando SQL: {e}")

if __name__ == "__main__":
    ask("¿Cuál es el producto más vendido?")
    ask("¿Cuánto ha vendido cada empleado?")
    ask("¿Qué clientes son de Bogotá?")
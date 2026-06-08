from fastapi import FastAPI
from pydantic import BaseModel
from database import get_connection
from copilot import generate_sql

app = FastAPI(
    title="Enterprise Decision Copilot",
    description="API que convierte preguntas en español a SQL y consulta la BD de NovaTech",
    version="1.0.0"
)

class Question(BaseModel):
    question: str

@app.get("/")
def root():
    return {"message": "Enterprise Decision Copilot activo 🚀", "company": "NovaTech Solutions"}

@app.post("/ask")
def ask_question(body: Question):
    """
    Recibe una pregunta en español y retorna el SQL generado y los resultados.
    """
    try:
        # Generar SQL con IA
        sql = generate_sql(body.question)
        
        # Ejecutar en PostgreSQL
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        cursor.close()
        conn.close()
        
        # Formatear resultados
        results = [dict(zip(columns, row)) for row in rows]
        
        return {
            "question": body.question,
            "sql_generated": sql,
            "results": results,
            "total_rows": len(results)
        }
        
    except Exception as e:
        return {"error": str(e), "sql_generated": sql if 'sql' in locals() else None}
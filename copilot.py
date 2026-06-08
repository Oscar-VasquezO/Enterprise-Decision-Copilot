from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Esquema de la base de datos que la IA necesita conocer
DB_SCHEMA = """
Tienes acceso a una base de datos PostgreSQL llamada novatech con las siguientes tablas:

1. categorias(id_categoria, nombre, descripcion)
2. clientes(id_cliente, nombre, email, telefono, ciudad, fecha_registro)
3. empleados(id_empleado, nombre, cargo, email, telefono, ciudad, salario, fecha_ingreso)
4. productos(id_producto, nombre, descripcion, precio, id_categoria)
5. inventario(id_inventario, id_producto, stock, stock_minimo, ultima_actualizacion)
6. ventas(id_venta, id_cliente, id_empleado, fecha_venta, total, estado)
7. detalle_ventas(id_detalle, id_venta, id_producto, cantidad, precio_unitario, subtotal)

Relaciones importantes:
- productos.id_categoria -> categorias.id_categoria
- ventas.id_cliente -> clientes.id_cliente
- ventas.id_empleado -> empleados.id_empleado
- detalle_ventas.id_venta -> ventas.id_venta
- detalle_ventas.id_producto -> productos.id_producto
- inventario.id_producto -> productos.id_producto
"""

def generate_sql(user_question):
    """
    Recibe una pregunta en español y retorna una consulta SQL.
    """
    prompt = f"""
{DB_SCHEMA}

El usuario pregunta: "{user_question}"

Genera SOLO la consulta SQL para responder esa pregunta.
No incluyas explicaciones, no uses markdown, no uses ```.
Solo escribe la consulta SQL pura y nada más.
"""
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "Eres un experto en SQL y bases de datos. Solo respondes con consultas SQL puras, sin explicaciones ni formato markdown."},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    sql_query = response.choices[0].message.content.strip()
    return sql_query


if __name__ == "__main__":
    pregunta = "¿Cuál es el producto más vendido?"
    print(f"Pregunta: {pregunta}")
    sql = generate_sql(pregunta)
    print(f"SQL generado:\n{sql}")
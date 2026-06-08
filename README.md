# Enterprise Decision Copilot
### NovaTech Solutions — Proyecto 1 

Sistema inteligente que permite a cualquier persona consultar una base de datos empresarial usando **lenguaje natural en español**, sin necesidad de saber SQL.

---

## Problema que resuelve

Los gerentes y directivos necesitan datos para tomar decisiones, pero dependen de analistas para obtenerlos. Este sistema elimina esa dependencia — cualquier persona puede hacer preguntas y obtener respuestas en segundos.

## 💡 ¿Cómo funciona?

Usuario escribe una pregunta en español
↓
IA (Groq - LLaMA 3.3) interpreta la intención
↓
Se genera una consulta SQL automáticamente
↓
Se ejecuta en PostgreSQL
↓
Se retorna la respuesta con los datos reales

## 🛠️ Tecnologías

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)

- **Python 3.14** — lenguaje principal
- **FastAPI** — framework para la API REST
- **PostgreSQL** — base de datos empresarial
- **Groq API (LLaMA 3.3)** — modelo de IA para generación de SQL
- **psycopg2** — conector Python-PostgreSQL

##  Estructura del proyecto

Enterprise-Decision-Copilot/
├── api.py          # API REST con FastAPI
├── copilot.py      # Lógica de generación de SQL con IA
├── database.py     # Conexión a PostgreSQL
├── main.py         # Pruebas de consola
├── .env            # Variables de entorno (no incluido)
└── .gitignore      # Archivos ignorados por Git

## 🚀 Ejemplos de uso

**Pregunta:** "¿Cuál fue el empleado que más vendió?"
```json
{
  "question": "¿Cuál fue el empleado que más vendió?",
  "sql_generated": "SELECT e.nombre, SUM(dv.subtotal) AS total_ventas FROM empleados e JOIN ventas v ON e.id_empleado = v.id_empleado JOIN detalle_ventas dv ON v.id_venta = dv.id_venta GROUP BY e.nombre ORDER BY total_ventas DESC LIMIT 1",
  "results": [{"nombre": "Alejandro Mora", "total_ventas": 29780000}]
}
```

## ⚙️ Instalación

```bash
# Clonar el repositorio
git clone https://github.com/Oscar-VasquezO/Enterprise-Decision-Copilot.git

# Instalar dependencias
pip install fastapi uvicorn psycopg2-binary groq python-dotenv

# Configurar variables de entorno
cp .env.example .env
# Editar .env con tus credenciales

# Ejecutar la API
uvicorn api:app --reload
```

## 🌐 Endpoints

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/` | Estado de la API |
| POST | `/ask` | Hacer una pregunta en español |

---

> Proyecto desarrollado como parte del ecosistema **NovaTech Solutions** — un portafolio de 4 proyectos empresariales que combinan bases de datos, automatización e inteligencia artificial.

from flask import Flask
import os
import psycopg2

app = Flask(__name__)

@app.route("/")
def hola():
    return "Hola desde mi contenedor"

@app.route("/db")
def revisar_db():
    conn = psycopg2.connect(
        host=os.environ.get("DB_HOST", "db"),
        dbname="postgres",
        user="postgres",
        password=os.environ.get("DB_PASSWORD", "demo")
    )
    cur = conn.cursor()
    cur.execute("SELECT 1;")
    resultado = cur.fetchone()
    conn.close()
    return f"Conexión a la base de datos OK: {resultado}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
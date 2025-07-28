from flask import Flask
from config import Config
from database import db
from models import Admin  # ← Importa desde __init__.py

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    try:
        admins = Admin.query.all()
        if admins:
            print("✔ Registros encontrados en la tabla 'admin':")
            for admin in admins:
                print(f"ID: {admin.id} - Nombre: {admin.nombre_completo} - Correo: {admin.correo}")
        else:
            print("⚠ La tabla 'admin' está vacía.")
    except Exception as e:
        print("❌ Error al consultar la tabla 'admin':", e)


from flask import Flask
from config import Config
from models import db
from routes.alumno_routes import alumno_bp  # Asegúrate de que existe
from routes.conductor_routes import conductor_bp
from routes.apoderado_routes import apoderado_bp
from routes.colegio_routes import colegio_bp
from routes.asistente_routes import asistente_bp
from routes.auth_routes import auth_bp
from routes.furgon_routes import furgon_bp
from routes.pago_routes import pago_bp 
from routes.notificacion_routes import notificacion_bp
from routes.documentos_routes import documento_bp
from routes.calificacion_routes import calificacion_bp
from routes.contrato_routes import contrato_bp
from routes.solicitud_routes import solicitud_bp


app = Flask(__name__)
app.config.from_object(Config)
app.config['SECRET_KEY'] = 'clave_secreta_segura'
db.init_app(app)

@app.route('/')
def home():
    return "✅ API funcionando correctamente"

# Registrar rutas (Blueprints)
app.register_blueprint(alumno_bp)
app.register_blueprint(conductor_bp)
app.register_blueprint(apoderado_bp)
app.register_blueprint(colegio_bp)
app.register_blueprint(asistente_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(furgon_bp)
app.register_blueprint(pago_bp)
app.register_blueprint(notificacion_bp)
app.register_blueprint(documento_bp)
app.register_blueprint(calificacion_bp) 
app.register_blueprint(contrato_bp)
app.register_blueprint(solicitud_bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
from database import db
import enum
from datetime import date
from datetime import datetime


class Alumno(db.Model):
    __tablename__ = 'alumno'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre_completo = db.Column(db.String(255), nullable=False)
    rut = db.Column(db.String(20), unique=True, nullable=False)
    fecha_nacimiento = db.Column(db.Date, nullable=False)
    horario_entrada = db.Column(db.Time, nullable=False)
    horario_salida = db.Column(db.Time, nullable=False)
    curso = db.Column(db.String(50), nullable=False)
    direccion_hogar = db.Column(db.String(255), nullable=True)
    nombre_contacto_emergencia = db.Column(db.String(255), nullable=True)
    contacto_emergencia = db.Column(db.String(15), nullable=False)
    
    # Relaciones ManyToOne
    colegio_id = db.Column(db.Integer, db.ForeignKey('colegio.id'), nullable=False)
    colegio = db.relationship('Colegio', backref='alumnos_colegio')  # Cambiado el backref
    apoderado_id = db.Column(db.Integer, db.ForeignKey('apoderado.id'), nullable=False)
    sector_id = db.Column(db.Integer, db.ForeignKey('sector.id'), nullable=False)
    sector = db.relationship('Sector', backref='alumnos_sector')  # Cambiado el backref


class Apoderado(db.Model):
    __tablename__ = 'apoderado'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre_completo = db.Column(db.String(255), nullable=False)
    rut = db.Column(db.String(20), unique=True, nullable=False)  # Ejemplo: largo máximo de 20 para el RUT
    correo = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    direccion = db.Column(db.String(255), nullable=False)
    numero_telefono = db.Column(db.String(15), nullable=False)  # Ejemplo: largo máximo de 15 para un número de teléfono
    sexo = db.Column(db.String(10), nullable=True)  # Ejemplo: largo máximo de 10 para 'M'/'F' o 'Masculino'/'Femenino'
    rol = db.Column(db.String(50), nullable=True)  # Ejemplo: largo máximo de 50 para roles como 'Admin', 'User', etc.

    # Relaciones OneToMany
    alumnos = db.relationship('Alumno', backref='apoderado', cascade='all, delete-orphan', lazy=True)
    contratos = db.relationship('Contrato', backref='apoderado', cascade='all, delete-orphan', lazy=True)
    solicitudes = db.relationship('Solicitud', backref='apoderado', cascade='all, delete-orphan', lazy=True)
    # apoderado = db.relationship('Apoderado', backref='alumnos')
    # apoderado = db.relationship('Apoderado', backref='contratos')
    # apoderado = db.relationship('Apoderado', backref='solicitudes')


class Colegio(db.Model):
    __tablename__ = 'colegio'
    
    id = db.Column(db.Integer, primary_key=True)
    rbd = db.Column(db.String(20), nullable=True)  # Ejemplo: largo máximo de 20 para el RBD
    nombre_colegio = db.Column(db.String(255), nullable=True)
    direccion = db.Column(db.String(255), nullable=True)
    contacto = db.Column(db.String(15), nullable=True)  # Ejemplo: largo máximo de 15 para el número de contacto
    
    # Relación ManyToOne con Sector
    sector_id = db.Column(db.Integer, db.ForeignKey('sector.id'), nullable=False)
    sector = db.relationship('Sector', backref='colegios')


class Asistente(db.Model):
    __tablename__ = 'asistente'
    
    id = db.Column(db.Integer, primary_key=True)
    correo = db.Column(db.String(255), nullable=False)
    nombre_completo = db.Column(db.String(255), nullable=False)
    rut = db.Column(db.String(20), unique=True, nullable=False)  # Ejemplo: largo máximo de 20 para el RUT
    sexo = db.Column(db.String(10), nullable=True)  # Ejemplo: largo máximo de 10 para 'M'/'F' o 'Masculino'/'Femenino'
    telefono = db.Column(db.String(15), nullable=False)  # Ejemplo: largo máximo de 15 para el número de teléfono
    
    # Campo LOB (Large Object Binary) para la imagen
    image = db.Column(db.LargeBinary, nullable=True)
    
    # Relación ManyToOne con Conductor
    conductor_id = db.Column(db.Integer, db.ForeignKey('conductor.id'), nullable=False)
    # conductor = db.relationship('Conductor', backref='asistentes')
    
    # Relación OneToOne con Furgon
    furgon_id = db.Column(db.Integer, db.ForeignKey('furgon.id'), unique=True, nullable=True)
    furgon = db.relationship('Furgon', backref=db.backref('asistente', uselist=False))


class Conductor(db.Model):
    __tablename__ = 'conductor'
    id = db.Column(db.Integer, primary_key=True)
    nombre_completo = db.Column(db.String(255), nullable=False)
    rut = db.Column(db.String(20), unique=True, nullable=False)  # Ejemplo: largo máximo de 20 para el RUT
    correo = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    numero_telefono = db.Column(db.String(15), nullable=False)  # Ejemplo: largo máximo de 15 para el número de teléfono
    sexo = db.Column(db.String(10), nullable=True)  # Ejemplo: largo máximo de 10 para 'M'/'F' o 'Masculino'/'Femenino'
    rol = db.Column(db.String(50), nullable=True)  # Ejemplo: largo máximo de 50 para roles como 'Admin', 'User', etc.
    # Campo LOB (Large Object Binary) para la imagen
    image = db.Column(db.LargeBinary, nullable=True)
    asistentes = db.relationship('Asistente', backref='conductor', cascade='all, delete-orphan', lazy=True)


class TipoDocumentoEnum(enum.Enum):
    LICENCIA = "LICENCIA"
    SEGURO = "SEGURO"
    REVISION_TECNICA = "REVISION_TECNICA"

class DocumentoFurgon(db.Model):
    __tablename__ = 'documento_furgon'
    
    id = db.Column(db.Integer, primary_key=True)
    
    # Campo Enum para TipoDocumento
    tipo_documento = db.Column(db.Enum(TipoDocumentoEnum), nullable=False)
    
    # Campo LOB (Large Object Binary) para el archivo
    archivo = db.Column(db.LargeBinary, nullable=False)
    
    # Relación ManyToOne con Furgon
    furgon_id = db.Column(db.Integer, db.ForeignKey('furgon.id'), nullable=False)
    furgon = db.relationship('Furgon', backref='documentos')


class Furgon(db.Model):
    __tablename__ = 'furgon'
    
    id = db.Column(db.Integer, primary_key=True)
    patente = db.Column(db.String(20), unique=True, nullable=False)  # Ejemplo: largo máximo de 20 para la patente
    marca = db.Column(db.String(50), nullable=False)  # Ejemplo: largo máximo de 50 para la marca
    modelo = db.Column(db.String(50), nullable=False)  # Ejemplo: largo máximo de 50 para el modelo
    ano = db.Column(db.Integer, nullable=False)
    capacidad = db.Column(db.Integer, nullable=False)
    cupos_disponibles = db.Column(db.Integer, nullable=False)
    precio_base = db.Column(db.Float, nullable=False)
    validado = db.Column(db.Boolean, nullable=False)
    
    # Relaciones ManyToOne
    conductor_id = db.Column(db.Integer, db.ForeignKey('conductor.id'), nullable=False)
    #conductor = db.relationship('Conductor', backref='furgones')
    
    sector_id = db.Column(db.Integer, db.ForeignKey('sector.id'), nullable=False)
    #sector = db.relationship('Sector', backref='furgones')
    
    colegio_id = db.Column(db.Integer, db.ForeignKey('colegio.id'), nullable=False)
    #colegio = db.relationship('Colegio', backref='furgones')
    
    # Relaciones OneToMany
    contratos = db.relationship('Contrato', backref='furgon', cascade='all, delete-orphan', lazy=True)
    imagenes = db.relationship('ImagenFurgon', backref='furgon', cascade='all, delete-orphan', lazy=True)



class ImagenFurgon(db.Model):
    __tablename__ = 'imagen_furgon'
    
    id = db.Column(db.Integer, primary_key=True)
    
    # Campo LOB (Large Object Binary) para la imagen
    imagen = db.Column(db.LargeBinary, nullable=False)
    
    # Relación ManyToOne con Furgon
    furgon_id = db.Column(db.Integer, db.ForeignKey('furgon.id'), nullable=False)
    #furgon = db.relationship('Furgon', backref='imagenes')




class Calificacion(db.Model):
    __tablename__ = 'calificacion'
    
    id = db.Column(db.Integer, primary_key=True)
    
    # Relación ManyToOne con Apoderado
    apoderado_id = db.Column(db.Integer, db.ForeignKey('apoderado.id'), nullable=False)
    #apoderado = db.relationship('Apoderado', backref='calificaciones')
    
    # Relación ManyToOne con Conductor
    conductor_id = db.Column(db.Integer, db.ForeignKey('conductor.id'), nullable=False)
    #conductor = db.relationship('Conductor', backref='calificaciones')
    
    # Relación OneToOne con Contrato
    contrato_id = db.Column(db.Integer, db.ForeignKey('contrato.id'), nullable=False, unique=True)
    #contrato = db.relationship('Contrato', backref=db.backref('calificacion', uselist=False))
    
    puntuacion = db.Column(db.Integer, nullable=False)  # Puntuación numérica
    comentario = db.Column(db.String(500), nullable=True)  # Comentario con límite de 500 caracteres
    fecha_calificacion = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)  # F


class Contrato(db.Model):
    __tablename__ = 'contrato'
    
    id = db.Column(db.Integer, primary_key=True)
    direccion_establecimiento = db.Column(db.String(255), nullable=False)
    direccion_hogar = db.Column(db.String(255), nullable=False)
    fecha_contratacion = db.Column(db.Date, default=date.today, nullable=False)
    nombre_alumno = db.Column(db.String(255), nullable=False)
    nombre_apoderado = db.Column(db.String(255), nullable=False)
    rut_apoderado = db.Column(db.String(20), nullable=False)  # Ejemplo: largo máximo de 20 para el RUT
    nombre_establecimiento = db.Column(db.String(255), nullable=False)
    periodo = db.Column(db.String(50), nullable=False)  # Ejemplo: largo máximo de 50 para el periodo
    precio = db.Column(db.Float, nullable=False)
    estado = db.Column(db.String(50), nullable=False)  # Ejemplo: largo máximo de 50 para el estado del contrato
    tipo_servicio = db.Column(db.String(50), nullable=False)  # Ejemplo: largo máximo de 50 para el tipo de servicio
    nombre_contacto_emergencia = db.Column(db.String(255), nullable=False)
    numero_contacto_emergencia = db.Column(db.String(15), nullable=False)  # Ejemplo: largo máximo de 15 para el número de contacto

    # Relaciones ManyToOne
    furgon_id = db.Column(db.Integer, db.ForeignKey('furgon.id'), nullable=False)
    #furgon = db.relationship('Furgon', backref='contratos')
    
    conductor_id = db.Column(db.Integer, db.ForeignKey('conductor.id'), nullable=False)
    #conductor = db.relationship('Conductor', backref='contratos')
    
    apoderado_id = db.Column(db.Integer, db.ForeignKey('apoderado.id'), nullable=False)
    
    
    alumno_id = db.Column(db.Integer, db.ForeignKey('alumno.id'), nullable=False)
    #alumno = db.relationship('Alumno', backref='contratos')
    
    colegio_id = db.Column(db.Integer, db.ForeignKey('colegio.id'), nullable=False)
   # colegio = db.relationship('Colegio', backref='contratos')

class Documentos(db.Model):
    __tablename__ = 'documentos'
    
    id = db.Column(db.Integer, primary_key=True)
    
    # Campo LOB (Large Object Binary) para el contenido del documento
    contenido_documento = db.Column(db.LargeBinary, nullable=True)
    
    # Tipo de documento
    tipo_documento = db.Column(db.String(50), nullable=False)  # Ejemplo: largo máximo de 50 para el tipo de documento
    
    # Relación ManyToOne con Conductor
    conductor_id = db.Column(db.Integer, db.ForeignKey('conductor.id'), nullable=True)
    #conductor = db.relationship('Conductor', backref='documentos')
    
    # Relación ManyToOne con Asistente
    asistente_id = db.Column(db.Integer, db.ForeignKey('asistente.id'), nullable=True)
    #asistente = db.relationship('Asistente', backref='documentos')

class Notificacion(db.Model):
    __tablename__ = 'notificacion'
    
    id = db.Column(db.Integer, primary_key=True)
    mensaje = db.Column(db.String(255), nullable=False)
    fecha = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    
    # Relación ManyToOne con Conductor
    conductor_destino_id = db.Column(db.Integer, db.ForeignKey('conductor.id'), nullable=True)
    #conductor_destino = db.relationship('Conductor', backref='notificaciones')
    
    # Relación ManyToOne con Apoderado
    apoderado_destino_id = db.Column(db.Integer, db.ForeignKey('apoderado.id'), nullable=True)
    #apoderado_destino = db.relationship('Apoderado', backref='notificaciones')


class Pago(db.Model):
    __tablename__ = 'pago'
    
    id = db.Column(db.Integer, primary_key=True)
    
    # Relación ManyToOne con Apoderado
    apoderado_id = db.Column(db.Integer, db.ForeignKey('apoderado.id'), nullable=False)
    apoderado = db.relationship('Apoderado', backref='pagos')
    
    # Relación OneToOne con Contrato
    contrato_id = db.Column(db.Integer, db.ForeignKey('contrato.id'), nullable=False, unique=True)
    contrato = db.relationship('Contrato', backref=db.backref('pago', uselist=False))
    
    monto = db.Column(db.Float, nullable=False)
    completado = db.Column(db.Boolean, nullable=False)
    fecha_pago = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    metodo_pago = db.Column(db.String(255), nullable=True)  # Ejemplo: largo máximo de 25

class Solicitud(db.Model):
    __tablename__ = 'solicitud'
    
    id = db.Column(db.Integer, primary_key=True)
    
    # Relaciones ManyToOne
    apoderado_id = db.Column(db.Integer, db.ForeignKey('apoderado.id'), nullable=False)
    
    
    conductor_id = db.Column(db.Integer, db.ForeignKey('conductor.id'), nullable=False)
    #conductor = db.relationship('Conductor', backref='solicitudes')
    
    furgon_id = db.Column(db.Integer, db.ForeignKey('furgon.id'), nullable=False)
    #furgon = db.relationship('Furgon', backref='solicitudes')
    
    # Campos adicionales
    fecha_solicitud = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    fecha_respuesta = db.Column(db.DateTime, nullable=True)
    aceptada = db.Column(db.Boolean, nullable=False, default=False)
    rechazada = db.Column(db.Boolean, nullable=False, default=False)
    vencida = db.Column(db.Boolean, nullable=False, default=False)
    estado = db.Column(db.String(50), nullable=True)  # Ejemplo: largo máxi
    
class Sector(db.Model):
    __tablename__ = 'sector'
    
    id = db.Column(db.Integer, primary_key=True)
    poblacion = db.Column(db.String(255), nullable=True)
    comuna = db.Column(db.String(255), nullable=True)
    
    
class Admin(db.Model):
    __tablename__ = 'admin'

    id = db.Column(db.Integer, primary_key=True)
    nombre_completo = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f'<Admin {self.nombre_completo}>'

    
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date



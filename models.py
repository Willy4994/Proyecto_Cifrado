from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from database import Base
import uuid
from datetime import datetime, timedelta

class Usuario(Base):
    __tablename__ = "usuarios"
    id_usuario = Column(Integer, primary_key=True, index=True)
    nombre_usuario = Column(String, unique=True)
    password_hash = Column(String)
    fecha_registro = Column(DateTime, default=datetime.utcnow)

class RegistroMensaje(Base):
    __tablename__ = "registro_mensajes"
    id_registro = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"))
    etiqueta = Column(String)
    texto_cifrado = Column(String)
    longitud_bits = Column(Integer)
    estado = Column(String, default="ACTIVO") # Para borradoLogico()
    fecha_creacion = Column(DateTime, default=datetime.utcnow)
    fecha_lectura = Column(DateTime, nullable=True)

class Token(Base):
    __tablename__ = "tokens"
    id_token = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    id_registro = Column(String, ForeignKey("registro_mensajes.id_registro"))
    token_string = Column(String, unique=True, index=True)
    fecha_expiracion = Column(DateTime, default=lambda: datetime.utcnow() + timedelta(days=7))
    usado = Column(Boolean, default=False)

class Auditoria(Base):
    __tablename__ = "auditoria"
    id_log = Column(Integer, primary_key=True, index=True)
    id_registro = Column(String, ForeignKey("registro_mensajes.id_registro"), nullable=True)
    fecha_intento = Column(DateTime, default=datetime.utcnow)
    resultado = Column(String)
    ip_visitante = Column(String)
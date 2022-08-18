import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er
from sqlalchemy import Table
Base = declarative_base()

association_table = Table(
    "favoritos",
    Base.metadata,
    Column("usuario_id", ForeignKey("usuario.id")),
    Column("personaje_id", ForeignKey("personaje.id")),
)

class Personaje(Base):
    __tablename__ = 'personaje'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250))
    altura=Column(String(200))
    personalidad=Column(String(300))
    naves = relationship("Naves")
    planetas = relationship("Planetas")
    especies = relationship("Especies")
    usuario = relationship("Usuario", secondary="favoritos")

class Naves(Base):
    __tablename__ = 'naves'
    id = Column(Integer, primary_key=True)
    forma = Column(String(250))
    caracteristicas= Column(String(250))
    color = Column(String(250))
    personaje_que_conduce =  Column(String(250))
    personaje_id = Column(Integer, ForeignKey("personaje.id"))


class Planetas(Base):
    __tablename__ = 'planetas'
    id = Column(Integer, primary_key=True)
    forma = Column(String(250))
    caracteristicas= Column(String(250))
    especies_que_habitan = Column(String(250))
    personaje_id = Column(Integer, ForeignKey("personaje.id"))


class Especies (Base):
    __tablename__ = 'especies'
    id = Column(Integer, primary_key=True)
    genero = Column(String(250))
    caracteristicas= Column(String(250))
    especies_que_habitan = Column(String(250))
    personaje_id = Column(Integer, ForeignKey("personaje.id"))

class Usario (Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250))
    e_mail= Column(String(250))
    nombre_de_usuario = Column(String(250))
    planetas = relationship("Planetas")
    especies = relationship("Especies")
    naves = relationship("Naves")
    personajes = relationship("Personajes", secondary="favoritos")



render_er(Base, 'diagram.png')
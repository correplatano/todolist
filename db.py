from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# creamos el motor que maneja la conexión con la BD, el dialecto, así como evitar errores para conexiones simultáneas generando vario hilos de ejecución
engine = create_engine('sqlite:///database/tareas.db', connect_args={'check_same_thread': False})
# Creamos la sesión, lo que nos permite realizar transacciones (operaciones) dentro de nuestra BD:
Session = sessionmaker(bind=engine)
session = Session()
# se encarga de mapear la clase o clases creadas y vincularlas a la base de datos
Base = declarative_base()

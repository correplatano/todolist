from sqlalchemy import Column, Integer, String, Boolean, Date
import db


class Tarea(db.Base):
    __tablename__ = "tareas"
    id = Column(Integer, primary_key=True)#este es un campo que generará un número único automáticamente cada vez que se cree un objeto nuevo en la BD
    contenido = Column(String(200), nullable=False)#no puede ser un campo null
    hecha = Column(Boolean)
    categoria = Column(String(50))
    fecha = Column(String(50))

    def __init__(self, contenido, hecha, categoria, fecha):
        self.contenido = contenido
        self.hecha = hecha
        self.categoria = categoria
        self.fecha = fecha

    def __str__(self):
        return "Tarea({}: {}, {}, {}, {})".format(self.id, self.contenido, self.hecha, self.categoria, self.fecha)

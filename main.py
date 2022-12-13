from flask import Flask, render_template, request, redirect, url_for, flash
import db
from models import Tarea
import datetime
app = Flask(__name__)  # guardamos el servidor  en una variable
app.secret_key = "loquesea"


@app.route("/")
def home():
    lista_tareas = db.session.query(Tarea).order_by(Tarea.categoria).all() # Hacemos una consulta a la BD para que muestre todos los registros
    return render_template("index.html",
                           lista_tareas=lista_tareas)  # para que pueda mostrar en la página la lista de tareas hay que recepcionar la variable en el index.html


@app.route("/crear-tarea", methods=['POST'])
def crear():
    tarea_nueva = Tarea(contenido=request.form['contenido_tarea'], hecha=False, categoria=request.form['categoria'], fecha=request.form['fecha_limite'])
    db.session.add(tarea_nueva)  # añade el objeto creado a la tabla tarea
    db.session.commit()
    db.session.close()
    flash("Tarea guardada")
    return redirect(url_for("home"))  # le damos el nombre de la funcion definida en python y la ejecuta


@app.route(
    "/tarea-hecha/<id>")  # recibe el parametro de la funcion, en este caso id, y tiene q ir entre <>, para recibir una variable, ya q puede ser cualquier numero
def hecha(id):
    hecha = db.session.query(Tarea).filter_by(id=id).first()  # como solo va a haber un registro le pasamos first()
    hecha.hecha = not (
        hecha.hecha)  # cambiamos de false a true con una negación cuando encuentra la id q le pasamos, de la columna "hecha" de la BD
    if hecha.hecha == False:
        flash("Tarea pendiente")
    db.session.commit()
    db.session.close()
    flash("Tarea hecha")

    return redirect(url_for("home"))


@app.route("/borrar-tarea/<id>")
def borrar(id):
    borrar = db.session.query(Tarea).filter_by(
        id=id).delete()  # si el id de la BD coincide con el parametro q le pasamos, q tb hemos llamado id, lo elimina
    db.session.commit()
    db.session.close()
    flash("Tarea borrada")
    return redirect(url_for("home"))


@app.route("/editar-tarea/<id>")
def editar(id):
    editar_tarea = db.session.query(Tarea).filter_by(id=id).first()
    #db.session.close()
    return render_template("editar-tarea.html", editar_tarea=editar_tarea)


@app.route("/editada/<id>", methods=['POST'])
def tarea_editada(id):
    #editada = db.session.query(Tarea).filter_by(id=id)
    #editada.update = Tarea(contenido=request.form['nuevo_contenido'], hecha=False, categoria=request.form['nueva_categoria'], categoria=request.form['nueva_fecha_limite'])
    #editar_categoria = editada.update({Tarea.contenido: request.form['nuevo_contenido'], Tarea.categoria: request.form['nueva_categoria'], Tarea.fecha: request.form['nueva_fecha_limite']})
    tarea = db.session.query(Tarea).filter_by(id=id).first()
    print(tarea)
    print("CONTENIDO")
    tarea.contenido = request.form['nuevo_contenido']
    print("CATEGORIA")
    tarea.categoria = request.form['nueva_categoria']
    print("FECHA")
    tarea.fecha = request.form['nueva_fecha_limite']
    db.session.commit()
    db.session.close()
    flash("Tarea editada")
    return redirect(url_for("home"))


@app.route("/limite/<id>", methods=['POST'])
def fecha_limite(id):
    limite = db.session.query(Tarea).filter_by(id=id)
    fecha = datetime.date.now()
    if limite == fecha:
        return hecha(id)
    return redirect(url_for("home"))


# Creamos el main e inicializamos nuestra app
if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine)  # Con esta instrucción creamos el modelo de datos
    app.run(debug=True)  # esto hará correr el servidor, además hará que cada vez que se ejecute se reinicie solo.

from flask import Flask, render_template, request, redirect
from config.mysqlconnection import connectToMySQL

app = Flask(__name__)

db = "esquema_estudiantes_cursos"


@app.route("/")
def cursos():
    mysql = connectToMySQL(db)
    lista = mysql.query_db("SELECT * FROM cursos ORDER BY id")
    return render_template("index.html", cursos=lista)


@app.route("/cursos/crear", methods=["POST"])
def crear_curso():
    nombre = request.form["nombre"]
    mysql = connectToMySQL(db)
    mysql.query_db("INSERT INTO cursos (nombre) VALUES (%s)", (nombre,))
    return redirect("/")


@app.route("/cursos/<int:id>")
def ver_curso(id):
    mysql = connectToMySQL(db)
    curso = mysql.query_db("SELECT * FROM cursos WHERE id = %s", (id,))
    if len(curso) == 0:
        return redirect("/")
    mysql = connectToMySQL(db)
    estudiantes = mysql.query_db(
        "SELECT * FROM estudiantes WHERE curso_id = %s ORDER BY id", (id,)
    )
    return render_template("curso.html", curso=curso[0], estudiantes=estudiantes)


@app.route("/estudiantes/nuevo")
def nuevo_estudiante():
    mysql = connectToMySQL(db)
    lista = mysql.query_db("SELECT * FROM cursos ORDER BY id")
    return render_template("nuevo_estudiante.html", cursos=lista)


@app.route("/estudiantes/crear", methods=["POST"])
def crear_estudiante():
    nombre = request.form["nombre"]
    apellido = request.form["apellido"]
    correo = request.form["correo"]
    curso_id = request.form["curso_id"]
    mysql = connectToMySQL(db)
    query = "INSERT INTO estudiantes (nombre, apellido, correo, curso_id) VALUES (%s, %s, %s, %s)"
    mysql.query_db(query, (nombre, apellido, correo, curso_id))
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)

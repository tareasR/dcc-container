from flask import Flask, render_template

app = Flask(__name__)

keys = ["#1", "#2", "#3"]
values = ["Estudiantes", "Profesores", "Secretarias"]
combinacion = list(zip(keys, values))

@app.route('/')
def index():
    return render_template("index.html", variable="hola!", navegacion=combinacion)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
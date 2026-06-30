from flask import Flask, render_template
import yaml

app = Flask(__name__)

def cargar_configuracion():
    with open("configuracion.yaml", "r") as archivo:
        return yaml.safe_load(archivo)

@app.route("/")
def index():
    config = cargar_configuracion()
    return render_template("index.html", titulo_sitio=config["titulo_sitio"], info=config["datos_personales"], content=config["contenido"])

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)

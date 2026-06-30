from flask import Flask, render_template
import requests

app = Flask(__name__)
url = 'https://jsonplaceholder.typicode.com/users'
respuesta = requests.get(url)
print(respuesta.status_code)

if respuesta.status_code == 200:
    datos = respuesta.json()
else:
    print(f"no se puede recuperar: {respuesta.status_code}")

@app.route('/')
def index():
    return render_template("index.html", datos=datos)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
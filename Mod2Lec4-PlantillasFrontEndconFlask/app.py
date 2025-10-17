from flask import Flask, render_template

app = Flask(__name__)


productos = [
    {"nombre": "LaptopGaming", "precio": 1500},
    {"nombre": "TecladoLED", "precio": 75},
    {"nombre": "MouseLED", "precio": 55}
]

usuarios = [
    {"nombre": "Emanuel", "correo": "emanuel@gmail.com"},
    {"nombre": "John", "correo": "john@gmail.com"},
    {"nombre": "Jane", "correo": "jane@gmail.com"}
]

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/productos")
def mostrar_productos():
    return render_template("productos.html", productos=productos)

@app.route("/usuarios")
def mostrar_usuarios():
    return render_template("usuarios.html", usuarios=usuarios)

if __name__ == "__main__":
    app.run(debug=True)

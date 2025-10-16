from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Función para devolver JSON sin escapar caracteres
def jsonify_utf8(data):
    return app.response_class(
        response=json.dumps(data, ensure_ascii=False),
        status=200,
        mimetype='application/json'
    )


@app.route('/info', methods=['GET'])
def info():
    data = {
        "nombre_aplicacion": "Prueba de server",
        "estado": "En desarrollo",
        "descripcion": "Server de practica para probar la arquitectura de Cliente/Servidor y REST APIs"
    }
    return jsonify_utf8(data)


@app.route('/mensaje', methods=['POST'])
def mensaje():
    contenido = request.get_json()
    nombre = contenido.get("nombre", "Usuario") if contenido else "Usuario"
    mensaje = f"¡Hola {nombre}! Tu mensaje fue recibido correctamente."

    respuesta = {
        "respuesta": mensaje,
        "estado": "La prueba se realizo correctamente"
    }
    return jsonify_utf8(respuesta)


if __name__ == '__main__':
    app.run(debug=True)

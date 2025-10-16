from flask import Flask, request
import json

app = Flask(__name__)

def jsonify_utf8(data, status=200):
    return app.response_class(
        response=json.dumps(data, ensure_ascii=False, indent=4),
        status=status,
        mimetype='application/json'
    )


usuarios = []


@app.route('/info', methods=['GET'])
def info():
    data = {
        "nombre_sistema": "Gestor de Usuarios JSON",
        "estado": "Esto es un server en desarrollo",
        "autor": "Emanuel",
        "descripción": "API de prueba con el proposito de manejar usuarios en Flask con JSON"
    }
    return jsonify_utf8(data, 200)


@app.route('/crear_usuario', methods=['POST'])
def crear_usuario():
    try:
        datos = request.get_json()

        
        if not datos or 'nombre' not in datos or 'correo' not in datos:
            return jsonify_utf8({"error": "Faltan campos: 'nombre' y 'correo' son obligatorios"}, 400)

    
        nuevo_usuario = {
            "id": len(usuarios) + 1,
            "nombre": datos['nombre'],
            "correo": datos['correo']
        }

        usuarios.append(nuevo_usuario)

        return jsonify_utf8({
            "mensaje": "Usuario creado exitosamente",
            "usuario": nuevo_usuario
        }, 201)

    except Exception as e:
        return jsonify_utf8({"error": f"Ocurrió un error: {str(e)}"}, 500)



@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    return jsonify_utf8({
        "cantidad": len(usuarios),
        "usuarios": usuarios
    }, 200)


if __name__ == '__main__':
    app.run(debug=True)

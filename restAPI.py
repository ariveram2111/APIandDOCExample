"""API REST - Práctica modulo 3 - Asignatura Gestión de Proyectos

Este script permite la ejecución de una API REST sencilla
desarrollada en la asignatura de Gestión de Proyectos y
Factorías Software. 

Se trata de una API REST con métodos de ejemplo que permiten calcular
y mostrar ejemplos sencillos.

Para ejecutar este script se requieren las librerías de `Flask` y `werkzeug`
que tienen que estar instaladas en el entorno de Python donde se ejecute 
este script.

Este fichero también puede importarse como un módulo. Para ello, es necesario
importar su función principal:

    * main - ejecuta la API REST con Flask
"""

from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException
import time

app = Flask(__name__)

users = {
    '0': 'user0',
    '1': 'user1',
    '2': 'user2',
    '3': 'user3',
    '4': 'user4',
    '5': 'user5',
    '6': 'user6',
    '7': 'user7',
    '8': 'user8',
    '9': 'user9',
    '10': 'user10',
}

def get_timeStamp():
    """Obtiene el timestamp actual en milisegundos

    Returns:
        int: timestamp en milisegundos
    """

    # Se retorna el timestamp actual en milisegundos
    return int(round(time.time() * 1000))

@app.route('/options/', methods = ['GET'])
def options():
    """Endpoint expuesto en la API REST que retorna los métodos y errores más 
    comunes de una API REST

    Returns:
        class 'flask.wrappers.Response': respuesta HTTP que contiene un timestamp
        los métodos y errores más comunes (en formato JSON)
    """
     
    options = {
        # Principales métodos HTTP de una API REST y sus errores más comunes
        'data': {
            'get': 'return the information',
            'post': 'create a new resource',
            'put': 'modify/update the information',
            'delete': 'delete some information',
            'errors': [400, 404, 405, 500]
        },
        # Timestamp actual en milisegundos
        'timestamp': get_timeStamp()
    }

    return jsonify(options)

@app.route('/sayhello/', methods = ['GET'])
def say_hello():
    """Endpoint expuesto en la API REST que retorna un saludo al usuario

    Returns:
        class 'flask.wrappers.Response': respuesta HTTP que contiene un
        timestamp y el saludo (en formato JSON)
    """

    data = {
        # Mensaje para saludar al usuario
        'data': 'hola',
        # Timestamp actual en milisegundos
        'timestamp': get_timeStamp()
    }

    return jsonify(data)

@app.route('/calculate/<num>', methods = ['GET'])
def calculate(num):
    """Endpoint expuesto en la API REST que recibe un número, calcula su 
    cuadrado y lo retorna

    Args:
        num (str): número a elevar al cuadrado

    Returns:
        class 'flask.wrappers.Response': respuesta HTTP que contiene un
        timestamp y el número elevado al cuadrado (en formato JSON)
    """

    try:
        # Se calcula el cuadrado del número pasado en la URL
        squared_number = int(num) ** 2
        data = {
            # Cuadrado del número pasado en la URL
            'data': squared_number,
            # Timestamp actual en milisegundos
            'timestamp': get_timeStamp()
        }
    except:
        # En caso de que no sea un número, se devuelve el siguiente error
        return jsonify({
            'message': 'The input (passed in the URL) has not a good format. It must be a number'
        }), 400

    return jsonify(data)

@app.route('/calculate/', methods = ['GET'])
def calculate2():
    """Endpoint expuesto en la API REST que recibe un número por parámetro, 
    calcula su cuadrado y lo retorna

    Returns:
        class 'flask.wrappers.Response': respuesta HTTP que contiene un
        timestamp y el número elevado al cuadrado (en formato JSON)
    """

    # Se obtiene el parámetro <num>
    num = request.args.get(key='num', default='[no_param]')
    # En caso de no haber introducido el parámetro <num>, se retorna el siguiente error
    if (num == '[no_param]'):
        return jsonify({
            'message': 'It is mandatory to introduce the parameter <num>.'
        }), 400

    try:
        # Se obtiene el cuadrado del número pasado por parámetro
        squared_number = int(num) ** 2
        data = {
            # Cuadrado del número pasado por parámetro
            'data': squared_number,
            # Timestamp actual en milisegundos
            'timestamp': get_timeStamp()
        }
    except:
        # En caso de que el parámetro no sea un número, se devuelve el siguiente error
        return jsonify({
            'message': 'The input (the parameter num) has not a good format. It must be a number'
        }), 400
    
    return jsonify(data)

@app.route('/concatenate/', methods = ['GET'])
def concatenate():
    """Endpoint expuesto en la API REST que recibe dos cadenas por parámetro, 
    las concatena y retorna el resultado

    Returns:
        class 'flask.wrappers.Response': respuesta HTTP que contiene un 
        timestamp y la concatenación de las dos cadenas recibidas (en formato JSON)
    """

    # Se obtienen los parámetros <cad1> y <cad2>
    cad1 = request.args.get(key='cad1', default='[no_param]')
    cad2 = request.args.get(key='cad2', default='[no_param]')
    # En caso de no haber introducido alguno de los parámetros anteriores, se retorna el siguiente error
    if (cad1 == '[no_param]') or (cad2 == '[no_param]'):
        return jsonify({
            'message': 'It is mandatory to introduce the parameters <cad1> and <cad2>.'
        }), 400
    # Se concatenan las dos cadenas recibidas
    concatenation = cad1 + cad2
    data = {
        # Concatenación de las cadenas recibidas
        'data': concatenation,
        # Timestamp actual en milisegundos
        'timestamp': get_timeStamp()
    }
    return jsonify(data)

@app.route('/users/<id>', methods = ['GET'])
def usersM(id):
    """Endpoint expuesto en la API REST que recibe un ID de usuario y retorna el 
    nombre de usuario asociado a este ID

    Args:
        id (str): ID del usuario del cual se quiere obtener su nombre de usuario

    Returns:
        class 'flask.wrappers.Response': respuesta HTTP que contiene un timestamp 
        y el nombre del usuario (en formato JSON)
    """

    try:
        # Se obtiene el nombre de usuario a partir de su ID
        user = users[id]
        data = {
            # Nombre del usuario asociado al ID recibido
            'data': user,
            # Timestamp actual en milisegundos
            'timestamp': get_timeStamp()
        }
    except:
        # En caso de no existir el ID recibido, se devuelve el siguiente error
        return jsonify({
            'message': 'The user ID passed in the URL doesnt exist'
        }), 404
    
    return jsonify(data)

@app.errorhandler(Exception)
def handle_error(e):
    """Método de la API REST que gestiona los errores que se producen

    Args:
        e (class Exception): excepción producida y que se tiene que gestionar

    Returns:
        class 'flask.wrappers.Response': respuesta que contiene la 
        descripción de la excepción
    """

    code = 500
    description = str(e)
    if isinstance(e, HTTPException):
        # Se obtiene el código HTTP de la excepción de tipo HTTPException
        code = e.code
        # Se obtiene la descripción de la excepción de tipo HTTPException
        description = e.description
    data = {
        'message': str(description)
    }
    return jsonify(data), code

def main():
    """Inicia la ejecución de la API REST creada con Flask
    """

    app.run(host='127.0.0.1', port=5000)

if __name__ == '__main__':
    main()


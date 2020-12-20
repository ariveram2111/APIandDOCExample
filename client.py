"""Cliente de la API REST - Práctica modulo 3 - Gestión de Proyectos

Este script permite consumir la API REST creada para la actividad 
del módulo 3 de la asignatura de Gestión de Proyectos y Factorías 
Software.

Se trata de un cliente que prueba todos los endpoints declarados en la
API REST.

Este fichero también puede importarse como un módulo. Contiene las
siguientes funciones:

    * print_client_method - imprime por pantalla la respuesta de la
    petición que se realizará con el método HTTP y URL pasada por 
    argumentos
    * main - ejecuta la función anterior para varias peticiones que
    prueban la API REST
"""

import requests
import time

requests_list = [('GET', 'http://localhost:5000/options/'), 
    ('GET','http://localhost:5000/sayhello/'),
    ('GET','http://localhost:5000/calculate/10'),
    ('GET','http://localhost:5000/calculate/a'),
    ('GET','http://localhost:5000/calculate/?num=10'),
    ('GET','http://localhost:5000/calculate/?num=a'),
    ('GET','http://localhost:5000/calculate/'),
    ('GET','http://localhost:5000/concatenate/?cad1=Hello&cad2=World'),
    ('GET','http://localhost:5000/concatenate/'),
    ('GET','http://localhost:5000/users/4'),
    ('GET','http://localhost:5000/users/a'),
    ('GET','http://localhost:5000/users/100'),
    ('GET','http://localhost:5000/test/'),
    ('POST','http://localhost:5000/users/4')]

def print_client_method(http_method, url):
    """Realiza una petición con el método HTTP y la URL pasadas por 
    argumento e imprime por pantalla el código y cuerpo de la respuesta

    Args:
        http_method (str): Método HTTP para realizar la petición. 
        Posibles valores: GET, POST, PUT, PATCH y DELETE
        url (str): URL a la que se va a realizar la petición.
    """

    print("[+] ", http_method, " REQUEST --> ", url)
    # Se realiza la petición con el método especificado a la URL especificada
    if (http_method == 'GET'):
        result = requests.get(url)
    elif (http_method == 'POST'):
        result = requests.post(url)
    elif (http_method == 'PUT'):
        result = requests.put(url)
    elif (http_method == 'PATCH'):
        result = requests.patch(url)
    elif (http_method == 'DELETE'):
        result = requests.delete(url)
    # Se imprime por pantalla el código de estado y el cuerpo de la respuesta
    print("[-] RESPONSE STATUS CODE --> ", result.status_code)
    print("[-] RESPONSE BODY --> ", result.text)

def main():
    """Realiza todas las peticiones declaradas en la lista "requests_list" e 
    imprime las respuestas por pantalla
    """

    print('================ CLIENT OF THE API REST ================')
    # Se llama a cada uno de los métodos que realizan las peticiones. 
    # Por cada método llamado se espera 1 segundo
    for http_method, url in requests_list:
        print_client_method(http_method=http_method, url=url)
        time.sleep(1)

if __name__ == '__main__':
    main()
    



# Práctica - Módulo 3 - Gestión de Proyectos y Factorías Software

El objetivo de la práctica del módulo 3 de la asignatura es desarrollar una API REST utilizando Python y Flask y un cliente que la consuma y que sirva para mostrar cómo consumir dicha API, además de documentarla adecuadamente.

## 1. Desarrollo de la API REST

La API REST se ha desarrollado utilizando las siguientes librerías:
- ***Flask*** para el desarrollo de la API REST.
- ***werkzeug*** para gestionar las excepciones generales de la API REST ajenas a los controladores/endpoints declarados.

Los endpoints de esta API REST, con sus métodos HTTP permitidos, son los siguientes:
- ***[http://localhost:5000/options/](http://localhost:5000/options/)*** -> GET -> Sin parámetros -> Devuelve los principales métodos HTTP de una API REST y los errores más comunes.
- ***[http://localhost:5000/sayhello/](http://localhost:5000/sayhello/)*** -> GET -> Sin parámetros -> Devuelve un *hola* al usuario.
- ***[http://localhost:5000/calculate/<num\>](http://localhost:5000/calculate/<num\>)*** -> GET -> Hay que introducir un número en la URL -> Devuelve el cuadrado del número introducido en la URL.
- ***[http://localhost:5000/calculate/?num=<num\>](http://localhost:5000/calculate/?num=<num\>)*** -> GET -> Hay que introducir el parámetro *num* -> Devuelve el cuadrado del número que se ha pasado como parámetro.
- ***[http://localhost:5000/concatenate/?cad1=<cad1\>&cad2=<cad2\>](http://localhost:5000/concatenate/?cad1=<cad1\>&cad2=<cad2\>)*** -> GET -> Hay que introducir dos parámetros: *cad1* y *cad2* -> Devuelve la concatenación de ambos parámetros.
- ***[http://localhost:5000/users/<id\>](http://localhost:5000/users/<id\>)*** -> GET -> Hay que pasar un ID de usuario en la URL de la petición -> Devuelve el nombre de usuario asociado al ID introducido en la URL.

Los datos mencionados en cada una de las peticiones anteriores se devuelven en formato JSON y dentro del campo *data* de la petición. Además, también se devuelve el *timestamp* de la petición.

## 2. Ejecución de la API REST

Para ejecutar la API REST, hay que seguir los siguientes pasos:
1. Instalar los requerimientos a partir del fichero *requirements.txt*.
```
pip install -r requirements.txt
```
2. Ejecutar el fichero *restAPI.py* con *Python*.
```
python restAPI.py
```
3. La API REST ya estaría lista para ser consumida.

## 3. Desarrollo del cliente que consume la API REST

Las peticiones se realizan con la librería de *Python* de *requests* que viene instalada por defecto. El objetivo de este cliente es mostrar ejemplos para consumir la API REST (por tanto, también funciona a modo de documentación de la API REST). También, se muestran ejemplos de error para que se vea qué respuesta arrojaría esta API REST en caso de que no encuentre la URL, no se realice la petición de forma correcta, etc. **¡¡ IMPORTANTE !!** Los métodos definidos de la API REST están en el apartado 1. Las peticiones de este apartado también contienen peticiones incorrectas para poder visualizar los errores que arroja la API REST. Si solamente desea ver los endpoints expuestos por esta API REST diríjase al apartado 1. 

Las peticiones que prueba este cliente son las siguientes:
- ***[http://localhost:5000/options/](http://localhost:5000/options/)*** -> GET -> <span style="color:green">Petición correcta</span>
- ***[http://localhost:5000/sayhello/](http://localhost:5000/sayhello/)*** -> GET -> <span style="color:green">Petición correcta</span>
- ***[http://localhost:5000/calculate/10](http://localhost:5000/calculate/10)*** -> GET -> <span style="color:green">Petición correcta</span>
- ***[http://localhost:5000/calculate/a](http://localhost:5000/calculate/a)*** -> GET -> <span style="color:red">Petición incorrecta</span>
- ***[http://localhost:5000/calculate/?num=10](http://localhost:5000/calculate/?num=10)*** -> GET -> <span style="color:green">Petición correcta</span>
- ***[http://localhost:5000/calculate/?num=a](http://localhost:5000/calculate/?num=a)*** -> GET -> <span style="color:red">Petición incorrecta</span>
- ***[http://localhost:5000/calculate/](http://localhost:5000/calculate/)*** -> GET -> <span style="color:red">Petición incorrecta</span>
- ***[http://localhost:5000/concatenate/?cad1=Hello&cad2=World](http://localhost:5000/concatenate/?cad1=Hello&cad2=World)*** -> GET -> <span style="color:green">Petición correcta</span>
- ***[http://localhost:5000/concatenate/](http://localhost:5000/concatenate/)*** -> GET -> <span style="color:red">Petición incorrecta</span>
- ***[http://localhost:5000/users/4](http://localhost:5000/users/4)*** -> GET -> <span style="color:green">Petición correcta</span>
- ***[http://localhost:5000/users/a](http://localhost:5000/users/a)*** -> GET -> <span style="color:red">Petición incorrecta</span>
- ***[http://localhost:5000/users/100](http://localhost:5000/users/100)*** -> GET -> <span style="color:red">Petición incorrecta</span>
- ***[http://localhost:5000/test/](http://localhost:5000/test/)*** -> GET -> <span style="color:red">Petición incorrecta</span>
- ***[http://localhost:5000/users/4](http://localhost:5000/users/4)*** -> POST -> <span style="color:red">Petición incorrecta</span>

## 4. Ejecución del cliente

La librería *requests* viene por defecto instalada en *Python*. Por tanto, no es necesario instalar ninguna librería. Para ejecutar el cliente hay que introducir el siguiente comando:
```
python client.py
```

La salida del cliente debería ser la siguiente:
```
================ CLIENT OF THE API REST ================
[+]  GET  REQUEST -->  http://localhost:5000/options/
[-] RESPONSE STATUS CODE -->  200
[-] RESPONSE BODY -->  {"data":{"delete":"delete some information","errors":[400,404,405,500],"get":"return the information","post":"create a new resource","put":"modify/update the information"},"timestamp":1608466898693}

[+]  GET  REQUEST -->  http://localhost:5000/sayhello/
[-] RESPONSE STATUS CODE -->  200
[-] RESPONSE BODY -->  {"data":"hola","timestamp":1608466901731}

[+]  GET  REQUEST -->  http://localhost:5000/calculate/10
[-] RESPONSE STATUS CODE -->  200
[-] RESPONSE BODY -->  {"data":100,"timestamp":1608466904770}

[+]  GET  REQUEST -->  http://localhost:5000/calculate/a
[-] RESPONSE STATUS CODE -->  400
[-] RESPONSE BODY -->  {"message":"The input (passed in the URL) has not a good format. It must be a number"}

[+]  GET  REQUEST -->  http://localhost:5000/calculate/?num=10
[-] RESPONSE STATUS CODE -->  200
[-] RESPONSE BODY -->  {"data":100,"timestamp":1608466910850}

[+]  GET  REQUEST -->  http://localhost:5000/calculate/?num=a
[-] RESPONSE STATUS CODE -->  400
[-] RESPONSE BODY -->  {"message":"The input (the parameter num) has not a good format. It must be a number"}

[+]  GET  REQUEST -->  http://localhost:5000/calculate/
[-] RESPONSE STATUS CODE -->  400
[-] RESPONSE BODY -->  {"message":"It is mandatory to introduce the parameter <num>."}

[+]  GET  REQUEST -->  http://localhost:5000/concatenate/?cad1=Hello&cad2=World
[-] RESPONSE STATUS CODE -->  200
[-] RESPONSE BODY -->  {"data":"HelloWorld","timestamp":1608466919973}

[+]  GET  REQUEST -->  http://localhost:5000/concatenate/
[-] RESPONSE STATUS CODE -->  400
[-] RESPONSE BODY -->  {"message":"It is mandatory to introduce the parameters <cad1> and <cad2>."}

[+]  GET  REQUEST -->  http://localhost:5000/users/4
[-] RESPONSE STATUS CODE -->  200
[-] RESPONSE BODY -->  {"data":"user4","timestamp":1608466926064}

[+]  GET  REQUEST -->  http://localhost:5000/users/a
[-] RESPONSE STATUS CODE -->  404
[-] RESPONSE BODY -->  {"message":"The user ID passed in the URL doesnt exist"}

[+]  GET  REQUEST -->  http://localhost:5000/users/100
[-] RESPONSE STATUS CODE -->  404
[-] RESPONSE BODY -->  {"message":"The user ID passed in the URL doesnt exist"}

[+]  GET  REQUEST -->  http://localhost:5000/test/
[-] RESPONSE STATUS CODE -->  404
[-] RESPONSE BODY -->  {"message":"The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again."}

[+]  POST  REQUEST -->  http://localhost:5000/users/4
[-] RESPONSE STATUS CODE -->  405
[-] RESPONSE BODY -->  {"message":"The method is not allowed for the requested URL."}
```

## 5. Documentación de la práctica

Tal y como se menciona en [el artículo propuesto en la asignatura](https://realpython.com/documenting-python-code/), un proyecto debe **comentarse y documentarse**. La parte de comentarios va más destinada a los desarrolladores para que el código desarrollado sea fácilmente entendible. La parte de documentación está destinada a los desarrolladores y a los usuarios que quieren utilizar la aplicación, proyecto, script, etc. 

Para la parte de comentarios, se han añadido comentarios al código siguiendo las guías de buenas prácticas del artículo. Una de las cosas que propone usar el artículo es *Type Hinting* para que se conozcan los tipos de las variables que se utilizan. Sin embargo, también se dice que utilizar esta herramienta o librería hace el código mucho más difícil de mantener. Por ese motivo, se ha decidido no utilizarlo y utilizar comentarios que describan muy bien lo que se está haciendo. Además, tal y como se comenta en el artículo, la forma de escribir el código también ayuda a que sea más fácilmente entendible. Por tanto, esto también se ha tenido muy en cuenta.

Para la parte de documentación, se han utilizados los comentarios con *"""* de Python, usando la sintaxis de Google (que es la que usa por defecto Visual Studio Code). Adicionalmente, se ha añadido un fichero ***README.md*** que explica los aspectos más importantes a tener en cuenta sobre la práctica. **Se ha utilizado el servicio de GitHub para convertir este *README* en [una página estática alojada en sus servidores](https://ariveram2111.github.io/ariveram2111/)**.

Además, con el fin de facilitar la instalación y ejecución, también se proporciona un fichero ***requirements.txt*** con las librerías necesarias para ejecutar la práctica.

## 6. Autoría de la práctica

Alberto Rivera Martínez. Contacto: [a.riveram.2016@alumnos.urjc.es](a.riveram.2016@alumnos.urjc.es).




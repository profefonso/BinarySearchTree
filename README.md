# BinarySearchTree

Crea y organiza Arboles binarios de busqueda con un API REST.

  - Crea un árbol binario a partir de un array y lo almacena en una base de datos
  - Utiliza Preorden para mostrar organizadamente un árbol
  - Presenta el valor maximo y el valor minimo del árbol generado
  - Muestra el ancestro común mas cercano entre dos nodos


### Tecnologias 

Desarrollado usando tecnologias:

* [Python] - Django Rest Framework - Gunicorn.
* [Docker] - Gestion de contenedores y despliegue.
* [PostgreSql] - Base de datos relacional.
* [Nginx] - Servidor de aplicaciones.

And of course Dillinger itself is open source with a [public repository][dill]
 on GitHub.

### Instalación

Para la instalación requiere [Docker](https://www.docker.com/) y [Docker Compose](https://docs.docker.com/compose/).

Clonar el proyecto e ingresar al directorio creado

```sh
$ git clone https://github.com/profefonso/BinarySearchTree.git
$ cd BinarySearchTree
```

Descargar y construir las imagenes necesarias

```sh
$ docker-compose build
$ docker-compose up 
```

### Probar App

Ingrese a la direccion para ver la documentacion del API en swagger
[http://localhost:1337/api/](http://localhost:1337/api/)

Crear un nuevo árbol binario.

```sh
$ curl -X POST -H "Content-Type: application/json" \
 -d '{"name":"test-tree","data":[67,39,76,28,74,44,29,85,83,87]}' \
 http://localhost:1337/tree/
```

Ver los árboles creados [http://localhost:1337/tree/](http://localhost:1337/tree/):
```sh
$ curl -X GET "http://localhost:1337/tree/" -H  "accept: application/json"
```

Ver el árbol ordenado en Pre-orden.

```sh
$ curl -X POST -H "Content-Type: application/json" -d '{"tree":"test-tree"}' http://localhost:1337/preorder/
```

Ver el valor Maximo del árbol.

```sh
$ curl -X POST -H "Content-Type: application/json" -d '{"tree":"test-tree"}' http://localhost:1337/max/
```

Ver el valor Minimo del árbol.

```sh
$ curl -X POST -H "Content-Type: application/json" -d '{"tree":"test-tree"}' http://localhost:1337/min/
```

Obtener el ancestro común más cercano.

```sh
$ curl -X POST -H "Content-Type: application/json" \
 -d '{"tree":"test-tree","node_one":29, "node_two":44}' \
 http://localhost:1337/common-ancestor/
```

License
----

MIT

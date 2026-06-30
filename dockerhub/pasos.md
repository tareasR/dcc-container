# Pasos para publicación de imagen en Docker Hub
1. contar con la cuenta en docker hub
1. autenticarnos en docker hub desde la consola
``` bash
    docker login
```
3. revisar las imagenes que deseamos publicar
``` bash
    docker images
```
4. ejecutar la imagen con los parámetros deseados, por ejemplo modo de arranque
``` bash
    docker exec -it -p in:out -w path_inicia nombre_imagen python3 app.py
```
- -w path_inicial,cambia el directorio de arranque al establecido en el path
- python3 app.py, representa el comando a ejecutar dentro del contenedor
5. hacer el commit del contenedor en ejecución con el formato del nombre de usario
``` bash
    docker ps # buscar la imagen activa
    docker commit id usuario/nombre_imagen
```
6. publicar en docker hub la imagen
``` bash
    docker push usuario/nombre_imagen
```
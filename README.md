# Proyecto Final Python 57825 -  Pedro Sanchez

## Entorno virtual
Lo primero que debe hacerse es crear un entorno virtual en el proyecto:  
```sh
python -m venv venv
```
Activar el entorno virtual con el comando:
```sh
source venv/Scripts/activate
```
O con el comando que corresponda a tu consola.

## Dependencias
Puedes ver las dependencias utilizadas en el archivo requirements.txt.  
Usa el comando `pip install` para instalarlas y así poder correr el proyecto.

## Correr el servidor
Para poner el servidor en funcionamiento, ejecutar:
```sh
python manage.py runserver
```
Con esto el servidor estará funcionando y podemos acceder a él desde http://127.0.0.1:8000/

## Navegación
Al correr el servidor y entrar a http://127.0.0.1:8000/ solo será visible un botón de redirección a la aplicación `BaseApp` y otro a la página `Admin`.

La aplicación consiste de 5 vistas principales:
  - Inicio
  - Guitarras
  - Bajos
  - Clientes
  - About

Cada una de ellas (excepto inicio y about) tiene 2 botones, uno para insertar un nuevo item en la BD, y otro para buscar en la BD; y un listado de todos los items correspondientes al modelo.  
Una vez ingresado a una sección, elegir la acción y llenar el formulario.

Si se elige insertar datos en la BD, al llenar el formulario serás redirigido a la página de Inicio, y podrás ver los cambios dentro de `db.sqlite3`.

Si se elige buscar datos, al llenar el formulario serás redirigido a `results.html` donde se mostrarán los datos correspondientes a tu búsqueda.

Si se elige ingresar al detalle de algún item, entraras en una página donde se verán todos los datos correspondientes a ese objeto.

## Funcionamiento
La aplicación funciona de manera que al ingresar en cualquiera de las rutas mostradas en `BaseApp/urls.py` se llama a la función correspondiente de `BaseApp/views.py` y renderiza el template que le corresponda.

Todas las páginas de detalle y formularios estan protegidos tal que si no se está loggeado no se podrán visualizar.  
Las páginas Inicio, About, y List (Clientes no incluido) son visibles, pero si se intenta ingresar más adentro no se podrá.  
Para ello se deberá crear un usuario y después hacer login.

Al entrar a cualquiera de los 3 forms para ingreso de datos, se hace una petición HTTP POST de manera que se instancia un nuevo objecto del modelo correspondiente (`BaseApp/models.py`), y se llama al método `save()` para cargarlo en la BD.

Si se ingresa a los forms de búsqueda de información, al llenar el fomulario, se hace una petición GET del item correspondiente y se redirecciona al usuario a la url de resultados que usa el template `BaseApp/templates/BaseApp/results.html`, ejemplo: http://127.0.0.1:8000/BaseApp/search-results/?guitar=Epiphone.

Por último, cuando se ingresa al detalle de un item de la BD, se hace una petición GET al servidor para que devuelva todos los datos correspondientes al objeto llamado. Ejemplo de url: http://127.0.0.1:8000/BaseApp/guitarras/2/

## Admin
Se puede acceder a la página de admin desde http://127.0.0.1:8000/admin/  
Las credenciales del superuser son genéricas, puedes entrar a él con:
  - User: admin
  - Pass: admin
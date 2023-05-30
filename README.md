# WatchFileQt
Scripts para detectar los cambios en los archivos .ui

El script principal es "watch_files.py" este detecta los archivos que terminen en .ui y aplica las acciones que ahi se establece en este caso crear un archivo compilado y un archivo de recursos compilado.
Este tiene un pequeño detalle y es que no detectara archivos .ui que no hayan cambiado el nombre de untitled.ui esto debido a lo siguiente:
  
    - QtDesigner genera una extensión temporal para todo archivo .ui que no tenga un titulo perosnalizado asignado, por lo que el archivo final resultara como: untitled.ui.jhf
    - Esto no pasa si colocamos un nombre a nuestro archivo.
 
** RECORDAR **
    - Los archivos que genera qt se generar 3 veces:
      
      - Primero genera un archivo .ui.erd ---- este es el archivo temporal
      - Luego genera el archivo .ui vacio
      - Finalmente ese archivo .ui le introduce el código y lo guarda
      
 El segundo script aun no esta provado pero pretende erradicar el problema de la extensión temporal de los archivos para que funcione con cualquier archivo .ui sin importar si tiene un titulo perosnalizado o no

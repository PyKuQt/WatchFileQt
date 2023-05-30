import os
import time
import subprocess

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class UiChange(FileSystemEventHandler):
    def __init__(self) -> None:
        super().__init__()

        self.ultima_vez_modificado = 0

        self.ruta_trabajo = os.getcwd() + "\\"

        print("Escuchando... {}".format(self.ruta_trabajo))

    def on_modified(self, event):
        print(event.src_path)
        if event.src_path.endswith('.ui'):
            print(event.src_path)
            cambio_actual = os.path.getmtime(event.src_path)
            if cambio_actual != self.ultima_vez_modificado:
                self.ultima_vez_modificado = cambio_actual

                #self.crear_pyuic(event.src_path)
    
    def crear_pyuic(self,path):
        ruta_relativa = path.replace(".\\","")
        nombre_archivo = ruta_relativa.replace(".ui","")
        nombre_archivo = nombre_archivo.split("\\")[-1]
        nombre_compilado = nombre_archivo + ".py"

        nuevo_compilado = self.ruta_trabajo + "src\\views\\compiled\\"+nombre_compilado


        subprocess.run(["pyuic5","-o",nuevo_compilado,ruta_relativa])

        #print("Modificado UI: {}".format(nombre_archivo))

        self.crear_pyrcc()
    
    def crear_pyrcc(self):
        try:
            ruta_qrc = self.ruta_trabajo+"resource.qrc"
            ruta_compilado = self.ruta_trabajo+"resource_rc.py"

            subprocess.run(["pyrcc5","-o",ruta_compilado,ruta_qrc])

            #print("Modificado qrc: {}".format(ruta_compilado))
        except FileExistsError:
            print("Imposible crear archivo de recursos")

if __name__=="__main__":
    event_handler = UiChange()
    observer = Observer()
    observer.schedule(event_handler,path=".",recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("Saliendo...")
    
    observer.join()


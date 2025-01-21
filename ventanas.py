#para abrir las ventanas de la aplicacion

import subprocess #para habilitar los subprocesos

#variables para saber que usuario o que herramienta o material se modificara, se ponen en este archivo ya que es compartido por todos

def registrar(usuario):#funcion para ir al archivo registro.py
    subprocess.run(["python", "registro.py", usuario], check=True)#registro.py se habre como un proceso independiente y se cierra el proceso actual #paso el valor del usuario como argumento por medio de la linea de comandos para que se pueda compartir el valor con el subproceso

def principal():#funcion para ir a la ventana principal
    subprocess.run(["python", "main.py"], check=True)

def inventario(usuario):#funcion para ir a la ventana de inventario
    subprocess.run(["python", "inventario.py", usuario], check=True)#paso el valor del usuario como argumento por medio de la linea de comandos para que se pueda compartir el valor con el subproceso

def menu(usuario):#funcion para ir a la ventana de menu
    subprocess.run(["python", "menuadmin.py", usuario], check=True)#paso el valor del usuario como argumento por medio de la linea de comandos para que se pueda compartir el valor con el subproceso

def menuus(usuario):#funcion para ir a la ventana de menu del usuario
    subprocess.run(["python", "menu.py", usuario], check=True)#paso el valor del usuario como argumento por medio de la linea de comandos para que se pueda compartir el valor con el subproceso

def reginventario(usuario):#funcion para ir a la ventana de registrar_inventario
    subprocess.run(["python", "registrar_inventario.py", usuario], check=True)#paso el valor del usuario como argumento por medio de la linea de comandos para que se pueda compartir el valor con el subproceso

def usuarios(usuario):#funcion para ir a la ventana de usuarios
    subprocess.run(["python", "usuarios.py", usuario], check=True)#paso el valor del usuario como argumento por medio de la linea de comandos para que se pueda compartir el valor con el subproceso

def modusuario(usuario, usmod):#funcion para ir a la ventana de modificar usuarios
    subprocess.run(["python", "modificarus.py", usuario, usmod], check=True)#paso el valor del usuario como argumento por medio de la linea de comandos para que se pueda compartir el valor con el subproceso
    #recibe el usuario a modificar y modifica el valor de la variable usuario para que este valor tambien pueda ser accedido por la ventana de modificar usuario

def modperfil(usuario):#funcion para ir a la ventana de modificar perfil
    subprocess.run(["python", "modificarperfil.py", usuario], check=True)#paso el valor del usuario como argumento por medio de la linea de comandos para que se pueda compartir el valor con el subproceso
    #recibe el usuario a modificar y modifica el valor de la variable usuario para que este valor tambien pueda ser accedido por la ventana de modificar usuario

def modinv(usuario, tabla, invmod):#funcion para ir a la ventana de modificar inventario
    subprocess.run(["python", "modificarinv.py", usuario, tabla, invmod], check=True)#paso el valor del usuario como argumento por medio de la linea de comandos para que se pueda compartir el valor con el subproceso

def cambiarinv(usuario):#funcion para ir a la ventana de usar o agregar inventario
    subprocess.run(["python", "cambiarinv.py", usuario], check=True)#paso el valor del usuario como argumento por medio de la linea de comandos para que se pueda compartir el valor con el subproceso

def usar(usuario, tabla, invmod):#funcion para ir a la ventana de usar inventari
    subprocess.run(["python", "usar.py", usuario, tabla, invmod], check=True)#paso el valor del usuario como argumento por medio de la linea de comandos para que se pueda compartir el valor con el subproceso

def agregar(usuario, tabla, invmod):#funcion para ir a la ventana de agregar inventario
    subprocess.run(["python", "agregar.py", usuario, tabla, invmod], check=True)#paso el valor del usuario como argumento por medio de la linea de comandos para que se pueda compartir el valor con el subproceso

def usados(usuario):#funcion para ir a la ventana de usados
    subprocess.run(["python", "usados.py", usuario], check=True)#paso el valor del usuario como argumento por medio de la linea de comandos para que se pueda compartir el valor con el subproceso

def generar(usuario):#duncion para ir a generar reporte
    subprocess.run(["python", "generarreporte.py", usuario], check=True)#paso el valor del usuario como argumento por medio de la linea de comandos para que se pueda compartir el valor con el subproceso
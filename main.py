import tkinter as tk #para que sea mas facil el uso de la libreria usamos el alias tk si no puesieramos esto tendriamos que poner tkiner a cada rato
from tkinter import messagebox #para las ventanas emergentes
from tkinter import ttk #para el estilo
import cone #para la coneccion ala base de datos
import ventanas #para poder cambiar de ventana

"""
Diego Adolfo Guerrero González
Edgar Aaron Durán Álvarez
Víctor Alfonso Covarrubias Solís

"""

conexion = cone.conectar()#se crea la coneccion a la base de datos

def cerrar():#si se cierra la ventana
    if messagebox.askokcancel("Atención", "¿Seguro que quieres salir?"):
        cone.desconectar(conexion)
        ventana.destroy()


#creacion de la ventana para el login
ventana = tk.Tk()
ventana.geometry("800x650") #ajuste del ancho y alto respectivamente
#centrar ventana
ventana.update_idletasks()
ancho_ventana = ventana.winfo_width()#para saber el ancho de la pantalla
altura_ventana = ventana.winfo_height()#para saber el largo(altura) de la pantalla
x = (ventana.winfo_screenwidth() // 2) - (ancho_ventana // 2)# // para hacer funcion piso bueno se redondea hacia abajo y queda como entero
y = (ventana.winfo_screenheight() // 2) - (altura_ventana // 2)
ventana.geometry('+{}+{}'.format(x, y - 30)) #sele resta 30 a y ya que es lo de la barra de tareas para que no afecte visualmente
ventana.title("Maquinados Industriales DURAN") #titulo de la ventana
ventana.configure(bg="#CB31D7")#color del fondo (background)
#ventana.configure(bg="black")#color del fondo (background)

style = ttk.Style()#creacion de estilo
style.theme_use("clam")#eleccion de tema, tambien hay otros como defalut y alt

label_usuario = ttk.Label(ventana, text="Usuario")#para que muestre usuario
label_usuario.pack(pady=(100,5))#acomoda el label en la ventana, el pady sirve para aumentar el espaciado en la parte de arriba y de abajo, si se usan parentesis se especifica cual de las dos

entry_usuario = ttk.Entry(ventana)
entry_usuario.pack(pady=5)#acomoda el textfield en la ventana

label_contra = ttk.Label(ventana, text="Contraseña")#para que muestre contraseña
label_contra.pack(pady=5)#acomoda el label en la ventana

entry_contra = ttk.Entry(ventana, show="*")  # Para ocultar la contraseña
entry_contra.pack(pady=5)#acomoda el textfield en la ventana


def acceder():
    usuario = entry_usuario.get()#para conseguir el texto escrito en los textfields
    contra = entry_contra.get()#para conseguir el texto escrito en los textfields
    #comprobacion con la base de datos
    if cone.buscar(conexion, "usuarios", "usuario", usuario): #se comprueba que el usuario este correcto
        contradeusuario = cone.valor_especifico(conexion, "usuarios", "contra", "usuario", usuario)#se consigue la contraseña del usuario
        if contra == contradeusuario[0]: #se comprueba que la contraseña este correcta
            messagebox.showinfo("Inicio de sesión exitoso", "Bienvenido, {}".format(usuario))
            #se mueve a la pagina principal de la aplicacion
            ventana.destroy()#para cerrar la ventana del main
            rol = cone.valor_especifico(conexion, "usuarios", "rol", "usuario", usuario)#se checa si es admin o no
            if rol[0]== "admin":#se hace de esta forma ya que la consulta regresa una tupla por lo que debemos acceder afuerzas al primer elemento aunque sea solo uno
                ventanas.menu(usuario)#se va al menu de los admins
            else:
                ventanas.menuus(usuario)#se va al menu de los usuarios
        else:
            messagebox.showinfo("Contraseña incorrecta", "Intentalo de nuevo")
    else:
        messagebox.showerror("Credenciales incorrectas", "Intentalo de nuevo")

ventana.protocol("WM_DELETE_WINDOW", cerrar)

#Botón de inicio de sesión
boton_login = ttk.Button(ventana, text="Iniciar sesión", command=acceder)#comand sirve para indicar que el boton al ser accionado llamara a la funcion acceder
boton_login.pack(pady=5)

#Ejecutar el bucle principal de la ventana
ventana.mainloop()#mainloop sirve para que ña ventana siga abierta y el usuario pueda interactuar con ella, para detenerla se debe destruir despues

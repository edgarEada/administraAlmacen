import tkinter as tk #para que sea mas facil el uso de la libreria usamos el alias tk si no puesieramos esto tendriamos que poner tkiner a cada rato
from tkinter import messagebox #para las ventanas emergentes
from tkinter import ttk #para el estilo
import cone #para la coneccion ala base de datos
import ventanas #para poder cambiar de ventana
import sys #para obtener el valor de la variable usuario desde ventanas que se va pasando desde el main para saber que usuario es el que esta logeado
import validaciones #para poder usar las validaciones

conexion = cone.conectar()#se crea la coneccion a la base de datos

def cerrar():#si se cierra la ventana
    if messagebox.askokcancel("Atención", "¿Seguro que quieres salir?"):
        cone.desconectar(conexion)
        ventana.destroy()

def regresar():#para poder regresar al menu
    ventana.destroy()#se destruye la ventana y se dirige al menu
    ventanas.menu(usuarioactual)#se tiene que seguir pasando el usuario

def regresar2():#para poder regresar al menu
    ventana.destroy()#se destruye la ventana y se dirige al menu
    ventanas.usuarios(usuarioactual)#se tiene que seguir pasando el usuario

#creacion de la ventana para el registro de usuarios
ventana = tk.Tk()
ventana.geometry("800x650") #ajuste del ancho y alto respectivamente
#centrar ventana
ventana.update_idletasks()
ancho_ventana = ventana.winfo_width()#para saber el ancho de la pantalla
altura_ventana = ventana.winfo_height()#para saber el largo(altura) de la pantalla
x = (ventana.winfo_screenwidth() // 2) - (ancho_ventana // 2)# // para hacer funcion piso bueno se redondea hacia abajo y queda como entero
y = (ventana.winfo_screenheight() // 2) - (altura_ventana // 2)
ventana.geometry('+{}+{}'.format(x, y - 30)) #sele resta 30 a y ya que es lo de la barra de tareas para que no afecte visualmente
ventana.title("Modificacion de usuario")
ventana.configure(bg="#6C74DC")#color del fondo (background)
#ventana.configure(bg="purple")#color del fondo (background)
usuarioactual = sys.argv[1] #se resive el argumento pasado por la linea de comandos que se va pasando desde el main para saber que usuario es el que esta logeado
usmod = sys.argv[2] #se resive el segundo argumento pasado por la linea de comandos que es el usuario seleccionado en la tabla

style = ttk.Style()#creacion de estilo
style.theme_use("clam")#eleccion de tema, tambien hay otros como defalut y alt

#se consiguen los datos del usuario que esta logeado
nombremod = cone.valor_especifico(conexion, "usuarios", "nombre", "usuario", usmod)#se consigue el nombre con el usuario a modificar
correomod = cone.valor_especifico(conexion, "usuarios", "correo", "usuario", usmod)#se consigue el nombre con el usuario a modificar
rolmod = cone.valor_especifico(conexion, "usuarios", "rol", "usuario", usmod)#se consigue el nombre con el usuario a modificar
contramod = cone.valor_especifico(conexion, "usuarios", "contra", "usuario", usmod)#se consigue el nombre con el usuario a modificar

#Botón de menu
boton_regresar = ttk.Button(ventana, text="Menu", command=regresar)
boton_regresar.pack(anchor="nw",padx= 5, pady=5)#anchor para colocarlo en la esquiina superior izquierda northwest

#Botón de usuarios
boton_regresar = ttk.Button(ventana, text="Atras", command=regresar2)
boton_regresar.pack(anchor="nw",padx= 5, pady=5)#anchor para colocarlo en la esquiina superior izquierda northwest

#se registran las funciones de validacion en la ventana
valnombre = (ventana.register(validaciones.val_nombre), '%P')#%P es para enviar el valor que se escribe en el entry despues de cada modificacion
valcredencial = (ventana.register(validaciones.val_credencial), '%P')#%P es para enviar el valor que se escribe en el entry despues de cada modificacion
valcorreo = (ventana.register(validaciones.val_correo), '%P')#%P es para enviar el valor que se escribe en el entry despues de cada modificacion

label_usuario = ttk.Label(ventana, text="Usuario")#para que muestre usuario
label_usuario.pack(pady=(100,5))#acomoda el label en la ventana, el pady sirve para aumentar el espaciado en la parte de arriba y de abajo, si se usan parentesis se especifica cual de las dos

entry_usuario = ttk.Entry(ventana, validate="key", validatecommand=valcredencial)#con key se asegura la validacion cada que el usuario presiona una tecla)
entry_usuario.pack(pady=5)#acomoda el textfield en la ventana
entry_usuario.insert(0, usmod)#se pone desde el principio el valor que tenia antes para que el usuario sepa que tenia y decida si cambiarlo o no

label_nombre = ttk.Label(ventana, text="Nombre")#para que muestre usuario
label_nombre.pack(pady=5)#acomoda el label en la ventana

entry_nombre = ttk.Entry(ventana, validate="key", validatecommand=valnombre)
entry_nombre.pack(pady=5)#acomoda el textfield en la ventana
entry_nombre.insert(0, nombremod)#se pone desde el principio el valor que tenia antes para que el usuario sepa que tenia y decida si cambiarlo o no
#quitar llaves ya que si se inserta un texto con espacios en un entry este sale rodeado de llaves {}
llaves = entry_nombre.get()
llaves = llaves.strip("{}")
entry_nombre.delete(0, 'end')
entry_nombre.insert(0, llaves)

label_correo = ttk.Label(ventana, text="Correo")#para que muestre contraseña
label_correo.pack(pady=5)#acomoda el label en la ventana

entry_correo = ttk.Entry(ventana, validate="key", validatecommand=valcorreo)
entry_correo.pack(pady=5)#acomoda el textfield en la ventana
entry_correo.insert(0, correomod)#se pone desde el principio el valor que tenia antes para que el usuario sepa que tenia y decida si cambiarlo o no

label_contra = ttk.Label(ventana, text="Contraseña")#para que muestre contraseña
label_contra.pack(pady=5)#acomoda el label en la ventana

entry_contra = ttk.Entry(ventana, show="*", validate="key", validatecommand=valcredencial)  # Para ocultar la contraseña
entry_contra.pack(pady=5)#acomoda el textfield en la ventana
entry_contra.insert(0, contramod)#se pone desde el principio el valor que tenia antes para que el usuario sepa que tenia y decida si cambiarlo o no

label_contra2 = ttk.Label(ventana, text="Confirmar contraseña")#para que muestre contraseña
label_contra2.pack(pady=5)#acomoda el label en la ventana

entry_contra2 = ttk.Entry(ventana, show="*", validate="key", validatecommand=valcredencial)  # Para ocultar la contraseña
entry_contra2.pack(pady=5)#acomoda el textfield en la ventana
entry_contra2.insert(0, contramod)#se pone desde el principio el valor que tenia antes para que el usuario sepa que tenia y decida si cambiarlo o no

opciones = ["admin", "usuario"]#lista de opciones para el Combobox
label_rol = ttk.Label(ventana, text="Rol")#para que muestre tipo
label_rol.pack(pady=5)#acomoda el label en la ventana, el pady sirve para aumentar el espaciado en la parte de arriba y de abajo, si se usan parentesis se especifica cual de las dos

combo_rol = ttk.Combobox(ventana, values=opciones)#se crea el combobox y como valores se le pone opciones
#el if sirve para que aparesca el rol que ya tenia el usuario a modificar
if rolmod[0] == "admin": #como es tupla se accede al primer indice
    combo_rol.set(opciones[0])#para que aparesca ya con un valor
else:
    combo_rol.set(opciones[1])#para que aparesca ya con un valor
combo_rol.pack(pady=5)

def modificar():
    global usuarioactual
    global correoactual
    usuario = entry_usuario.get()#para conseguir el texto escrito en los textfields
    contra = entry_contra.get()#para conseguir el texto escrito en los textfields
    contra2 = entry_contra2.get()#para conseguir el texto escrito en los textfields
    correo = entry_correo.get()#para conseguir el texto escrito en los textfields
    nombre = entry_nombre.get()#para conseguir el texto escrito en los textfields
    rol = combo_rol.get()#para saber que se selecciono
    #primero se comprueba que los entrys esten llenos
    if usuario.strip()!="" and contra.strip()!="" and contra2.strip()!="" and correo.strip()!="" and nombre.strip()!="":#el strip quita espacios y luego se comprueba que no esten vacios
        if not (correo.endswith("@gmail.com") or correo.endswith("@outlook.com") or correo.endswith("@hotmail.com")):#el correo debe terminar con una de esas opciones para que sea un correo valido
            messagebox.showerror("Atencion", "Correo no valido asegurate de que sea un correo real")
        else:
            if usuario != usmod and cone.buscar(conexion, "usuarios", "usuario", usuario) : #se comprueba si es diferente al que tiene el usuario al usuario a modificar y que el usuario este en la base de datos
                messagebox.showerror("Ya registrado", "Usuario ya registrado, prueba con otro")
            else:
                #el correoactual se pone con indice ya que a diferencia del usuarioactual se consigio apartir de una consulta por lo que recibio una tupla y saldra diferente aunque sea igual
                if correo != correomod[0] and cone.buscar(conexion, "usuarios", "correo", correo): #se comprueba si es diferente al correo del usuario a modificar y que el correo este en la base de datos o si dejo el mismo que ya tenia
                    messagebox.showerror("Ya registrado", "Correo ya registrado, prueba con otro")
                else:
                    if contra == contra2: #se comprueba que las contraseñas coincidan
                        messagebox.showinfo("Cambio realizado", "se modifico el usuario: {}".format(usuario))
                        if usuarioactual == usmod:#si el que se modifico es el mismo entonces 
                            usuarioactual=usuario #se actualiza el usuarioactual ya que puede que se haya modificado

                        cone.modificarusuario(conexion, usmod, nombre, correo, usuario, contra, rol)#se manda a modificar
                    else:
                        messagebox.showerror("Contraseña incorrecta", "las contraseñas no coinciden")
    else:
        messagebox.showerror("llena los campos", "No dejes campos vacios")

#Botón de registro
boton_registrar = ttk.Button(ventana, text="Modificar", command=modificar)
boton_registrar.pack(pady=5)

ventana.protocol("WM_DELETE_WINDOW", cerrar)

#Ejecutar el bucle principal de la ventana
ventana.mainloop()#mainloop sirve para que ña ventana siga abierta y el usuario pueda interactuar con ella, para detenerla se debe destruir despues

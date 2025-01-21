import tkinter as tk #para que sea mas facil el uso de la libreria usamos el alias tk si no puesieramos esto tendriamos que poner tkiner a cada rato
from tkinter import messagebox #para las ventanas emergentes
from tkinter import ttk #para el treeview y el estilo
import cone #para la coneccion ala base de datos
import ventanas #para poder cambiar de ventana
import sys #para obtener el valor de la variable usuario desde ventanas que se va pasando desde el main para saber que usuario es el que esta logeado

conexion = cone.conectar()#se crea la coneccion a la base de datos

def cerrar():#si se cierra la ventana
    if messagebox.askokcancel("Atención", "¿Seguro que quieres salir?"):
        cone.desconectar(conexion)
        ventana.destroy()

def regresar():#para poder regresar al menu
    ventana.destroy()#se destruye la ventana y se dirige al menu
    ventanas.menu(usuarioactual)#se envia el valor que recibio por la linea de comandos

def registrar():#para poder ir a registrar usuarios
    ventana.destroy()
    ventanas.registrar(usuarioactual)#se envia el valor que recibio por la linea de comandos

def eliminar():
    seleccionado = tree.selection()
    if seleccionado:#se corrobora que un registro este seleccionado
        # Obtener los valores del elemento seleccionado
        id = tree.item(seleccionado, "values")[0] #el valor de la primera columna es el id
        useliminar = tree.item(seleccionado, "values")[3] #el valor de la cuarta columna es el usuario
        if useliminar == usuarioactual:#si se intenta eliminar el mismo
            messagebox.showerror("Cancelado", "No te puedes eliminar a ti mismo")
        else:#si es otro usuario
            opcion = messagebox.askquestion("Cuidado", "En verdad eliminara al usuario: {}?".format(useliminar))#se pregunta si en verdad lo borrara
            if opcion == 'yes':
                cone.eliminar_registro(conexion, "usuarios", id)#se manda a eliminar el usuario con la id seleccionada
                messagebox.showinfo("Eliminado", "Eliminado de usuarios")
            else:
                messagebox.showinfo("Cancelado", "no se elimino")
    mostrar_tabla()#se muestra la tabla

def modificar():
    seleccionado = tree.selection()
    if seleccionado:#se corrobora que un registro este seleccionado
        # Obtener los valores del elemento seleccionado
        usmod = tree.item(seleccionado, "values")[3] #el valor de la cuarta columna es el usuario por lo que es el que se guarda
        opcion = messagebox.askquestion("Cuidado", "En verdad modificara al usuario: {}?".format(usmod))#se pregunta si en verdad lo borrara
        if opcion == 'yes':
            ventana.destroy()
            ventanas.modusuario(usuarioactual, usmod)#se va a la interfaz de modificar usuario, usmod es el usuario que se modificara, actual sirve para ver si es el mismo el que se quiere modificar
        else:
            messagebox.showinfo("Cancelado", "no se modificara")


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
ventana.title("Usuarios")
ventana.configure(bg="#E9191C")#color del fondo (background)
#ventana.configure(bg="#1B175F")#color del fondo (background)
usuarioactual = sys.argv[1] #se resive el argumento pasado por la line a de comandos que se va pasando desde el main para saber que usuario es el que esta logeado

style = ttk.Style()#creacion de estilo
style.theme_use("clam")#eleccion de tema, tambien hay otros como defalut y alt

#Botón de menu
boton_regresar = ttk.Button(ventana, text="Menu", command=regresar)
boton_regresar.pack(anchor="nw",padx= 5, pady=5)#anchor para colocarlo en la esquiina superior izquierda northwest

tree = ttk.Treeview(ventana)#crear Treeview o tabla del tkinter
#tree.pack()#se agrega a la ventana
def mostrar_tabla():#para poder actualizarla si se hacen cambios
    #primero se limpia la tabla
    if tree.get_children():#si no esta vacio
        for item in tree.get_children():
            tree.delete(item)
            
    filas = cone.mostrar_tabla(conexion, "usuarios")#conseguir la informacion de la tabla a mostrar
    if filas:#solo si consiguio informacion la mostrara ya que si no sale una excepcion
        tree["columns"] = tuple(range((len(filas[0]))-1))#se saca la longitud de la primera fila para saber cuantas columnas son, se le quita uno para no mostrar la contraseña
        #el atributo columns de treeview necesita una tupla por eso se hace el rengo y se convierte en una
        #gracias al rango las columnas se identican con numeros del 0 a el numero de campos menos uno
        tree["show"] = "headings"  #para evitar que salgan filas vacias al principio

        # Agregar encabezados
        tree.heading(0, text="Id")
        tree.heading(1, text="Nombre")
        tree.heading(2, text="Correo")
        tree.heading(3, text="Usuario")
        tree.heading(4, text="rol")
        tree.column('0', width='50', anchor=tk.CENTER)#cambio el ancho de una columna 
        tree.column('1', width='50', anchor=tk.CENTER)#cambio el ancho de una columna
        tree.column('2', width='50', anchor=tk.CENTER)#cambio el ancho de una columna
        tree.column('3', width='50', anchor=tk.CENTER)#cambio el ancho de una columna
        tree.column('4', width='50', anchor=tk.CENTER)#cambio el ancho de una columna

        style.configure("Treeview.Heading", background="#0EDAA8")#cambio del fondo de los encabezados
        tree["style"] = "mystyle.Treeview"#se aplica el estilo al treeview
        # Agregar filas
        for fila in filas:
            tree.insert("", "end", values=fila)#inserta la fila en la tabla el end sirve para que la siguiente fila este despues de la anterior

        tree.pack(fill="both", expand=True)#para que el contenido se expanda en todo el treeview

mostrar_tabla()#se muestra la tabla
#Botón de eliminar
boton_eliminar = ttk.Button(ventana, text="Eliminar usuario seleccionado", command=eliminar)
boton_eliminar.pack(pady=5)

#Botón de modificar
boton_modificar = ttk.Button(ventana, text="Modificar usuario seleccionado", command=modificar)
boton_modificar.pack(pady=5)

#Botón de registro
boton_registrar = ttk.Button(ventana, text="Registrar nuevo usuario", command=registrar)
boton_registrar.pack(pady=5)

ventana.protocol("WM_DELETE_WINDOW", cerrar)

#Ejecutar el bucle principal de la ventana
ventana.mainloop()#mainloop sirve para que ña ventana siga abierta y el usuario pueda interactuar con ella, para detenerla se debe destruir despues

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
    #se checa el ro, del usuario para saber a que menu ir
    querol = cone.valor_especifico(conexion, "usuarios", "rol", "usuario", usuarioactual) #se busca el rol usando el valor de usuario
    if querol[0] == "admin":
        ventanas.menu(usuarioactual)#se envia el valor que recibio por la linea de comandos
    else:#es usuario
        ventanas.menuus(usuarioactual)#se envia el valor que recibio por la linea de comandos

def usarinv():
    seleccionado = tree.selection()
    if seleccionado:#se corrobora que un registro este seleccionado
        # Obtener los valores del elemento seleccionado
        tabla = tabla = combo_tabla.get()#para saber que se selecciono
        invusar = tree.item(seleccionado, "values")[0] #el valor de la primer columna es el id y se guarda
        opcion = messagebox.askquestion("Atencion", "se usara {}: {}?".format(tabla, invusar))#se pregunta si en verdad lo borrara
        if opcion == 'yes':
            ventana.destroy()
            ventanas.usar(usuarioactual, tabla, invusar)#se va a la interfaz de usar inventario 
        else:
            messagebox.showinfo("Cancelado", "no se usara")

def agregarinv():
    seleccionado = tree.selection()
    if seleccionado:#se corrobora que un registro este seleccionado
        # Obtener los valores del elemento seleccionado
        tabla = tabla = combo_tabla.get()#para saber que se selecciono
        invagregar = tree.item(seleccionado, "values")[0] #el valor de la primer columna es el id y se guarda
        opcion = messagebox.askquestion("Atencion", "se agregara {}: {}?".format(tabla, invagregar))#se pregunta si en verdad lo borrara
        if opcion == 'yes':
            ventana.destroy()
            ventanas.agregar(usuarioactual, tabla, invagregar)#se va a la interfaz de usar inventario 
        else:
            messagebox.showinfo("Cancelado", "no se agregara")




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
ventana.title("Usar Inventario")
ventana.configure(bg="#E9191C")#color del fondo (background)
#ventana.configure(bg="black")#color del fondo (background)

usuarioactual = sys.argv[1] #se resive el argumento pasado por la line a de comandos que se va pasando desde el main para saber que usuario es el que esta logeado

style = ttk.Style()#creacion de estilo
style.theme_use("clam")#eleccion de tema, tambien hay otros como defalut y alt

def actualiza(event):#para que se actulize dependiendo de que se seleccione en el combobox

    tree.delete(*tree.get_children())#vaciar el contenido actual de la tabla

    tabla = combo_tabla.get()#para saber que se selecciono

    filas = cone.mostrar_tabla(conexion, tabla)#conseguir la informacion de la tabla a mostrar
    if filas:#solo si consiguio informacion la mostrara ya que si no sale una excepcion
        tree["columns"] = tuple(range(len(filas[0])))#se saca la longitud de la primera fila para saber cuantas columnas son
        #el atributo columns de treeview necesita una tupla por eso se hace el rengo y se convierte en una
        #gracias al rango las columnas se identican con numeros del 0 a el numero de campos menos uno
        tree["show"] = "headings"  #para evitar que salgan filas vacias al principio

        # Agregar encabezados
        tree.heading(0, text="Id")
        tree.heading(1, text="Nombre")
        tree.heading(2, text="Categoria")
        tree.heading(3, text="Cantidad")
        tree.heading(4, text="Medida")
        tree.heading(5, text="Longitud")
        tree.heading(6, text="Minimo")
        tree.column('0', width='50')#cambio el ancho de una columna
        tree.column('1', width='50')#cambio el ancho de una columna
        tree.column('2', width='50')#cambio el ancho de una columna
        tree.column('3', width='50')#cambio el ancho de una columna
        tree.column('4', width='50')#cambio el ancho de una columna
        tree.column('5', width='50')#cambio el ancho de una columna
        tree.column('6', width='50')#cambio el ancho de una columna

        style.configure("Treeview.Heading", background="#0EDAA8")#cambio del fondo de los encabezados
        tree["style"] = "mystyle.Treeview"#se aplica el estilo al treeview

        # Agregar filas
        for fila in filas:
            tree.insert("", "end", values=fila)#inserta la fila en la tabla el end sirve para que la siguiente fila este despues de la anterior

        tree.pack(fill="both", expand=True)#para que el contenido se expanda en todo el treeview
        # Vincular el evento de selección a la función on_select


#Botón de menu
boton_regresar = ttk.Button(ventana, text="Menu", command=regresar)
boton_regresar.pack(anchor="nw",padx= 5, pady=5)#anchor para colocarlo en la esquiina superior izquierda northwest

label_usuario = ttk.Label(ventana, text="Inventario")#para que muestre usuario
label_usuario.pack(pady=(55,5))#acomoda el label en la ventana, el pady sirve para aumentar el espaciado en la parte de arriba y de abajo, si se usan parentesis se especifica cual de las dos


opciones = ["herramientas", "material"]#lista de opciones para el Combobox
combo_tabla = ttk.Combobox(ventana, state="readonly", values=opciones)#se crea el combobox y como valores se le pone opciones
combo_tabla.pack(pady=5)
combo_tabla.bind("<<ComboboxSelected>>", actualiza)  # Vincular función al evento de selección del Combobox

tree = ttk.Treeview(ventana)#crear Treeview o tabla del tkinter
tree.pack()#se agrega a la ventana

#Botón de usar
boton_eliminar = ttk.Button(ventana, text="usar seleccionado", command=usarinv)
boton_eliminar.pack(pady=5)

#Botón de agregar
boton_modificar = ttk.Button(ventana, text="agregar seleccionado", command=agregarinv)
boton_modificar.pack(pady=5)

ventana.protocol("WM_DELETE_WINDOW", cerrar)

#Ejecutar el bucle principal de la ventana
ventana.mainloop()#mainloop sirve para que ña ventana siga abierta y el usuario pueda interactuar con ella, para detenerla se debe destruir despues

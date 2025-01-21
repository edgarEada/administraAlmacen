import tkinter as tk #para que sea mas facil el uso de la libreria usamos el alias tk si no puesieramos esto tendriamos que poner tkiner a cada rato
from tkinter import messagebox #para las ventanas emergentes
from tkinter import ttk #para el combobox y los estilos
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

def regresar2():#para poder regresar a cambiarinv
    ventana.destroy()#se destruye la ventana y se dirige al menu
    ventanas.cambiarinv(usuarioactual)#se tiene que seguir pasando el usuario

#creacion de la ventana para el registro de herramientas y materiales
ventana = tk.Tk()
ventana.geometry("800x650") #ajuste del ancho y alto respectivamente
#centrar ventana
ventana.update_idletasks()
ancho_ventana = ventana.winfo_width()#para saber el ancho de la pantalla
altura_ventana = ventana.winfo_height()#para saber el largo(altura) de la pantalla
x = (ventana.winfo_screenwidth() // 2) - (ancho_ventana // 2)# // para hacer funcion piso bueno se redondea hacia abajo y queda como entero
y = (ventana.winfo_screenheight() // 2) - (altura_ventana // 2)
ventana.geometry('+{}+{}'.format(x, y - 30)) #sele resta 30 a y ya que es lo de la barra de tareas para que no afecte visualmente
ventana.title("Agregación de  herramientas y materiales")
ventana.configure(bg="#98A086")#color del fondo (background)
#ventana.configure(bg="purple")#color del fondo (background)
usuarioactual = sys.argv[1] #se resive el argumento pasado por la linea de comandos que se va pasando desde el main para saber que usuario es el que esta logeado
tabla = sys.argv[2] #se resive el segundo argumento pasado por la linea de comandos lo seleccionado en la tabla
invcambiar = sys.argv[3] #se resive el tercer argumento pasado por la linea de comandos lo seleccionado en la tabla

style = ttk.Style()#creacion de estilo
style.theme_use("clam")#eleccion de tema, tambien hay otros como defalut y alt

#se consiguen los datos de la herramienta o material seleccionado
nombrecambiar = cone.valor_especifico(conexion, tabla, "nombre", "id", invcambiar)#se consigue el nombre de lo seleccionado a cambiar
cantidadcambiar = cone.valor_especifico(conexion, tabla, "cantidad", "id", invcambiar)#se consigue la cantidad de lo seleccionado a cambiar
#medidacambiar = cone.valor_especifico(conexion, tabla, "medida", "nombre", invcambiar)#se consigue la medida de lo seleccionado a cambiar
minimocambiar = cone.valor_especifico(conexion, tabla, "minimo", "id", invcambiar)#se consigue el minimo de lo seleccionado a cambiar

#Botón de menu
boton_regresar = ttk.Button(ventana, text="Menu", command=regresar)
boton_regresar.pack(anchor="nw",padx= 5, pady=5)#anchor para colocarlo en la esquiina superior izquierda northwest

#Botón de inventario
boton_regresar = ttk.Button(ventana, text="Atras", command=regresar2)
boton_regresar.pack(anchor="nw",padx= 5, pady=5)#anchor para colocarlo en la esquiina superior izquierda northwest


label_cantidad = ttk.Label(ventana, text="Cantidad a agregar")#para que muestre cantidad
label_cantidad.pack(pady=5)#acomoda el label en la ventana

entry_cantidad = ttk.Entry(ventana)
entry_cantidad.pack(pady=10)#acomoda el textfield en la ventana

def agregar():
    cantidad = entry_cantidad.get()#para conseguir el texto escrito en los textfields
    cant = int(cantidad)#se hace entero
    #primero se comprueba que los entrys esten llenos
    if cantidad:#si tienen informacion los campos procede al registro
        if cantidad.isdigit():#se checa que se entero en caso de que el usuario escriba la cantidad
            if cant > 0:#se checa que sea una cantidad positiva
                messagebox.showinfo("Accion realizada", "{} {}, agregado al inventario".format(tabla, nombrecambiar))
                cone.modificarvalor_especifico(conexion, tabla, "cantidad", "id", invcambiar, cantidadcambiar[0] + cant)#se cambia el valor anterior de cantidad por el ingresado pro el usuario
                if (cantidadcambiar[0] + cant) <= minimocambiar[0]:#si es menor que el minimo se volvera a recomendar que se agregen mas
                    messagebox.showwarning("Atención", "quedan {} en el inventario por lo que se recomienda agregar mas".format(cantidadcambiar[0] + cant))
            else:
                 messagebox.showerror("Valor no valido", "La cantidad debe ser mayor a 0")
        else:
            messagebox.showerror("Cantidad erronea", "Cantidad debe ser una cantidad entera")
    else:
        messagebox.showerror("llena los campos", "No dejes campos vacios")

#Botón de modificar
boton_registrar = ttk.Button(ventana, text="Agregar", command=agregar)
boton_registrar.pack(pady=5)

ventana.protocol("WM_DELETE_WINDOW", cerrar)

#Ejecutar el bucle principal de la ventana
ventana.mainloop()#mainloop sirve para que ña ventana siga abierta y el usuario pueda interactuar con ella, para detenerla se debe destruir despues

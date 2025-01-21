import tkinter as tk #para que sea mas facil el uso de la libreria usamos el alias tk si no puesieramos esto tendriamos que poner tkiner a cada rato
from tkinter import messagebox #para las ventanas emergentes
from tkinter import ttk #para el combobox y los estilos
import cone #para la coneccion ala base de datos
import ventanas #para poder cambiar de ventana
import sys #para obtener el valor de la variable usuario desde ventanas que se va pasando desde el main para saber que usuario es el que esta logeado
import datetime #para la fecha

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
ventana.title("Uso de herramientas y materiales")
ventana.configure(bg="#98A086")#color del fondo (background)
#ventana.configure(bg="#1B175F")#color del fondo (background)
usuarioactual = sys.argv[1] #se resive el argumento pasado por la linea de comandos que se va pasando desde el main para saber que usuario es el que esta logeado
tabla = sys.argv[2] #se resive el segundo argumento pasado por la linea de comandos lo seleccionado en la tabla
invcambiar = sys.argv[3] #se resive el tercer argumento pasado por la linea de comandos lo seleccionado en la tabla

style = ttk.Style()#creacion de estilo
style.theme_use("clam")#eleccion de tema, tambien hay otros como defalut y alt

#se consiguen los datos de la herramienta o material seleccionado

nombrecambiar = cone.valor_especifico(conexion, tabla, "nombre", "id", invcambiar)#se consigue el nombre de lo seleccionado a cambiar
categoriacambiar = cone.valor_especifico(conexion, tabla, "categoria", "id", invcambiar)#se consigue la categoria de lo seleccionado a cambiar
cantidadcambiar = cone.valor_especifico(conexion, tabla, "cantidad", "id", invcambiar)#se consigue la cantidad de lo seleccionado a cambiar
medidacambiar = cone.valor_especifico(conexion, tabla, "medida", "id", invcambiar)#se consigue la medida de lo seleccionado a cambiar
longitudcambiar = cone.valor_especifico(conexion, tabla, "longitud", "id", invcambiar)#se consigue la longitud de lo seleccionado a cambiar
minimocambiar = cone.valor_especifico(conexion, tabla, "minimo", "id", invcambiar)#se consigue el minimo de lo seleccionado a cambiar

#Botón de menu
boton_regresar = ttk.Button(ventana, text="Menu", command=regresar)
boton_regresar.pack(anchor="nw",padx= 5, pady=5)#anchor para colocarlo en la esquiina superior izquierda northwest

#Botón de inventario
boton_regresar = ttk.Button(ventana, text="Atras", command=regresar2)
boton_regresar.pack(anchor="nw",padx= 5, pady=5)#anchor para colocarlo en la esquiina superior izquierda northwest


label_cantidad = ttk.Label(ventana, text="Cantidad a usar")#para que muestre cantidad
label_cantidad.pack(pady=5)#acomoda el label en la ventana

entry_cantidad = ttk.Entry(ventana)
entry_cantidad.pack(pady=10)#acomoda el textfield en la ventana

label_razon = ttk.Label(ventana, text="Razon por la cual se usara")#para que muestre cantidad
label_razon.pack(pady=5)#acomoda el label en la ventana

campo_desecho = tk.Text(ventana, width=25, height=5)#campo de texto para que el usuario escriba la razon de uso
campo_desecho.pack(pady=10)#se acomoda en la ventana

#funcion para registrar en usados
def insertar_usado(id, nombre, categoria, cantidad, desecho, medida, longitud):
    fecha = datetime.date.today()#para conseguir la fecha de el momento en el que se inserta en la base de datos
    cursor = conexion.cursor()#para poder hacer las consultas sql
    consulta = "INSERT INTO usados (idproducto, nombre, categoria, cantidad, desecho, medida, longitud, fecha) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)" #para insertar los valores, especificamos las columnas.
    cursor.execute(consulta, (id, nombre, categoria, cantidad, desecho, medida, longitud, fecha))#ejecucion de la consulta
    conexion.commit()#para que se actualice la base de datos
    cursor.close()#para liberar recursos (memoria)

def registrar():
    cantidad = entry_cantidad.get()#para conseguir el texto escrito en los textfields
    desecho = campo_desecho.get("1.0", "end-1c")#consigo el texto del campo de texto desde la primera linea sin que importe el salto de linea
    cant = int(cantidad)#se hace entero
    #primero se comprueba que los entrys esten llenos
    if cantidad and desecho:#si tienen informacion los campos procede al registro
        if cantidad.isdigit():#se checa que se entero en caso de que el usuario escriba la cantidad
            if cant > 0:#la cantidad debe ser positiva
                if cant <= cantidadcambiar[0]:#la cantidad que se quiere usar debe ser menor o igual a la cantidad del producto, como la cantidad del seleccionado es una tupa se usa indice
                    messagebox.showinfo("Accion realizada", "{} {}, restada de inventario".format(tabla, nombrecambiar[0]))
                    insertar_usado(invcambiar, nombrecambiar[0], categoriacambiar[0], cantidad, desecho, medidacambiar[0], longitudcambiar[0])#se manda a registrar en usados
                    cone.modificarvalor_especifico(conexion, tabla, "cantidad", "id", invcambiar, cantidadcambiar[0] - cant)#se cambia el valor anterior de cantidad por lo que sobra de la resta de lo que se tenia y lo que se quito
                    if (cantidadcambiar[0] - cant) <= minimocambiar[0]:
                        messagebox.showwarning("Atención", "quedan {} en el inventario por lo que se recomienda agregar mas".format(cantidadcambiar[0] - cant))
                else:
                    messagebox.showerror("Valor no valido", "La cantidad a usar es mayor a la que se encuentra en el inventario")
            else:
                messagebox.showerror("Valor no valido", "La cantidad a usar debe ser mayor que 0")
        else:
            messagebox.showerror("Cantidad erronea", "Cantidad debe ser una cantidad entera")
    else:
        messagebox.showerror("llena los campos", "No dejes campos vacios")

#Botón de modificar
boton_registrar = ttk.Button(ventana, text="Usar", command=registrar)
boton_registrar.pack(pady=5)

ventana.protocol("WM_DELETE_WINDOW", cerrar)

#Ejecutar el bucle principal de la ventana
ventana.mainloop()#mainloop sirve para que ña ventana siga abierta y el usuario pueda interactuar con ella, para detenerla se debe destruir despues

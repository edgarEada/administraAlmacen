import mysql.connector #para poder usar el lenguaje sql

#funcion para conectarse ala base de datos
def conectar():
    conexion = mysql.connector.connect(
        host="localhost",    #como es base local se usa localhost como host
        user="root",      #usuario
        password="",  #contraseña
        database="almacentorno" #nos conecatremos ala base de datos llamada almacentorno
    )
    return conexion

#funcion para cerrar la conexion a la base de datos
def desconectar(conexion):
    conexion.close()

#funcion para buscar valores en una tabla
def buscar(conexion, tabla, campo, valor):
    cursor = conexion.cursor()#para poder hacer lñas consultas sql
    consulta = "SELECT * FROM {} WHERE {} = %s".format(tabla, campo)#consulta
    cursor.execute(consulta, (valor,))#ejecucion de la consulta se pone una coma despues ya que es una tupla y si es una tupla de solo un elemento siempre debe agregarse la coma al final
    encontrado = cursor.fetchall()#para conseguir todas las filas de la tabla en caso de que el valor se repita 
    cursor.close()#para liberar recursos (memoria)
    return encontrado

#funcion para mostrar la tabla
def mostrar_tabla(conexion, tabla):
    cursor = conexion.cursor()#para poder hacer lñas consultas sql
    consulta = "SELECT * FROM {}".format(tabla)#consulta de la tabla
    cursor.execute(consulta)#ejecucion de la consulta
    filas = cursor.fetchall()#para conseguir todas las filas de la tabla en caso de que el valor se repita 
    cursor.close()#para liberar recursos (memoria)
    return filas

#funcion para eliminar un registro de la tabla
def eliminar_registro(conexion, tabla, valor):
    cursor = conexion.cursor()#para poder hacer lñas consultas sql
    consulta = "DELETE FROM {} WHERE Id = %s".format(tabla)#consulta de la tabla
    cursor.execute(consulta, (valor,))#ejecucion de la consulta se pone una coma despues ya que es una tupla y si es una tupla de solo un elemento siempre debe agregarse la coma al final
    conexion.commit()#para que se actualice la base de datos
    cursor.close()#para liberar recursos (memoria)

#funcion para buscar un valor en especifico en un registro
def valor_especifico(conexion, tabla, campobus, campo, valor):
    cursor = conexion.cursor()#para poder hacer lñas consultas sql
    consulta = "SELECT {} FROM {} WHERE {} = %s".format(campobus, tabla, campo)#consulta
    cursor.execute(consulta, (valor,))#ejecucion de la consulta se pone una coma despues ya que es una tupla y si es una tupla de solo un elemento siempre debe agregarse la coma al final
    encontrado = cursor.fetchone()#para conseguir todas las filas de la tabla en caso de que el valor se repita 
    cursor.close()#para liberar recursos (memoria)
    return encontrado

#funcion para modificar un valor en especifico en un registro
def modificarvalor_especifico(conexion, tabla, campomod, campo, valor, nuevovalor):
    cursor = conexion.cursor()#para poder hacer lñas consultas sql
    consulta = "UPDATE {} SET {} = %s WHERE {} = %s".format(tabla, campomod,campo)#consulta
    cursor.execute(consulta, (nuevovalor, valor))#ejecucion de la consulta 
    conexion.commit()#para que se actualice la base de datos
    cursor.close()#para liberar recursos (memoria)

#funcion para modificar un usuario
def modificarusuario(conexion, usuario, nuevonombre, nuevocorreo, nuevousuario, nuevacontra, nuevorol = "usuario"):#se pone que el parametro de rol es predeterminado ya que el propio usuario no se puede cambiar el rol nomas lo puede hacer un administrador
    cursor = conexion.cursor()#para poder hacer lñas consultas sql
    consulta = "UPDATE usuarios SET nombre = %s, correo = %s, usuario = %s, rol = %s, contra = %s WHERE usuario = %s" #consulta
    cursor.execute(consulta, (nuevonombre, nuevocorreo, nuevousuario, nuevorol, nuevacontra, usuario))#ejecucion de la consulta 
    conexion.commit()#para que se actualice la base de datos
    cursor.close()#para liberar recursos (memoria)

#funcion para modificar inventario
def modificarinv(conexion, tabla, id, nuevonombre, nuevacategoria, nuevacantidad, nuevamedida, nuevalongitud, nuevominimo):
    cursor = conexion.cursor()#para poder hacer lñas consultas sql
    consulta = "UPDATE {} SET nombre = %s, categoria = %s, cantidad = %s, medida = %s, longitud= %s, minimo = %s WHERE id = %s".format(tabla) #consulta
    cursor.execute(consulta, (nuevonombre, nuevacategoria, nuevacantidad, nuevamedida, nuevalongitud, nuevominimo, id))#ejecucion de la consulta 
    conexion.commit()#para que se actualice la base de datos
    cursor.close()#para liberar recursos (memoria)

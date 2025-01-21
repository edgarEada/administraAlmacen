import mysql.connector
from fpdf import FPDF
from estilos import *
import datetime
from dateutil.relativedelta import relativedelta
import tkinter as tk #para que sea mas facil el uso de la libreria usamos el alias tk si no puesieramos esto tendriamos que poner tkiner a cada rato
from tkinter import messagebox #para las ventanas emergentes
import os
import webbrowser

def abrir_reporte(ruta):
    # Acción a realizar después de que se presiona "Aceptar"
    webbrowser.open("file:"+ruta)
    print("Se presionó 'Aceptar'")

def mensaje_exito(ruta):
    messagebox.showinfo("Informe generado", "Informe generado")
    ruta_absoluta = os.path.abspath(ruta)
    abrir_reporte(ruta_absoluta)  # Llama a la función que realiza la acción

def obtenerConsulta(opcion):
    # Obtener la fecha actual
    hoy = datetime.datetime.today()

    if opcion == 1:
        # Calcular el inicio de la semana (lunes)
        inicio_semana = hoy - datetime.timedelta(days=hoy.weekday())
        sql = "SELECT * from `usados` WHERE `fecha` >= '{}';".format(inicio_semana.strftime('%Y-%m-%d'))
    elif opcion ==2:
        # Obtener el primer día del mes actual
        primer_dia_mes = hoy.replace(day=1)
        sql = "SELECT * from `usados` WHERE `fecha` >= '{}';".format(primer_dia_mes.strftime('%Y-%m-%d'))
    elif opcion ==3:
        # Restar 6 meses a la fecha actual
        hace_6_meses = hoy - relativedelta(months=6)
        # Obtener el primer día del mes de hace 6 meses
        primer_dia_hace_6_meses = hace_6_meses.replace(day=1)
        sql = "SELECT * from `usados` WHERE `fecha` >= '{}';".format(primer_dia_hace_6_meses.strftime('%Y-%m-%d'))
    elif opcion==4:
        # Restar 12 meses a la fecha actual
        hace_12_meses = hoy - relativedelta(months=12)
        # Obtener el primer día del mes de hace 6 meses
        primer_dia_hace_12_meses = hace_12_meses.replace(day=1)
        sql = "SELECT * from `usados` WHERE `fecha` >= '{}';".format(primer_dia_hace_12_meses.strftime('%Y-%m-%d'))
    else:
        sql = "SELECT * from `usados`;"
    
    return sql

def generaReporte(periodo):
    conexion = mysql.connector.connect(user='root', password='',
                                    host='localhost',
                                    database='almacentorno',
                                    port='3306')

    cursor = conexion.cursor()
    if periodo == 0:
        ruta = "informes/informeSemanal-"+datetime.datetime.strftime(datetime.datetime.now(),"%d-%m-%Y-%H-%M-%S")+".pdf"
        sql = obtenerConsulta(1)
    elif periodo == 1:
        ruta = "informes/informeMensual-"+datetime.datetime.strftime(datetime.datetime.now(),"%d-%m-%Y-%H-%M-%S")+".pdf"
        sql = obtenerConsulta(2)
    elif periodo == 2:
        ruta = "informes/informeSemestral-"+datetime.datetime.strftime(datetime.datetime.now(),"%d-%m-%Y-%H-%M-%S")+".pdf"
        sql = obtenerConsulta(3)
    elif periodo == 3:
        ruta = "informes/informeAnual-"+datetime.datetime.strftime(datetime.datetime.now(),"%d-%m-%Y-%H-%M-%S")+".pdf"
        sql = obtenerConsulta(4)
    elif periodo == 4:
        ruta = "informes/informeHistorico-"+datetime.datetime.strftime(datetime.datetime.now(),"%d-%m-%Y-%H-%M-%S")+".pdf"
        sql = obtenerConsulta(5)

    cursor.execute(sql)
    resultados = cursor.fetchall()
    if resultados:
        pdf = FPDF(orientation='L', unit='mm', format='A4')
        #pdf = PDF()

        pdf.alias_nb_pages()
        pdf.add_page()

        #Imagen
        pdf.image('media/logoMID.jpeg',x=10,y=10,w=50)
        #Texto
        pdf.set_font('Arial','B',25)
        # Move to the right
        pdf.cell(80)
        #Fecha del informe
        fecha = datetime.datetime.strftime(datetime.datetime.now(),"%d/%m/%Y")
        #Titulo
        pdf.cell(90,30,'Informe de material '+ fecha,0,1,'C',0)
        # Page number
        #pdf.set_font('Arial','',12)
        #pdf.multi_cell(0, 10, 'Página ' + str(pdf.page_no()) + '/{nb}', 0, 1, 'C')
        #Line break
        pdf.ln(20)


        #Metadatos
        pdf.set_title("Informe")
        pdf.set_author("Almacen Torno App")
        pdf.set_creator("Almacen Torno App")
        pdf.set_keywords("Informe, PDF, Uso, Almacén")
        pdf.set_subject("Informe de uso")

        #Encabezados
        pdf.set_font('Arial','B',12)
        backcol(pdf,"aqua")
        pdf.cell(10, 15, "Id", 1, 0, "C", 1)
        pdf.cell(50, 15, "Nombre", 1, 0, "C", 1)
        pdf.cell(30, 15, "Categoria", 1, 0, "C", 1)
        pdf.cell(30, 15, "Cantidad", 1, 0, "C", 1)
        pdf.cell(40, 15, "Motivo de desecho", 1, 0, "C", 1)
        pdf.cell(40, 15, "Medida", 1, 0, "C", 1)
        pdf.cell(30, 15, "Longitud", 1, 0, "C", 1)
        pdf.cell(0, 15, "Fecha", 1, 1, "C", 1)

        pdf.set_font('Arial','',12)
        backcol(pdf,"azul")
        par = 1
        for dato in resultados:
            if par % 2 == 0:
                backcol(pdf,"blanco")
                par+=1
            else:
                backcol(pdf,"gris")
                par+=1
            pdf.cell(10, 15, str(dato[1]), 1, 0, "C", 1)
            pdf.cell(50, 15, dato[2], 1, 0, "C", 1)
            pdf.cell(30, 15, dato[3], 1, 0, "C", 1)
            pdf.cell(30, 15, str(dato[4]), 1, 0, "C", 1)
            pdf.cell(40, 15, dato[5], 1, 0, "C", 1)
            pdf.cell(40, 15, dato[6], 1, 0, "C", 1)
            pdf.cell(30, 15, dato[7], 1, 0, "C", 1)
            pdf.cell(0, 15, str(dato[8]), 1, 1, "C", 1)

        #pdf.output('informes/informe.pdf','F')
        pdf.output(ruta,'F')
        mensaje_exito(ruta)
    else:
        messagebox.showinfo("Informe", "No hay datos")
    conexion.close()
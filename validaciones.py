from tkinter import messagebox #para las ventanas emergentes
#validacione de entrys al momento de registrar y modificar

def val_credencial(entrada):
    if len(entrada) >= 20:#se checa la cantidad, debe ser menor o igual a 20 caracteres
        messagebox.showerror("Atencion", "No puedes poner mas de 20 caracteres")
        return False
    if " " in entrada:#no puede tener espacios
        messagebox.showerror("Atencion", "No debe tener espacios")
        return False
    return True

def val_correo(entrada):
    if len(entrada) >= 20:#se checa la cantidad, debe ser menor o igual a 20 caracteres
        messagebox.showerror("Atencion", "No puedes poner mas de 20 caracteres")
        return False
    if " " in entrada:#no puede tener espacios
        messagebox.showerror("Atencion", "No debe tener espacios")
        return False
    return True

def val_nombre(entrada):
    if entrada.startswith("{") and entrada.endswith("}"):#sele quitan las llaves que tenia para verificar bien ya que al ser palabras con espacios estas se quedan entre llaves
        entrada = entrada[1:-1]  # Remover las llaves
    if len(entrada) > 30:#se checa la cantidad, debe ser menor o igual a 30 caracteres
        messagebox.showerror("Atencion", "No puedes poner mas de 30 caracteres")
        return False
    if not entrada.replace(' ', '').isalpha() and entrada !="":#se quitan espacios y se checa si son puras letras, si son puras letras entonces si esta bien, se checa ala vez que sea diferente de vacio para que no salte el error al borrar todo el texto
        messagebox.showerror("Atencion", "Solo pueden ser letras y espacios y El primer caracter no puede ser espacio")
        return False
    return True


#herramientas y materiales
def val_nombreinv(entrada):
    if entrada.startswith("{") and entrada.endswith("}"):#sele quitan las llaves que tenia para verificar bien ya que al ser palabras con espacios estas se quedan entre llaves
        entrada = entrada[1:-1]  # Remover las llaves
    if len(entrada) > 30:#se checa la cantidad, debe ser menor o igual a 30 caracteres
        messagebox.showerror("Atencion", "No puedes poner mas de 30 caracteres")
        return False
    if not entrada.replace(' ', '').isalnum() and entrada !="":#se quitan espacios y se checa si son puras letras o  numeros sin caracteres especiales, si son puras letras entonces si esta bien, se checa ala vez que sea diferente de vacio para que no salte el error al borrar todo el texto
        messagebox.showerror("Atencion", "Solo pueden ser letras y espacios y El primer caracter no puede ser espacio")
        return False
    return True

def val_medidasinv(entrada):
    if len(entrada) >= 30:#se checa la cantidad, debe ser menor o igual a 30 caracteres
        messagebox.showerror("Atencion", "No puedes poner mas de 30 caracteres")
        return False
    return True

def val_entero(entrada):
    if len(entrada) >= 5:#se checa la cantidad, debe ser menor o igual a 20 caracteres
        messagebox.showerror("Atencion", "No puedes poner mas de 5 digitos")
        return False
    if not entrada.isdigit() and entrada !="":#se checa que no pueda tene ralgo distinto a puros numeros, si la entrada no esta vacia, ya que esto permite que se pueda borrar toda la palabra
        messagebox.showerror("Atencion", "Debe ser un numero entero sin fracción")
        return False
    return True
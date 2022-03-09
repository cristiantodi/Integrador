from audioop import add
from cProfile import label
from  tkinter import *
from turtle import left, right

from setuptools import Command

raiz= Tk()
bmenu=Menu(raiz)
raiz.title=("proyecto")
#raiz.resizable(True,True)
#raiz.geometry=("2000x2000")

fram1=Frame(raiz, width=5000, height=5000)
fram1.pack()
#fram1.config(bg="blue")
fram1.pack(side="left", anchor="n") #Posicion del frame1
fram1.config(width="500", height="500") # Tamaño del fram1

#----INGRESO DE INFORMACION--------------------------------------------------
#-NOMBRE
nombre1=StringVar()
labelNombre=Label(fram1, text="Nombre:")
labelNombre.place(x=0,y=0)
textoNombre=Entry(fram1, textvariable=nombre1)
textoNombre.place(x=150,y=0)
#-APELLIDO
apellido1=StringVar()
labelApellido=Label(fram1, text="Apellido:")
labelApellido.place(x=0,y=20)
textoApellido=Entry(fram1,textvariable=apellido1)
textoApellido.place(x=150,y=20)
#-DIRECCION
direccion1=StringVar()
labelDireccion=Label(fram1, text="Direccion:")
labelDireccion.place(x=0,y=40)
textoDireccion=Entry(fram1, textvariable=direccion1)
textoDireccion.place(x=150,y=40)
#-TELEFONO
telefono1=StringVar()
labelTelefono=Label(fram1, text="Telefono:")
labelTelefono.place(x=0,y=60)
textoTelefono=Entry(fram1, textvariable=telefono1)
textoTelefono.place(x=150,y=60)
#-EDAD
edad1=StringVar()
labelEdad=Label(fram1, text="Edad:")
labelEdad.place(x=0,y=80)
textoEdad=Entry(fram1, textvariable=edad1)
textoEdad.place(x=150,y=80)
#-HIJOS
hijos1=StringVar()
labelHijos=Label(fram1, text="Numero de Hijos:")
labelHijos.place(x=0,y=100)
textoHijos=Entry(fram1, textvariable=hijos1)
textoHijos.place(x=150,y=100)
#-ESTATURA
estatura1=StringVar()
labelEstatura=Label(fram1, text="Estatura:")
labelEstatura.place(x=0,y=120)
textoEstatura=Entry(fram1,textvariable=estatura1)
textoEstatura.place(x=150,y=120)
#-SUELDO
sueldo1=StringVar()
labelSueldo=Label(fram1, text="Sueldo:")
labelSueldo.place(x=0,y=140)
textoSueldo=Entry(fram1, textvariable=sueldo1)
textoSueldo.place(x=150,y=140)
#-Dias
dias1=StringVar()
labelDias=Label(fram1, text="Dias Trabajados:")
labelDias.place(x=0,y=160)
textoDias=Entry(fram1, textvariable=dias1)
textoDias.place(x=150,y=160)

#-Genero
labelGenero=Label(fram1, text="Genero:")
labelGenero.place(x=0,y=180)
def selGenero():
    genx=genero1.get()
    if genx==1:
        Label(raiz, text="Mujer", fg="blue", font=18).place(x=500,y=180)
    elif genx==2:
        Label(raiz, text="Homnre", fg="blue", font=18).place(x=500,y=180)
    return
genero1=IntVar()
T1=Radiobutton(raiz,text="M", variable=genero1,value=1)
T2=Radiobutton(raiz,text="H", variable=genero1,value=2)
T1.place(x=150,y=180)
T2.place(x=190,y=180)

#


#print (gen)
#print (genero1.get())
#print (T1)
#print (T2)

    
#---------------    
prueba1=Menu(bmenu)
prueba1.add_command(label="copia")
#-FRAME2-----------------------------------------------------------------------------
fram2=Frame()
fram2.pack()
fram2.config(bg="red", width="300",height="300")
fram2.pack(side="right", anchor="n") #Posicion del frame2

#Label1=Label(fram2, text="HOLA MUNDO", fg="blue", font=18).place(x=0,y=0)
#Label1=Label(fram2, text="HOLA MUNDO", fg="blue", font=18).grid(row=0, column=0, padx=5, pady=5)

#-BOTON--------------------------------------------------------------------------------
def boton():
    #print(nombre1)
    Label(fram2, text=nombre1.get(), fg="blue", font=18).place(x=0,y=0)
    Label(fram2, text=apellido1.get(), fg="blue", font=18).place(x=0,y=20)
    Label(fram2, text=direccion1.get(), fg="blue", font=18).place(x=0,y=40)
    Label(fram2, text=telefono1.get(), fg="blue", font=18).place(x=0,y=60)
    Label(fram2, text=edad1.get(), fg="blue", font=18).place(x=0,y=80)
    Label(fram2, text=hijos1.get(), fg="blue", font=18).place(x=0,y=100)
    Label(fram2, text=estatura1.get(), fg="blue", font=18).place(x=0,y=120)
    Label(fram2, text=sueldo1.get(), fg="blue", font=18).place(x=0,y=140)
    Label(fram2, text=dias1.get(), fg="blue", font=18).place(x=0,y=160)
    selGenero()

            
    #Label(fram2, text=T1, fg="blue", font=18).place(x=0,y=180)
    print (genero1)
    #Label.configure(text=T1.get(), fg="blue", font=18).place(x=0,y=180)
    
botonEnviar=Button(raiz,text="Enviar", command=boton).place(x=2,y=265,width=230, height=30)
#(width=100, height=30)
#botonEnviar.pack()

raiz.mainloop()
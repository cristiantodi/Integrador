
#--------
documento=int(input("Ingrese # de documento: "))
nombre = input("Ingrese nombres : ")
apellido = input("Ingrese apellidos :  ")
direccion = input("Ingrese la direccion :  ")
edad = int(input("ingrese edad :  "))
while (edad<18 or  edad>63):
    print("La edad no escorrecta ")
    edad = int(input("ingrese edad :  "))
telefono = input("Ingrese el telefono :  ")
genero = input("ingrese genero :  ")
estado = input("Estado civil :  ")
print(estado)
while (estado!="soltero" and estado!="casado" and estado!="separado"):
    print("Estado cicil incorrecto los correcto son: soltero, casado, separado " )
    estado = input("Estado civil :  ")
hijos = int(input("Ingrese el numer de hijos :  "))
while (hijos<0):
    print("Valor invalido para # de hijos")
    hijos = int(input("Ingrese el numer de hijos :  "))
   
fechaNacimientoDia = int(input("Ingrese fecha de nacimiento (Dia) :  "))
fechaNacimientoMes = int(input("Ingrese fecha de nacimiento (Mes) :  "))
fechaNacimientoAgno = int(input("Ingrese fecha de nacimiento (Año) :  "))
sueldo = int(input("Ingrese Sueldo basico :  "))
estatura = float(input("Ingrese estatura (mt) :  "))
while (estatura<1.0 or estatura>2.5):
    print("Estatura no valida ")
    estatura = float(input("Ingrese estatura (mt) :  "))
while (sueldo<0):
    print("Valor invalido para el sueldo basico")
    sueldo = int(input("Ingrese Sueldo basico :  "))
 
diasLaborados = int(input("Ingresa los dias laborados :  "))
while (diasLaborados<0 or diasLaborados>30):
        print("Valor invalido para los dias laborados")
        diasLaborados = int(input("Ingresa los dias laborados :  "))


print("-------------------------------------------------------------------------------------")
print("El numero de documento es : ", documento)
print ("El nombre es :  ", nombre)
print ("El apellido es : " , apellido)
print ("La direccion es : " , direccion)
print ("El telefono es : " , telefono)
print ("La edad es : " , edad)
print ("El genero es : " , genero)
print ("El estado es :" , estado)
print ("El numero de hijos es : " , hijos)
print ("La estatura es : " , estatura)
print ("La fecha de nacimeinto es : " , fechaNacimientoDia,"/",fechaNacimientoMes,"/", fechaNacimientoAgno)
print ("El sueldo es : " , sueldo)
print ("Los dias laborados son : " , diasLaborados)

print("-------------------------------------------------------------------------------------")
cumpleCompañia=0
if(edad>55):
    bono=sueldo*0.05
    
if(fechaNacimientoDia==cumpleCompañia):
    print("Mereces una fiesta")
else:
    print("No hay fiesta")
    
if("casado"==estado and hijos>0):
    print("Paseo diciembre")
else:
    print("No hay paseo")

if(sueldo>1000000 and sueldo<1500000):
    print("Comision :  ", (sueldo*0.02))
elif (sueldo>1500001 and sueldo>200000):
    print("Comision :  ", (sueldo*0.05))
else:
    print("No hay comision")
        
if(diasLaborados>20 and sueldo<1000000):
    print("Bono de alimentacion")
else:
    print("No hay bono")


        
    
    







from ingreso import *

def imprime():
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

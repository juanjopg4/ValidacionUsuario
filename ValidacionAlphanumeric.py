#Crear un módulo para validación de nombres de usuarios. Dicho módulo, deberá cumplir con los siguientes criterios de aceptación:

#El nombre de usuario debe contener un mínimo de 6 caracteres y un máximo de 12.
#El nombre de usuario debe ser alfanumérico.
#Nombre de usuario con menos de 6 caracteres, retorna el mensaje "El nombre de usuario debe contener al menos 6 caracteres".
#Nombre de usuario con más de 12 caracteres, retorna el mensaje "El nombre de usuario no puede contener más de 12 caracteres".
#Nombre de usuario con caracteres distintos a los alfanuméricos, retorna el mensaje "El nombre de usuario puede contener solo letras y números".
#Nombre de usuario válido, retorna True.

import re

def validacionAlfanum(palabra):
    patron = '^[a-zA-Z0-9]+$'
    
    global result
    result = bool(re.search(patron,palabra))
    

def validacion(nombre):
      
    if len(nombre) < 6:
        print('El nombre de usuario debe contener al menos 6 caracteres')
    elif len(nombre) > 12:
        print("El nombre de usuario no puede contener más de 12 caracteres")

    validacionAlfanum(nombre)
    if result == False:
        print('El nombre de usuario puede contener solo letras y números')
    



def ValidacionPass(password):
    if not(len(password) >= 8 and re.search('[a-z]',password) and re.search('[A-Z]',password) and re.search('[1-9]',password) and re.search('[!"·$%&/()=?¿]', password) and not ' ' in password):               
        print ("La contraseña elegida no es segura")
        return False
    else:
        return True


def CreateUser():
    nombre = input('introduce tu nombre de usuario :')
    validacion(nombre)

    password = input('introduce tu contraseña :')
    ValidacionPass(password)
    
    
if __name__ == "__main__":
    CreateUser()



    


    
        
    
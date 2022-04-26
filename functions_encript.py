import functions_admins
from datetime import datetime,time
from cryptography.fernet import Fernet 

students = [["leiner","","inge","12345",[{'curso':'mate','estado':'Aprobado'},{'curso':'progra','estado':'En curso'}],[]]]
def register (): 
    auxlist = []
    courses = []
    activities = []
    name = input("Ingrese su nombre: ")
    email =  input("porfavor introduce tu gmail: ")   
    course = functions_admins.select_position_careers()
    course = functions_admins.careers[course]
    password = input("porfavor introduce una contraseña: ")
    

    key = Fernet.generate_key()
    objeto_cifrado = Fernet(key)
    texto_encriptado = objeto_cifrado.encrypt(str.encode(password))

    texto_desencriptado_bytes = objeto_cifrado.decrypt(texto_encriptado)
    texto_desencriptado = texto_desencriptado_bytes.decode()
  
    
    
    
    auxlist.append(name)
    auxlist.append(email)
    auxlist.append(course)
    auxlist.append(texto_encriptado)
    auxlist.append(courses)
    auxlist.append(activities)
    students.append(auxlist)
    print("Te has registrado con exito!!! ")
    print(students)
    
register()
def cifrar(password):
    key = Fernet.generate_key()
    objeto_cifrado = Fernet(key)
    texto_encriptado = objeto_cifrado.encrypt(str.encode(password))
    return texto_encriptado
def desencriptado(password,key,objeto_cifrado):
    texto_desencriptado_bytes = objeto_cifrado.decrypt(password)
    texto_desencriptado = texto_desencriptado_bytes.decode()
    return texto_desencriptado
  
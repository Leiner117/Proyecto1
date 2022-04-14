import csv
from distutils.log import error

def loge(): 
    while True:
        print("1. registro\n2. login\n3. salir")
        select = int (input("seleccione la opsion que desea:"))
        if (select == 1):
            register()
        elif (select == 2):
            login()
        elif (select == 3):
            break 
        
def register (): 
    with open ("users.csv.txt", 'w') as csvfile:
        writer = csv.writer (csvfile, delimiter=",") 
        email =  input("porfavor introduce tu gmail: ")   
        course = input("ingrese la o las carrera que desee cursar: ")
        password = input("porfavor introduce una contraseña: ")
        writer.writerow([email,password, course])
        print("Te has registrado con exito!!! ")

        
def login():
        email = input("porfavor introduce tu gmail: ")
        password = input("porfavor ingresa tu contraseña: ")
        with open("users.csv", mode="r") as csvfile:
            reader = csv.reader(csvfile,delimiter=",")
        for row in reader: 
            if row ==[email, password]:
                print("Usted a sido registrado!!!")
            return True 
        print("porfavor vuelva a intentarlo!!")
        return False
loge()


    
    
    
            

    
     
        
        
        

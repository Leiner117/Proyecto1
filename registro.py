import functions_admins
students = []
def register (): 
    auxlist = []
    name = input("Ingrese su nombre: ")
    email =  input("porfavor introduce tu gmail: ")   
    course = functions_admins.select_career()
    password = input("porfavor introduce una contraseña: ")
    auxlist.append(name)
    auxlist.append(email)
    auxlist.append(course)
    auxlist.append(password)
    students.append(auxlist)
    print("Te has registrado con exito!!! ")



    
    
    
            

    
     
        
        
        

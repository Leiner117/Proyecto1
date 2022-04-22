import functions_admins
students = []
def register (): 
    auxlist = []
    courses = []
    name = input("Ingrese su nombre: ")
    email =  input("porfavor introduce tu gmail: ")   
    course = functions_admins.select_position_careers()
    course = functions_admins.careers[course]
    password = input("porfavor introduce una contraseña: ")
    auxlist.append(name)
    auxlist.append(email)
    auxlist.append(course)
    auxlist.append(password)
    auxlist.append(courses)
    students.append(auxlist)
    print("Te has registrado con exito!!! ")
    print(students)
def mod_careers(name):
    new_career = functions_admins.select_position_careers()
    new_career = functions_admins.careers[new_career]
    for i in students:
        if name in i:
            i[2] = new_career
            
def assign_course(name):
    career = ""
    aux_dic = {}
    b = 0
    for i in students:
        if name in i:
            career = i[2]
            index = students.index(i)
            break
    print("Seleccione el curso que desea:")
    for a in functions_admins.courses:
        if career in a[6]:
            b = b+1
            print(str(b)+"-"+a[0])
    select = int(input("---> "))
    aux_dic["curso"] = functions_admins.courses[select-1][0]
    aux_dic["estado"] = "En curso"
    students[index][4].append(aux_dic)
    print(students)


            
                
           
                    
            
            

            
    
    
    
    
            

    
     
        
        
        

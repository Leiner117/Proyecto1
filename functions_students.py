import functions_admins
students = [["leiner","","inge","12345",[{'curso':'mate','estado':'En curso'},{'curso':'progra','estado':'En curso'}]]]
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
def index_student(name):
    for i in students:
        if name in i:
            index = students.index(i)
    return index
def mod_course_status(name):
    index = index_student(name)
    status = ""
    course = select_course_assign(index)
    print("1.Aprobado\n2.Reprobado\n3.En curso")
    num_status = int(input("Ingrese el estado del curso: "))
    if num_status == 1:
        status = "Aprobado"
    elif num_status == 2:
        status = "Reprobado"
    elif num_status == 3:
        status = "En curso"
    else:
        print("Ingrese solo las opciones indicadas!.")
    students[index][4][course]["estado"] = status
    
def select_course_assign(index):
    e = 0
    
    for i in students[index][4]:
        e = e+1
        print(str(e)+"-"+i['curso'])
    course = int(input("Seleccione el curso que desea: "))
    #course = students[index][4][course-1]
    
    return (course-1)
mod_course_status("leiner")


            
                
           
                    
            
            

            
    
    
    
    
            

    
     
        
        
        

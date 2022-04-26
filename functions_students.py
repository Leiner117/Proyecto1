import functions_admins
from control_dates import shedule

from datetime import datetime,time
students = []


def register (): 
    auxlist = []
    courses = []
    activities = {}
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
    auxlist.append(activities)
    students.append(auxlist)
    print("Te has registrado con exito!!! ")
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
    aux_dic["Estado"] = "En curso"
    students[index][4].append(aux_dic)
    load_shedule(index,functions_admins.courses[select-1][0])
    print("El curso se matriculo con exito!.")
    print(students[index][5])
def load_shedule(index,course):
    copy_shedule = shedule
    for i in copy_shedule:
        if course == i:
            students[index][5] = copy_shedule[i]
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
        students[index][4][course]["Estado"] = status
        mod_status(index,status)
    elif num_status == 2:
        status = "Reprobado"
        students[index][4][course]["Estado"] = status
        mod_status(index,status)
    elif num_status == 3:
        status = "En curso"
        students[index][4][course]["Estado"] = status
        mod_status(index,status,course)
    else:
        print("Ingrese solo las opciones indicadas!.")
        
def mod_status(index,status,course):
    course = students[index][4][course-1]
    for i in students[index][5]:
        if students[index][5][i]["curso"] == course:
            students[index][5][i]["Estado"] = status
    
    
def select_course_assign(index):
    e = 0
    
    for i in students[index][4]:
        e = e+1
        print(str(e)+"-"+i['curso'])
    course = int(input("Seleccione el curso que desea: "))
    #course = students[index][4][course-1]
    
    return (course-1)

def add_activities(name):
    activity = {}
    index = index_student(name)
    description = str(input("Ingrese la descripcion de la actividad: "))
    print("La actividad esta asociada a un curso?\n1.Si\n2.No")
    opselect = int(input("-->"))
    if opselect == 1:
        course = course_activities(index)
    elif opselect == 2:
        course = "Recreacion"
    start_date = input("fecha de la actividad'aaaa/mm/dd': ")
   
    try:
        start_date = datetime.strptime(start_date, '%Y/%m/%d')
    except ValueError:
        print("\n No ha ingresado una fecha correcta...")
        add_activities()
    start_time = input("Ingrese la hora de inicio de la actividad: ")
    start_time = datetime.strptime(start_time, '%H:%M').strftime('%H:%M')
    end_time = input("Ingrese la hora de conclusion de la actividad: ")
    end_time = datetime.strptime(end_time, '%H:%M').strftime('%H:%M')
    result = compare_date(index,start_date,start_time,end_time)
    if result == True:
        auxdic = {}
        auxdic["descripcion"] = description
        auxdic["curso"] = course
        auxdic["Fecha"] = start_date
        auxdic["Hora inicio"] = start_time
        auxdic["Hora conclusion"] = end_time
        auxdic["Estado"] = "En curso"
        students[index][5][start_date] = auxdic
        print("La actividad se agrego con exito")
    else:
        print("Tienes un choque en tu horario, no puedes agregar esta actividad.")
def status_activity():
    
    print("Seleccione estado de la actividad: \n1.En curso\n2.Ejecutada ")
    opselect = int(input("-->"))
    if opselect == 1:
        status = "En curso"
    elif opselect == 2:
        status = "Ejecutada"
    else:
        print("Seleccione solo las opciones indicadas!.")
        status_activity()
    return status
def compare_date(index,date,start_time,end_time):
    result = True
    for i in students[index][5]:
        if i == date:
            if students[index][5][date]["Estado"] == "En curso":
               if ((students[index][5][date]["Hora inicio"] > end_time or start_time > students[index][5][date]["Hora conclusion"])):
                   result = True# ya existe la fecha y no tiene problemas con los demas horarios
               else:
                   result = False# tiene choque de horario
                   break
            else:
               result = True #la fecha esta registrada pero los actividades ya se ejecutaron
        else:
            result = True # La fecha no esta registrada
    return result

def course_activities(index):
    e = 0
    
    for i in students[index][4]:
        e = e+1
        if i['Estado'] == "En curso":
            print(str(e)+"-"+i['curso'])
    course = int(input("Seleccione el curso que desea: "))
    return (course-1)
def print_activities(name):
    index = index_student(name)
    students[index][5]
    cont = 0
    for i in students[index][5]:
        if "descripcion" in students[index][5][i]:
            cont = cont+1
            print(str(cont)+"-"+str(students[index][5][i]["descripcion"])+" Estado: "+str(students[index][5][i]["Estado"]))

def mod_status_activities(name):
    print("Actividades:")
    index = index_student(name)
    students[index][5]
    cont = 0
    for i in students[index][5]:
        if "descripcion" in students[index][5][i]:
            cont = cont+1
            print("->"+str(students[index][5][i]["descripcion"])+" Estado: "+str(students[index][5][i]["Estado"]))
    opselect = (input("Ingrese la actividad que desea modificar:"))
    select = index_act(opselect,index)
    status = status_activity()
    students[index][5][select]["Estado"] = status
    print("El estado de la actividad se cambio exitosamente!.")
def index_act(select,index):
    for i in students[index][5]:
        if "descripcion" in students[index][5][i]:
            if select == students[index][5][i]["descripcion"]:
                return i 
            

    



            
            

            
    
    
    
    
            

    
     
        
        
        

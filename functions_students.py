import functions_admins
from control_dates import shedule
import os
from datetime import datetime,time
students = []#Almacena todos los estudiantes


def register (): 
    '''
    Registra estudiantes en una lista, ingresando los datos solicitados 
    Se utiliza una lista indexadas para almacenar los estudiantes 
    '''
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
    '''
    Recibe como parametro el nombre del estudiante que quiere cambiar la carrera
    Se llama a una funcion para elegir la nueva carrera
    Se selecciona la nueva carrrera
    se realiza el cambio en la lista indexada
    '''
    new_career = functions_admins.select_position_careers()
    new_career = functions_admins.careers[new_career]
    for i in students:
        if name in i:
            i[2] = new_career
            break
            
def assign_course(name):
    '''
    Se recorre la lista de estudiantes para obtener el indice del estudiante que desea realizar la matricula
    se imprime la lista de cursos que estan disponibles en la carrera del estudiante
    se utiliza un diccionario para almacenar los datos 
    se llama una funcion para asignar los dias de clases del curso matriculado
    '''
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
    
    
def load_shedule(index,course):
    '''
    Se genera la lista de fechas que hay clases asignadas en el curso matriculado
    se le asigna al estudiante en su diccionario de actividades 
    '''
    copy_shedule = shedule
    for i in copy_shedule:
        if course == i:
            students[index][5] = copy_shedule[i]
            
def index_student(name):
    '''
    recorre la lista de estudiante para obtener el indice del nombre indicado
    '''
    for i in students:
        if name in i:
            index = students.index(i)
    return index

def mod_course_status(name):
    '''
    Solicita el indice del estudiante
    Solicita el curso matriculado que desea cambiar el estado
    realiza el cambio en la lista indexada de estudiantes y en el diccionario de actividades
    
    '''
    index = index_student(name)
    status = ""
    course = select_course_assign(index)
    print("1.Aprobado\n2.Reprobado\n3.En curso")
    num_status = int(input("Ingrese el estado del curso: "))
    if num_status == 1:
        status = "Aprobado"
        students[index][4][course]["Estado"] = status
        mod_status(index,status,course)
    elif num_status == 2:
        status = "Reprobado"
        students[index][4][course]["Estado"] = status
        mod_status(index,status,course)
    elif num_status == 3:
        status = "En curso"
        students[index][4][course]["Estado"] = status
        mod_status(index,status,course)
    else:
        print("Ingrese solo las opciones indicadas!.")
        
def mod_status(index,status,course):
    '''
    modifica el estado del curso en el diccionario de actividades
    '''
    course = students[index][4][course-1]
    for i in students[index][5]:
        if students[index][5][i]["curso"] == course:
            students[index][5][i]["Estado"] = status
    
    
def select_course_assign(index):
    '''
    Imprime los cursos matriculados de un estudiante
    '''
    e = 0
    
    for i in students[index][4]:
        e = e+1
        print(str(e)+"-"+i['curso'])
    course = int(input("Seleccione el curso que desea: "))
    #course = students[index][4][course-1]
    
    return (course-1)

def add_activities(name):
    '''
    Se genera el indice del estudiante 
    Se solicita la informacion de la actividad
    se compara las fechas y horas para evitar choques con otras actividades
    se utiliza un diccionario indexado para almacenar las actividades
    '''
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
    '''
    Selecciona el estado de la actividad 
    '''
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
    '''
    recorre el diccionario indexado de actividades
    compara las fechas con la fecha que se quiere agregar
    compara el estado la actividad almacenada para averiguar si tiene algun choque
    se comparan las horas de la actividad para evitar choques de horarios
    se retorna un True o False dependiendo de si hay o no choque
    
    '''
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
    '''
    Imprime la lista de cursos matriculados y en curso para asociar alguna actividad
    '''
    e = 0
    
    for i in students[index][4]:
        e = e+1
        if i['Estado'] == "En curso":
            print(str(e)+"-"+i['curso'])
    course = int(input("Seleccione el curso que desea: "))
    return (course-1)

def print_activities(name):
    '''
    genera el indice del estudiante 
    recorre el diccionario indexado de actividades
    por medio de una caracteristica de las activdades ingresadas por el estudiante se realiza un filtro de las clases
    se imprime el nombre de la actividad y el estado 
    
    '''
    index = index_student(name)
    cont = 0
    os.system ("cls")
    print("Actividades: ")
    for i in students[index][5]:
        if "descripcion" in students[index][5][i]:
            cont = cont+1
            print(str(cont)+"-"+str(students[index][5][i]["descripcion"])+" Estado: "+str(students[index][5][i]["Estado"]))

def mod_status_activities(name):
    '''
    imprime la lista de actividades
    selecciona la actividad que desea
    se genera el indice de la actividad
    se realiza el cambio en el diccionario de actividades
    '''
    print("Actividades:")
    index = index_student(name)
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
    '''
    Recorre el diccionario de actividades y retorna la clave del valor que se ingreso
    '''
    for i in students[index][5]:
        if "descripcion" in students[index][5][i]:
            if select == students[index][5][i]["descripcion"]:
                return i 
            

    



            
            

            
    
    
    
    
            

    
     
        
        
        

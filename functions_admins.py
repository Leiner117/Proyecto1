from datetime import datetime,time
import control_dates
admins = [["admin","12345",123]]
courses = tuple()
careers = tuple()
week = {1:"LUNES",2:"MARTES",3:"MIERCOLES",4:"JUEVES",5:"VIERNES",6:"SABADO",7:"DOMINGO"}

def add_admins():
    ''' Agrega administradoreas a la lista, guardando los datos solicitados en una lista anidada'''
    aux_list = []
    name = input("Ingrese su nombre completo: ")
    password = input("Ingrese una contraseña: ")
    phone_number = int(input("Ingrese su numero de telefono: "))
    aux_list.append(name)
    aux_list.append(password)
    aux_list.append(phone_number)
    admins.append(aux_list)
    

def add_courses():
    if len(careers) > 0:
        num_courses = int(input("Ingrese la cantidad de cursos que desea agregar: "))
        i = 0
        global courses
        courses = list(courses)
        while num_courses > i:
            aux_list = []
            course = input("Ingrese el nombre del nuevo curso: ")
            credit = int(input("Ingrese la cantidad de creditos del curso: "))
            school_hours = credit*3
            start_date = input("fecha de inicio del curso'aaaa/mm/dd': ")
            end_date = input("fecha de finalización del curso'aaaa/mm/dd': ") 
            
            try:
                start_date = datetime.strptime(start_date, '%Y/%m/%d').strftime('%Y/%m/%d')
                end_date = datetime.strptime(end_date, '%Y/%m/%d').strftime('%Y/%m/%d')
            except ValueError:
                print("\n No ha ingresado una fecha correcta...")
            class_times = class_time()
            careers_belongs = select_career()
            aux_list.append(course)
            aux_list.append(credit)
            aux_list.append(school_hours)
            aux_list.append(start_date)
            aux_list.append(end_date)
            aux_list.append(class_times)
            aux_list.append(careers_belongs)
            courses.append(aux_list)
            aux_list.clear
            i = i +1
            print("El curso se agrego con exito!.")
        control_dates.load_dates(courses)
        print(control_dates.shedule)
        courses = tuple(courses)
        
    else:
        print("No se pueden registrar cursos si no existen carreras.")
        
def class_time():
    aux_list = []
    school_days = int(input("Ingrese la cantidad de dias a la semana que se importen lecciones: "))
    i = 0
    while i < school_days:
        aux_dic = {}
        day = select_day()
        start_time = input("Ingrese la hora de inicio de la clase: ")
        start_time = datetime.strptime(start_time, '%H:%M').strftime('%H:%M')
        end_time = input("Ingrese la hora de finalizacion de la clase: ")
        end_time = datetime.strptime(end_time, '%H:%M').strftime('%H:%M')
        aux_dic["dia"] = day
        aux_dic["inicio"] = start_time
        aux_dic["final"] = end_time
        aux_list.append(aux_dic)
        i = i+1
    return aux_list
        

def select_day():
    a = 0
    for i in week:
        a = a+1
        print(str(a)+"-"+week[i])
    select = int(input("Ingrese el dia que desea registrar: "))
    return [select-1]


def add_careers():
    global careers
    careers = list(careers)
    career = input("Ingrese el nombre de la carrera que desea agregar: ")
    careers.append(career)
    careers = tuple(careers)
    print("La carrera se agrego con exito!.")

def select_career():
    global careers
    careers_list = []
    b = 0
    while b == 0:
        print("Seleccione las carrera que desea:")
        a = 1
        for i in careers:
            print(str(a)+"-"+i)
            a = a+1
        select = int(input("---->"))
        if select > len(careers):
            print("La carrera seleccionada no existe")
            select_career()
        else:
            careers_list.append(careers[select-1])
            print("Desea asociar mas carreras a este curso?:")
            print("1. Si\n2. No")
            opselect = int(input("---> "))
            if opselect == 2:
                b = 1
                return careers_list



def select_course():
    global courses
    
    print("Seleccione el curso que desea:")
    a = 1
    e = 0
    for i in courses:
        print(str(a)+"-"+courses[e][0])
        a = a+1
        e = e+1
    select = int(input("---->"))
    if select > len(courses):
        print("El curso seleccionado no existe.")
        select_course()
    else:
        return (select-1)
def select_position_careers():
    global careers
    print("Seleccione la carrera que desea que desea:")
    a = 1
    for i in careers:
        print(str(a)+"-"+i)
        a = a+1
    select = int(input("---->"))
    if select > len(careers):
        print("El curso seleccionado no existe.")
        select_position_careers()
    else:
        return (select-1)

def mod_courses():
    course = select_course()
    while True:
        print("1. Nombre de curso\n2. creditos\n3. fecha de inicio\n4. fecha de finalizacion\n5. Horario\n6.carreras asociadas\n7.Salir")
        opselect = int(input("Ingrese la opcion que desea: "))
        if opselect == 1:
            mod_nameCourse(course)
                
        elif opselect == 2:
            mod_credits(course)
        elif opselect == 3:
            mod_start_date(course)
        elif opselect == 4:
            mod_end_date(course)
        elif opselect == 5:
            mod_class_times(course)
        elif opselect == 6:
            mod_careers(course)
        elif opselect == 7:
            break
def mod_nameCourse(course):
    global courses
    new_name = input("Ingrese el nuevo nombre del curso: ")
    courses = list(courses)
    courses[course][0] = new_name
    courses = tuple(courses)
def mod_credits(course):
    global courses
    courses = list(courses)
    new_credits = int(input("Ingrese la nueva cantidad de creditos: "))
    new_school_hours = new_credits*3
    courses[course][1] = new_credits
    courses[course][2] = new_school_hours
    courses = tuple(courses)
def mod_start_date(course):
    global courses
    courses = list(courses)
    start_date = input("fecha de inicio del curso'aaaa/mm/dd': ")
    try:
        start_date = datetime.strptime(start_date, '%Y/%m/%d').strftime('%Y/%m/%d')
        courses[course][3] = start_date
        courses = tuple(courses)
    except ValueError:
        print("\n No ha ingresado una fecha correcta...")
        mod_courses()
    
def mod_end_date(course):
    global courses
    courses = list(courses)
    end_date = input("fecha de finalización del curso'aaaa/mm/dd': ") 
    try:
        end_date = datetime.strptime(end_date, '%Y/%m/%d').strftime('%Y/%m/%d')
    except ValueError:
        print("\n No ha ingresado una fecha correcta...")
        mod_courses()
    courses[course][4] = end_date
    courses = tuple(courses)
def mod_class_times(course):
    global courses
    courses = list(courses)
    new_class_times = class_time()
    courses[course][5] = new_class_times
    courses = tuple(courses)
def mod_careers(course):
    global courses
    courses = list(courses)
    new_careers = select_career()
    courses[course][6] = new_careers
    courses = tuple(courses)
def mod_careers():
    career = select_position_careers
    new_careers = input("Ingrese el nuevo nombre de la carrera: ")
    careers[career] = new_careers
    

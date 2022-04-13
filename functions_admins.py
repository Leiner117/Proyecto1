from datetime import datetime,time
admins = []
courses = tuple()
careers = tuple()
def add_admins():
    aux_list = []
    name = input("Ingrese su nombre completo: ")
    phone_number = int(input("Ingrese su numero de telefono: "))
    aux_list.append(name)
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
            ''' Verificar '''
            try:
                start_date = datetime.strptime(start_date, '%Y/%m/%d').strftime('%Y/%m/%d')
                end_date = datetime.strptime(end_date, '%Y/%m/%d').strftime('%Y/%m/%d')
            except ValueError:
                print("\n No ha ingresado una fecha correcta...")
            class_times = input("Ingrese el horario de clases: ")
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
        courses = tuple(courses)
    else:
        print("No se pueden registrar cursos si no existen carreras.")



def add_careers():
    global careers
    careers = list(careers)
    career = input("Ingrese el nombre de la carrera que desea agregar: ")
    careers.append(career)
    careers = tuple(careers)

def select_career():
    global careers
    print("Seleccione la carrera que desea:")
    a = 1
    for i in careers:
        print(str(a)+"-"+i)
        a = a+1
    select = int(input("---->"))
    if select > len(careers):
        print("La carrera seleccionada no existe")
        select_career()
    else:
        return careers[select-1]
def mod_courses():
    global courses
    courses = list(courses)
    
    print("1. Modificar datos\n2. Eliminar curso")
    opselect = int(input("---> "))
    if opselect ==1:
        mod_data()
    elif opselect == 2:
        print()
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
        return courses[select-1][0]

    
            
def mod_data():
    course = select_course()
    print("1. Nombre de curso\n2. creditos\n3. fecha de inicio\n4. fecha de finalizacion\n5. Horario\n6.carrera asociada")
    opselect = int(input("Ingrese la opcion que desea: "))
    if opselect == 1:
        print()
    elif opselect == 2:
        print()
    elif opselect == 3:
        print()
    elif opselect == 4:
        print()
    elif opselect == 5:
        print()
    elif opselect == 6:
        print()

import functions_admins
import functions_students
def login():
    while True:
        print("1. Login\n2. Registro\n3. salir")
        opselect = int(input("Seleccione la opcion que desea: "))
        if (opselect == 1):
            verify_login()
        elif (opselect == 2):
            register()
        elif (opselect == 3):
            break
def verify_login():
    name = input("Ingrese su nombre: ")
    password = input("Ingrese su contraseña: ")
    rank = select_rank()
    flag = False
    if rank == "Administrativo":
        for i in functions_admins.admins:
            if name == i[0] and password == i[1]:
                flag = True
                menu_admins(i[0])
                break
        if flag == False:
            print("El usuario o la contraseña son incorrectos")
    elif rank == "Estudiante":
        for a in functions_students.students:
            if name == a[0] and password == a[3]:
                menu_students(a[0])
                break
        if flag == False:
            print("El usuario o la contraseña son incorrectos")
def select_rank():
    print("Selecciona tu rango:\n1.Administrativo\n2.Estudiante")
    rank = int(input("---> "))
    if rank == 1:
        rank = str("Administrativo")
    elif rank == 2:
        rank = str("Estudiante")
    else: 
        print("Ingresa alguna de las opciones indicadas!.")
        select_rank()
    return rank

def register():
    print("Desea registrarse como:\n1. Estudiante\n2. Salir")
    opselect = int(input("--->"))
    if (opselect == 1):
        functions_students.register()
        login()
    elif (opselect == 2):
        login()
    
def menu_admins(name):
    
    while True:
        print("Menú de administradores")
        print("1. Agregar cursos\n2. Modificar cursos\n3. Agregar carreras\n4. Modificar carreras\n5. Salir")
        opselect = int(input("Ingrese la opcion que desea: "))
        if (opselect == 1):
            functions_admins.add_courses()
        elif (opselect == 2):
            functions_admins.mod_courses()
        elif (opselect == 3):
            functions_admins.add_careers()
        elif (opselect == 4):
            functions_admins.mod_careers()
        elif (opselect == 5):
            break
        elif (opselect == 6):
            print(functions_admins.courses)
            print(functions_admins.careers)
            print(functions_admins.admins)
        
def menu_students(name):
    
    while True:
        print("Menú de estudiantes")
        print("1.Cambiar Carrera\n2.Matricular cursos\n3.agregar actividades\n4.modificar estado de un curso\n5.Salir")
        opselect = int(input("Ingrese la opcion que desea: "))
        if (opselect == 1):
            functions_students.mod_careers(name)
        elif (opselect == 2):
            functions_students.assign_course(name)
        elif (opselect == 3):
            print()
        elif (opselect == 4):
            functions_students.mod_course_status(name)
login()

    

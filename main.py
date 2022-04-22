import functions_admins
import functions_students
def login():
    while True:
        print("1. Login\n2. Registro\n3. salir\n4. menu admin")
        opselect = int(input("Seleccione la opcion que desea: "))
        if (opselect == 1):
            menu_students()
        elif (opselect == 2):
            register()
        elif (opselect == 3):
            break
        elif (opselect == 4):
            menu_admins()
 
def register():
    print("Desea registrarse como: \n1. Administrativo\n2. Estudiante")
    opselect = int(input("--->"))
    if (opselect == 1):
        functions_admins.add_admins()
        login()
    elif (opselect == 2):
        functions_students.register()
        login()
def menu_admins():
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
            print(functions_admins.courses)
            print(functions_admins.careers)
            print(functions_admins.admins)
        elif (opselect == 6):
            break
        
def menu_students():
    while True:
        print("Menú de estudiantes")
        print("1. asignar cursos \n2. \n3. Agregar carreras\n4. Modificar carreras")
        opselect = int(input("Ingrese la opcion que desea: "))
        if (opselect == 1):
            functions_students.assign_course("leiner")
        elif (opselect == 2):
            functions_admins.mod_courses()
        elif (opselect == 3):
            functions_admins.add_careers()
        elif (opselect == 4):
            print()
menu_admins()

    

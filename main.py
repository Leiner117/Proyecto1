import functions_admins
def login():
    while True:
        print("1. Login\n2. Registro\n3. salir")
        opselect = int(input("Seleccione la opcion que desea: "))
        if (opselect == 1):
            print()
        elif (opselect == 2):
            register()
        elif (opselect == 3):
            break
            
def register():
    print("Desea registrarse como: \n1. Administrativo\n2. Estudiante")
    opselect = int(input("--->"))
    if (opselect == 1):
        functions_admins.add_admins
        login()
    elif (opselect == 2):
        print()
def menu_admins():
    print("Menú de administradores")
    print("1. Agregar cursos\n2. Modificar cursos\n3. Agregar carreras\n4. Modificar carreras")
    opselect = int(input("Ingrese la opcion que desea: "))
    if (opselect == 1):
        functions_admins.add_courses
    elif (opselect == 2):
        functions_admins.mod_courses
    elif (opselect == 3):
        functions_admins.add_careers
    elif (opselect == 4):
        print()

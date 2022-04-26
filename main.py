
import functions_admins
import functions_students
import reports
from datetime import datetime
import os
def login():
    while True:
        print("1. Login\n2. Registro\n3. salir")
        opselect = int(input("Seleccione la opcion que desea: "))
        if (opselect == 1):
            os.system ("cls")
            verify_login()
        elif (opselect == 2):
            os.system ("cls")
            register()
        elif (opselect == 3):
            break
def verify_login():
    os.system ("cls")
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
    os.system ("cls")
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
    os.system ("cls")
    print("Desea registrarse como:\n1. Estudiante\n2. Salir")
    opselect = int(input("--->"))
    if (opselect == 1):
        functions_students.register()
        login()
    elif (opselect == 2):
        login()
    
def menu_admins(name):
    os.system ("cls")
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
            print(functions_students.students)
        
def menu_students(name):
    os.system ("cls")
    while True:
        print("Menú de estudiantes")
        print("1.Cambiar Carrera\n2.Matricular cursos\n3.Agregar actividades\n4.Modificar estado de un curso\n5.Actividades\n6.Modificar actividades\n7.Reportes\n8.Salir")
        opselect = int(input("Ingrese la opcion que desea: "))
        if (opselect == 1):
            functions_students.mod_careers(name)
        elif (opselect == 2):
            functions_students.assign_course(name)
        elif (opselect == 3):
            functions_students.add_activities(name)
        elif (opselect == 4):
            functions_students.mod_course_status(name)
        elif (opselect == 5):
            functions_students.print_activities(name)
        elif (opselect == 6):
            functions_students.mod_status_activities(name)
        elif (opselect == 7):
            menu_reports(name)
        elif (opselect == 8):
            break
def menu_reports(name):
    os.system ("cls")
    while True:
        print("Menu Reportes")
        print("1.Reporte de actividades\n2.Porcentaje de tiempo\n3.Reporte de tiempo\n4.Salir")
        opselect = int(input("Ingrese la opcion que desea: "))
        if opselect == 1:
            menu_printactivities(name)
        elif opselect == 2:
            print("en proceso")
        elif opselect == 3:
            print("en proceso")
        elif opselect == 4:
            break
def menu_printactivities(name):
    os.system ("cls")
    date = input("Ingrese la fecha exacta del dia que desea consultar: ")
    date = datetime.strptime(date, '%Y/%m/%d')
    reports.print_activities(name,date)
login()

    

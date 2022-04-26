import functions_students
from datetime import datetime
def print_activities(name,date):
    '''
    recorre el diccionario de actividades
    verifica que las fechas sean iguales
    imprime la informacion de la fecha 
    '''
    index = functions_students.index_student(name)
    for i in functions_students.students[index][5]:
        if functions_students.students[index][5][i]["Fecha"] == date:
            if "descripcion" in functions_students.students[index][5][i]:
                print("Día:"+str(functions_students.students[index][5][i]["Fecha"]))
                print("Actividad:"+functions_students.students[index][5][i]["descripcion"])
                print("Hora de inicio:"+functions_students.students[index][5][i]["Hora inicio"])
                print("Hora de conclusion:"+functions_students.students[index][5][i]["Hora conclusion"])
                print("Curso asociado:"+str(functions_students.students[index][5][i]["curso"]))
                print("Total de tiempo:"+str(datetime.strptime(functions_students.students[index][5][i]["Hora conclusion"], '%H:%M')-datetime.strptime(functions_students.students[index][5][i]["Hora inicio"], '%H:%M')))
                break
                

    
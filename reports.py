import functions_students
def print_activities(name,date):
    index = functions_students.index_student(name)
    for i in functions_students.students[index][5]:
        if functions_students.students[index][5][i]["Fecha"] == date:
            if "descripcion" in functions_students.students[index][5][i]:
                print("Día:"+str(functions_students.students[index][5][i]["Fecha"]))
                print("Actividad:"+functions_students.students[index][5][i]["Descripcion"])
                print("Hora de inicio:"+functions_students.students[index][5][i]["Hora inicio"])
                print("Hora de conclusion:"+functions_students.students[index][5][i]["Hora conclusion"])
                print("Curso asociado:"+functions_students.students[index][5][i]["curso"])
                print("Total de tiempo:"+(functions_students.students[index][5][i]["Hora inicio"]-functions_students.students[index][5][i]["Hora conclusion"]))
                
                
        
    
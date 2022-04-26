
from datetime import date, datetime,time
import calendar
#schedule = {"curso":[{datetime.datetime(2022, 3, 2, 0, 0): {'curso': 'estudiar','Fecha': datetime.datetime(2022, 3, 2, 0, 0), 'Hora inicio': '09:00', 'Hora conclusion': '11:00'}}],"course:":[]}

shedule = {}
def load_dates(course):
    '''
    -Recorre la lista de cursos
    -agrega los datos necesarios para generar las fechas
    -llama una funcion al tener todos los datos necesarios
    '''
    global shedule
    shedule.clear
    for i in course:
        name_course = i[0]
        list_hours = select_hours(i)
        start_date = i[3]
        end_date = i[4]
        start_date = datetime.strptime(start_date,'%Y/%m/%d')
        end_date = datetime.strptime(end_date,'%Y/%m/%d')
        list_days = select_days(i)
        difference_month = difference_months(start_date,end_date)
        total_weeks,months = gen_weeks(start_date,difference_month)
        list_dates = gen_dates(start_date,total_weeks,months,list_days,end_date)
        add_dates(list_dates,list_days,name_course,list_hours)
def difference_months(start_date,end_date):
    '''
    Genera la diferencia de meses entre 2 fechas
    '''
    difference = end_date.month-start_date.month
    return difference
def gen_weeks(start_date,difference):
    '''
    Se crea un ciclo donde compara un contador con la diferencia de meses entre las fechas
    se almacenan todos los meses en una lista
    se generan todas las semanas de un mes indicado utilizando una libreria
    las semanas se almacenan en un diccionario asignando de clave el mes que pertenecen las semanas
    este diccionario se almacena en una lista
    retorna la lista con todas las semanas y la lista con todos los meses
    '''
    total_weeks = []
    start_month = start_date.month
    i = 0
    months = []
    while difference > i:
        months.append(start_month)
        auxdic = {}
        weeks = calendar.monthcalendar(start_date.year,start_month)
        auxdic[start_month] = weeks
        total_weeks.append(auxdic)
        i = i+1
        start_month = start_month+1
    return total_weeks,months
def gen_dates(start_date,total_weeks,months,list_days,end_date):
    '''
    recorre la lista de semanas
    recorre la lista de semanas de cada mes 
    recorre la lista de dias de la semana asignados cuando se creo el curso
    se hace una comparacion para filtrar los dias de la semana necesarios
    las semanas con los dias necesarios se almacenan en una lista 
    se recorre la lista 
    se asigna el año/mes/dia a la fecha y se convierte en un objeto fecha
    las fechas se almacenan en una lista y se retornan
    '''
    dates = []
    auxlist1 = []
    b = 0  
    
    for i in total_weeks:
        auxmonths = []
        for a in i[months[b]]:
            for n in list_days:
                day = n[0]
                if a[day] > 0:
                    auxmonths.append(a[day])
        auxlist1.append(auxmonths)
        b = b+1
    

    e = 0
    ano = start_date.year
    for c in auxlist1:
        auxlist2 = []
        for h in c:
            date = str(ano)+"/"+str(months[e])+"/"+str(h)
            date1 = datetime.strptime(date,'%Y/%m/%d')
            if date1 <= end_date:
                auxlist2.append(date)
        dates.append(auxlist2)
        e = e+1
    return dates

def select_days(i):
    '''
    recorre la lista de dias asignados a los cursos
    guarda los dias en una lista y la retorna
    '''
    list_days = []
    for a in i[5]:
        list_days.append(a["dia"])
    return list_days
def select_hours(i):
    '''
    recorre la lista 
    almacena las horas en un diccionario y el diccionario en una lista y la retorna
    
    '''
    list_hours = []
    for a in i[5]:
        aux_dic = {}
        dic_hours = {}
        day = a["dia"][0]
        dic_hours["inicio"] = a["inicio"]
        dic_hours["final"] = a["final"]
        aux_dic[day] = dic_hours
        list_hours.append(aux_dic)
    return list_hours
def add_dates(list_dates,list_days,name,list_hours):
    '''
    recorre la lista de fechas
    convierte cada fecha en un objeto fecha
    asigna los datos necesarios para almacenar el dia con una actividad
    almacena todos los datos en un diccionario 
    el diccionario se almacena en un diccionario indexado
    '''
    auxdic = {}
    for i in list_dates:
        for a in i:
            auxdic2 = {}
            date = datetime.strptime(a,'%Y/%m/%d')
            auxdic2["curso"] = name
            auxdic2["Fecha"] = date
            auxdic2["Hora inicio"] = select_starthour(date,list_hours)
            auxdic2["Hora conclusion"] = select_endhour(date,list_hours)
            auxdic2["Estado"] = "En curso"
            auxdic[date] = auxdic2
    shedule[name] = auxdic
            
def select_starthour(date,list_hours):
    '''
    Recorre la lista de horas
    selecciona la hora correspondiente al dia 
    '''
    day = datetime.weekday(date)
    for i in list_hours:
        if day in i:
            start_hour = i[day]["inicio"]
            start_hour = datetime.strptime(start_hour, '%H:%M').strftime('%H:%M')
            break
    return start_hour
def select_endhour(date,list_hours):
    '''
    Recorre la lista de horas
    selecciona la hora correspondiente al dia 
    '''
    day = datetime.weekday(date)
    for i in list_hours:
        if day in i:
            end_hour = i[day]["final"]
            end_hour = datetime.strptime(end_hour, '%H:%M').strftime('%H:%M')
            break
    return end_hour

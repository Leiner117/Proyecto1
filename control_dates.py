import functions_admins
from datetime import date, datetime,time
import calendar
#schedule = {"curso":[{datetime.datetime(2022, 3, 2, 0, 0): {'curso': 'estudiar','Fecha': datetime.datetime(2022, 3, 2, 0, 0), 'Hora inicio': '09:00', 'Hora conclusion': '11:00'}}],"course:":[]}
course = functions_admins.courses
shedule = {}
def load_dates():
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
    difference = end_date.month-start_date.month
    return difference
def gen_weeks(start_date,difference):
    total_weeks = []
    start_month = start_date.month
    i = 0
    months = []
    while difference > i:
        months.append(start_month)
        auxlist = {}
        weeks = calendar.monthcalendar(start_date.year,start_month)
        auxlist[start_month] = weeks
        total_weeks.append(auxlist)
        i = i+1
        start_month = start_month+1
    return total_weeks,months
def gen_dates(start_date,total_weeks,months,list_days,end_date):
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
    list_days = []
    for a in i[5]:
        list_days.append(a["dia"])
    return list_days
def select_hours(i):
    
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
    auxlist = []
    for i in list_dates:
        auxdic = {}
        for a in i:
            auxdic2 = {}
            date = datetime.strptime(a,'%Y/%m/%d')
            auxdic2["curso"] = name
            auxdic2["Hora inicio"] = select_starthour(date,list_hours)
            auxdic2["Hora conclusion"] = select_endhour(date,list_hours)
            auxdic[date] = auxdic2
        auxlist.append(auxdic)
    shedule[name] = auxlist
            
def select_starthour(date,list_hours):
    day = datetime.weekday(date)
    for i in list_hours:
        if day in i:
            start_hour = i[day]["inicio"]
            start_hour = datetime.strptime(start_hour, '%H:%M').strftime('%H:%M')
            break
    return start_hour
def select_endhour(date,list_hours):
    day = datetime.weekday(date)
    for i in list_hours:
        if day in i:
            end_hour = i[day]["final"]
            end_hour = datetime.strptime(end_hour, '%H:%M').strftime('%H:%M')
            break
    return end_hour


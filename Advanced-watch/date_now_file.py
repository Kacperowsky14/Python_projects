import datetime

def date_now():
    date = datetime.datetime.now()
    month_now = date.strftime("%m")
    if month_now== "01":
        month = "Jan."
    if month_now== "02":
        month = "Feb."
    if month_now== "03":
        month = "Mar."
    if month_now== "04":
        month = "Apr."
    if month_now== "05":  
        month = "May"
    if month_now== "06":
        month = "Jun."
    if month_now== "07":
        month = "Jul."
    if month_now== "08":
        month = "Aug."
    if month_now== "09":
        month = "Sep."
    if month_now== "10":
        month = "Oct."
    if month_now== "11":
        month = "Nov."
    if month_now== "12":
        month = "Dec."
    return month

import datetime

def date_in_future(value):
    """Функция которая показывает дату через введное количество дней."""
    
    your_time = datetime.datetime.now() #Получаю текущую дату

    #Если это целое число
    if type(value) == int:
        your_time = your_time + datetime.timedelta(days = value) #Дата равна текущему значению дате + введое число дней 

        your_time = your_time.strftime("%d-%m-%Y %H:%M:%S") #Форматирование значения в '01-01-2001 22:33:44"
        return your_time
    
    else:
        your_time = your_time.strftime("%d-%m-%Y %H:%M:%S")
        return your_time
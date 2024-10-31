import datetime

def date_in_future(value):
    """Функция которая показывает дату через введное количество дней."""
    
    your_time = datetime.datetime.now() #Получаю текущую дату

    #Если это целое число
    if type(value) == int:
        your_time = your_time + datetime.timedelta(days = value) #Дата равна текущему значению дате + введое число дней 

        your_time = your_time.strftime("%d-%m-%Y %H:%M:%S") #Форматирование значения в '01-01-2001 22:33:44"
        print(your_time)
    
    else:
        your_time = your_time.strftime("%d-%m-%Y %H:%M:%S")
        print(your_time)

#Примеры которые должны проверять task_xx.py
date_in_future([]) # => текущая дата
date_in_future(2) # => текущая дата + 2 дня
def connect_dicts(first_dict_values, second_dict_values):
    """Функция которая объединяет два введеных словаря в один."""

    print_dict_values = {} #Новый словарь для вывода 

    #Перебирает ключи и слова в первом словаре
    for key, value in first_dict_values.items():
        #Если ключи есть во втором словаре
        if key in second_dict_values:
            #Если их значение больше 10
            if value > 10 :
                #Если сумма 1 словаря больше 2
                if sum(first_dict_values.values()) > sum(second_dict_values.values()):
                    print_dict_values[key] = first_dict_values[key] #Добавит значение из 1 словаря

                #Или же 1 словарь меньше 2 
                elif sum(first_dict_values.values()) < sum(second_dict_values.values()):
                    print_dict_values[key] = second_dict_values[key] #Добавит значение из 2 словаря

                #В ином случае когда они равны (приоритет)
                else:
                    print_dict_values[key] = second_dict_values[key] #Добавит значение из 2 словаря

        #Если ключа нет
        else:
            #Если значение больше 10
            if value > 10 :
                print_dict_values[key] = value #Добавит значение с таким ключом

    #Перебирает второй словарь
    for key, value in second_dict_values.items():
        #Если ключа нет в первом словаре
        if key not in first_dict_values:
            #Если значение больше 10
            if value > 10 :
                print_dict_values[key] = value #Добавит значение с таким ключом
    
    #Сортирует словарь используя значения из кортежа 
    print_dict_values = dict(sorted(print_dict_values.items(), key=lambda nums: nums[1]))

    return print_dict_values #Возвращает 
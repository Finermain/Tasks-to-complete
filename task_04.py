def sort_list(values):
    """Функция которая поменяет местами минимальные и максимальные элементы массива, добавит в конец массива минимальное значение из него."""
    
    #Блок проверки - на пустые значения или ошибки
    try:
        min_num = values[0] #Объявление минимального по 1 элементу
        max_num = values[0] #Объявление максимального по 1 элементу

        #Перебирает массив элементов
        for el in values:
            #Если элемент меньше
            if min_num > el:
                min_num = el #То минимальное равно элементу

            #Если элемент больше
            if max_num < el:
                max_num = el #То максимальное равно элементу
        
        #Перебираем массив элементов и индексов по enumerate
        for i, el in enumerate(values):
            #Если элемент равен максимальному
            if el == max_num:
                values[i] = min_num #То приравниваем значение к минимальному

                continue #И пропускаем итерацию

            #Если элемент равен минимальному
            if el == min_num:
                values[i] = max_num #То приравниваем значение к максимальному

                continue #И пропускаем итерацию

        values.append(min_num) #Добавляем минимальное значение в конец

        return values

    except:
        return values
def coincidence(*args):
    """Функция для определения элементов, значения которого входят в указанный диапазон."""
    
    answers = [] #Объявление массива
    
    #Всегда кроме передачи двух значений он возвращает пустой массив
    if len(args) == 1:
        return answers
        
    elif len(args) == 2:
        #Блок где при ошибках возвращает пустой массив
        try:
            #Перебираем list
            for num in args[0]:
                #Если значение число или число с плавающей точкой
                if type(num) is int or type(num) is float:
                    #Проверяет входит ли в диапозон 
                    if args[1][0] <= num <= args[1][-1]:
                        answers.append(num) #Добавляет значение в список
            
            return answers
            
        except:
            return answers
            
    else:
        return answers
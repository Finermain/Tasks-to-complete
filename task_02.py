def coincidence(*args):
    """Функция для определения элементов, значения которого входят в указанный диапазон."""
    
    answers = [] #Объявление массива
    
    #Всегда кроме передачи двух значений он возвращает пустой массив
    if len(args) == 1:
        print(answers)
        
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
            
            print(answers)
            
        except:
            print(answers)
            
    else:
        print(answers)
           
#Примеры которые должны проверять task_xx.py
coincidence([1, 2, 3, 4, 5], range(3, 6)) # => [3, 4, 5]
coincidence() # => []
coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4)) # => [1, 2, 2.5]
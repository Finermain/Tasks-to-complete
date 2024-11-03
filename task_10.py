import string 

def count_words(query_text: str):
    """Функция которая возвращает словарь c статистикой частоты употребления слов в предложении. """
    
    query_text = query_text.lower() #Делает текстовый запрос маленькой буквы

    #Проходим по константе знаков припинания и убираем их
    for punctuation in string.punctuation:
        query_text = query_text.replace(punctuation , "")

    query_text = query_text.replace("  " , " ")#Убирает излишние пробелы
    query_text = query_text.split(" ") #Разбивает текст по пробелу
    
    dict_words = {} #Инициализация словаря статистики
    #Перебирает текстовый запрос слов
    for word in query_text:
        #Если слово есть уже
        if word in dict_words:
            dict_words[word] += 1
        
        #Если слова нету
        else:
            dict_words[word] = 1
    
    return dict_words
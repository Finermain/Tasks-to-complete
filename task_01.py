import string

def is_palindrome(request):
    """Функция is_palindrome принимает значение и проверяет палиндроммность."""
    
    request = str(request) #Переводит любой тип данных в слово

    request = request.lower() #Делает слово с маленькой буквы

    #Проходим по константе знаков припинания и убираем их
    for punctuation in string.punctuation:
        request = request.replace(punctuation , "")

    request = request.replace(" " , "") #Убирает пробелы

    i = 0
    j = len(request) - 1
    request_palindrome = True #Переменная в цикле для проверки слова
    while i < j:
        if request[i] != request[j]: #Если символ от конца и от начала не совпадают 
            request_palindrome = False #Он будет отмечать что это не палиндром

        i += 1
        j -= 1

    #Проверяет результат после цикла и выводит
    if request_palindrome:
        print(True)
        
    else:
        print(False)

#Примеры которые должны проверять task_xx.py
is_palindrome("A man, a plan, a canal -- Panama") # => True
is_palindrome("Madam, I'm Adam!") # => True
is_palindrome(333) # => True
is_palindrome(None) # => False
is_palindrome("Abracadabra") # => False
def combine_anagrams(values):
    """Функция которая принимает на вход массив слов и разбивает их в группы по анаграммам."""
    
    anagram_words = {} #Слова анаграммы

    #Блок перебирает слова в массиве значений
    for word in values:
        anagram_key = sorted(word.lower()) #Создаст массив отсартированных букв, регистр не имеет значения 

        anagram_key = "".join(anagram_key) #Объединит их в одно слово - ключ

        #Если такой ключ есть
        if anagram_key in anagram_words:
            anagram_words[anagram_key].append(word) #Добавит слово
        
        #Если такого ключа нет
        else:
            anagram_words[anagram_key] = [word] #Создаст слово и ключ

    print_message = [] #Инициализация переменны чтоб вывод был похож на то что в примере вывода
    #Перебирает массивы в вложеном массиве 
    for mas in anagram_words:
        print_message.append(anagram_words[mas]) #Добавляет массив в переменную массива

    print(print_message) #TODO: Если вывод должен быть идентичным вашему, переделаю.

#Примеры которые должны проверять task_xx.py
combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar", "creams", "scream"]) # => [ ["cars", "racs", "scar"], ["four"], ["for"], ["potatoes"], ["creams", "scream"] ]
def multiply_numbers(value = None):
    """Функция которая  который вернет произведение цифр, входящих в inputs."""
    
    total_product = None #Изначально произведение равно

    value = str(value) #Перевод значения в строку
    
    #В блоке строка осуществляет поиск по буквам
    for letter in value:
        #Если буква - явл. цифрой
        if letter.isdigit():
            #Если произведение изначально равно
            if total_product == None:
                total_product = int(letter) #То тогда присвоется 1 эл.
                
            else:        
                total_product = total_product * int(letter) #В другом случае умножится эл. на предыдущее

    return total_product #Возвращает 
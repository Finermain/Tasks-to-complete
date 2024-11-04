class Dessert:
    """Класс описания десерта."""

    NOT_HEALTHY_CALORIES = 200 #Константа отметки калорий 

    def __init__(self, name="Вкусность", calories="100"):
        """Конструктор класса принимающий атрибуты name, calories."""

        self.__name = name

        self.__calories = calories

    @property
    def name(self):
        """Получение имени."""

        return self.__name

    @name.setter
    def name(self, name):
        """Установка значения имени."""

        self.__name = name

    @property
    def calories(self):
        """Получение кол-во калорий."""

        return self.__calories

    @calories.setter
    def calories(self, calories):
        """Установка количества калорий."""

        self.__calories = str(calories)

    def is_healthy(self):
        """Функция проверяет на то ,считается ли десерт здоровым для употребления."""

        #Блок проверки
        try:
            calories = int(self.__calories) #Если написано число словом то переводит

            #Если калорийность меньше константы
            if calories < self.NOT_HEALTHY_CALORIES:
                return True #Вернет правду
            
            else:
                return False #Либо ложь 
   
        #Блок исключения
        except ValueError:
            return str(False) + " - калорийность измеряется в числах. Не полезные слова :("
        
    def is_delicious(self):
        """Функция возвращает true всем десертам."""
        return True
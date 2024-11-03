class Dessert:
    """Класс описания десерта."""

    NOT_HEALTHY_CALORIES = 200 #Константа отметки калорий 

    def __init__(self, name="Вкусность", calories=100):
        """Конструктор класса принимающий атрибуты name, calories."""

        #Проверка на строку
        if type(name) != str:
            self.__name = "Вкусность"

        else:
            self.__name = name

        #Проверка на число и число с плавающей точкой
        if not isinstance(calories, (int, float)):
            self.__calories = 100

        else:
            self.__calories = calories

    @property
    def name(self):
        """Получение имени."""

        return self.__name

    @name.setter
    def name(self, name):
        """Установка значения имени."""

        #Проверка на строку
        if type(name) == str:
            self.__name = name

        else:
            print("Некоректное имя.")

    @property
    def calories(self):
        """Получение кол-во калорий."""

        return self.__calories

    @calories.setter
    def calories(self, calories):
        """Установка количества калорий."""

        #Проверка на число и число с плавающей точкой
        if isinstance(calories, (int, float)):
            self.__calories = calories

        else:
            print("Неправильный формат количества калорий.")

    def is_healthy(self):
        """Функция проверяет на то ,считается ли десерт здоровым для употребления."""

        #Если кол-во калорий меньше чем максимально допустимое
        if self.__calories < self.NOT_HEALTHY_CALORIES:
            return True
        
        else:
            return False

    def is_delicious(self):
        """Функция возвращает true всем десертам."""
        return True
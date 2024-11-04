from task_11 import Dessert 

class JellyBean (Dessert):
    """Клаасс для описания мармеладных бобов."""

    def __init__(self, flavor = "Мультифрукт", name = "Бобы", calories = "10"):
        """Конструктор принимающий параметры вкуса, имени и калорий."""

        super().__init__(name , calories) #Инициализация атрибутов из родителя
        
        self.__flavor = flavor
    
    @property
    def flavor(self):
        """Получение вкуса."""

        return self.__flavor
    
    @flavor.setter
    def flavor(self, flavor):
        """Установление вкуса."""

        self.__flavor = str(flavor)

    def is_delicious(self):
        """Функция проверяет на то,вкусный ли мармелад, если он равен черной лакрице то невкусный."""

        #Если вкус равен черной лакрице
        if self.__flavor.lower() == "black licorice":
            return False
        
        else:
            return True
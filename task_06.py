#Класс наследующий класс исключения - для вызова ошибок
class NoSuchStrategyError(Exception):
    """Класс проверяет на ход игроков отличительный от R, P и S."""

    pass

#Класс наследующий класс исключения - для вызова ошибок
class WrongNumberOfPlayersError(Exception):
    """Класс проверяет на количество игроков , должно быть не больше 2."""

    pass

def who_win(values):
    """Функция определяет кто победитель где P - бумага, S - ножницы, R - камень."""

    player_choice = [values[0][1], values[1][1]] #Сохранит выбор игрока в массив

    #Вложенный словарь "Игра" , возвращет игрока который победит 
    game = {
        "P": {"P": values[0], "S": values[1], "R": values[0]},
        "S": {"P": values[1], "S": values[0], "R": values[1]},  
        "R": {"P": values[1], "S": values[0], "R": values[0]},  
    }

    #Возвращает нужный мне формат строки выбрав из game[Предмет].get(Предмет) и => Выведет победителя
    return remake_winer(game[player_choice[0]].get(player_choice[1]))

def remake_winer(word):
    """Функция форматирует в текст похожий на 'player2 S' вывод из примера."""

    word = word[0] + " " + word[1]  #Слово будет как в примере => player2 S

    return word

def exception_choice(values):
     """Функция исключение проверяет на ход игроков отличительный от R, P и S."""

     #Перебираю массив значений
     for mas in values:
        #Перебираю массив игроков с индексом
        for i, player in enumerate(mas):
            #Если это второй элемент масссива игрока
            if i == 1:
                #Если он не равен этит трем значениям
                if player not in ['P', 'S', 'R']:
                    raise NoSuchStrategyError("Ход игроков не должен быть отличительный от R, P и S.") #Выведет ошибку в основном блоке исключений
     
def exception_players(values):
        """Функция проверяет на количество игроков , должно быть не больше 2."""

        #Если длина не равна 2
        if len(values) != 2:
            raise WrongNumberOfPlayersError("Количество игроков , должно быть не больше 2.") #Выведет ошибку в основном блоке исключений

def rps_game_winner(values):
        """Основной метод - функция которая отвечает за логику программы Камень-Ножницы-Бумага."""
        
        #Блок проверки исключений      
        try:
            exception_players(values) #Проверяет не присутсвует ли игроков больше 2

            exception_choice(values) #Проверяет на стандартный выбор предметов в игре

            return who_win(values) #Возвращает победителя

        #Блок исключения 
        except WrongNumberOfPlayersError as e:
            raise e #Теперь оно выводит не текст вызваной ошибки,а вызыванную ошибку

        #Блок исключения 
        except NoSuchStrategyError as e:
            raise e #Теперь оно выводит не текст вызваной ошибки,а вызыванную ошибку
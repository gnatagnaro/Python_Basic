# если честно, то не понимаю, как можно сделать прям игру "Крестики-нолики", поэтому
# можно, пожалуйста, пример подобной программы, но с полным функционалом, если это вообще
# нужно

class Cell:
    #  Клетка, у которой есть значения
    #   - занята она или нет
    #   - номер клетки
    def __init__(self, number):
        self.number = number
        self.occupied = False


class Board:
    #  Класс поля, который создаёт у себя экземпляры клетки
    def __init__(self, count):
        self.cells = [Cell(num) for num in range(count)]


class Player:
    #  У игрока может быть
    #   - имя
    #   - на какую клетку ходит
    def __init__(self, name):
        self.name = name

    def goto_cell(self, num, desk):
        if not desk.cells[num].occupied:
            desk.cells[num].occupied = True
            return f'Клетка {num} занята игроком {self.name}'
        else:
            return f'Клетка {num} уже занята!'


lenn = 9
board = Board(lenn)
player1 = Player('Том')
player2 = Player('Фред')
for i in range(lenn):
    if i % 2 == 0:
        print(player1.goto_cell(i, board))
        # print(player2.goto_cell(i, board))
    else:
        print(player2.goto_cell(i, board))
        # print(player1.goto_cell(i, board))


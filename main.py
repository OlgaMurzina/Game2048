# v2_classic branch
import random

import pygame

FPS = 1


class Board:
    def __init__(self, width, height, scr):
        """
        конструктор объекта Доска
        :param width: ширина доски в кол-ве клеток
        :param height: высота доски в кол-ве клеток
        :param scr: холст из основной программы
        """
        self.width = width
        self.height = height
        self.screen = scr
        # игровая таблица числовых значений каждой клетки
        self.board = [[0] * width for _ in range(height)]
        # список пустых клеток
        self.empty_cells = list(range(16))
        # позиция верхнего левого угла картинки по умолчанию
        self.left = 10
        self.top = 10
        # размер клетки по умолчанию
        self.cell_size = 150
        # цвет фона клетки - ключ int, цвет цифры в клетке - ключ char
        self.colorit = {0: (205, 193, 180), 2: (238, 228, 218), 4: (238, 225, 201), 8: (243, 178, 122),
                        16: (246, 150, 100), 32: (247, 124, 95), 64: (247, 98, 60), 128: (237, 208, 115),
                        256: (237, 204, 98), 512: (237, 201, 80), 1024: (238, 198, 66), 2048: (237, 194, 46),
                        '8': (249, 246, 242),
                        '4': (119, 110, 101)}
        # цвет границы
        self.border = (187, 173, 160)
        # счет игры - за каждый ход прибавляет значение в изменившейся клетке
        self.score = 0
        # рабочие значения поля игры
        """self.board[2][2] = 2
        self.board[2][3] = 2048
        self.board[0][1] = 1024
        self.board[3][2] = 8
        self.board[3][0] = 4"""

    def render(self, screen):
        """
        :param screen: холст + глобальный параметр board с изменениями в значениях
        :return: прорисовка графической оболочки с закрашиванием нужных клеток
        """
        color = self.border
        for y in range(self.height):
            for x in range(self.width):
                color_cell = self.colorit[self.board[x][y]]
                # прорисовка фона клеток
                pygame.draw.rect(screen, color_cell, (
                    x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                    self.cell_size))
                # прорисовка границ клеток
                pygame.draw.rect(screen, pygame.Color(color), (
                    x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                    self.cell_size), 20)
                # прорисовка цифр в непустых клетках
                self.view_num(x, y, color_cell)
                if self.board[x][y] == 2048:
                    pygame.draw.rect(screen, pygame.Color('white'), (
                        x * self.cell_size + self.left + 10, y * self.cell_size + self.top + 10, self.cell_size - 22,
                        self.cell_size - 22), 2)

    def view_num(self, xx, yy, col_cell):
        """
        :param xx: координата х клетки
        :param yy: координата у клетки
        :param col_cell: цвет фона клетки
        :return: вывод цифры на экран в нужной клетке игрового поля
        """
        # назначение цвета цифры
        color_num = col_cell
        if 0 < self.board[xx][yy] <= 4:
            color_num = self.colorit['4']
        elif self.board[xx][yy] >= 8:
            color_num = self.colorit['8']
        # смещение цифр относительно верхнего угла клетки
        dy = 45
        dim = 100
        if self.board[xx][yy] < 16:
            dx = 56
        elif 15 < self.board[xx][yy] < 100:
            dx = 38
        elif 100 < self.board[xx][yy] < 1000:
            dx = 15
        else:
            dx = 14
            dy = 50
            dim = 75
        # экран для вывода цифры
        im = pygame.Surface((50, 50))
        im.set_colorkey(col_cell)
        # назначение шрифта
        basicFont = pygame.font.SysFont(None, dim)
        # настройка текста
        text = basicFont.render(str(self.board[xx][yy]), True, color_num, col_cell)
        text_area = im.get_rect().move(xx * self.cell_size + self.left + dx, yy * self.cell_size + self.top + dy)
        # нанесение текста на поверхность
        self.screen.blit(text, text_area)

    def set_view(self, left, top, cell_size):
        """
        :param left: левая позиция игрового поля окна
        :param top: верхняя позиция игрового поля окна
        :param cell_size: размер клетки игрового поля окна
        :return: установка стартовых параметров от пользователя (предусмотрен режим /по умолчанию
        """
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def event_mouse(self):
        """if event.pos[0] not in range(board.left, board.left + board.width * board.cell_size) or \
                                event.pos[1] not in range(board.top, board.top + board.height * board.cell_size):
                            pass
                        else:
                            row, col = (event.pos[1] - board.top) // board.cell_size, (
                                        event.pos[0] - board.left) // board.cell_size
                            if board.board[col][row] == 0:
                                board.board[col][row] = 1
                            elif board.board[col][row] == 1:
                                board.board[col][row] = 0
                            for y in range(board.height):
                                if y == row:
                                    for x in range(board.width):
                                        if board.board[x][y] == 0:
                                            board.board[x][y] = 1
                                        elif board.board[x][y] == 1:
                                            board.board[x][y] = 0
                            for x in range(board.width):
                                if x == col:
                                    for y in range(board.height):
                                        if board.board[x][y] == 0:
                                            board.board[x][y] = 1
                                        elif board.board[x][y] == 1:
                                            board.board[x][y] = 0"""
        pass

    def event_k_left(self):
        self.board_new(-1)

    def event_k_right(self):
        self.board_new(1)

    def event_k_up(self):
        self.board_new(2)

    def event_k_down(self):
        self.board_new(-2)

    def new_values(self):
        """
        :return: новый элемент на пустом пространстве доски
        """
        n = random.choice(self.empty_cells)
        self.empty_cells.remove(n)
        x1 = n // 4
        y1 = n % 4
        val = random.choice([2, 4])
        self.board[x1][y1] = val

    def new_gen(self, i):
        """
        генерирует новые значения на доске при каждом ходе
        :param i: очередность вызова: 2 - первый раз - генерирует 2 значения, 1 - все остальные вызовы и генерация 1 значения
        :return: возвращает доску с учетом новых значений
        """
        for j in range(i):
            self.new_values()

    def board_new(self, k):
        """
        создает новую ситуацию на доске после поступления сигнала от игрока в слот
        :param k: код смещения (-1 - нажата кнопка влево, 1 - нажата кнопка вправо,
                                -2 - нажата кнопка вниз, 2 - нажата кнопка вверх)
        :return: обновление состояния доски после получения слотом сигнала
        """
        pass


def main():
    pygame.init()
    size = 620, 620
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('2048')

    board = Board(4, 4, screen)
    board.set_view(10, 10, (size[0] - 20) // 4)
    # генерирует два новых числа 2 или 4 на произвольных пустых местах в таблице
    board.new_gen(2)
    clock = pygame.time.Clock()
    running = True
    while running:
        # задержка
        clock.tick(FPS)

        # цикл обработки событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT or not board.empty_cells:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.event_mouse()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    board.event_k_left()
                elif event.key == pygame.K_RIGHT:
                    board.event_k_right()
                elif event.key == pygame.K_UP:
                    board.event_k_up()
                elif event.key == pygame.K_DOWN:
                    board.event_k_down()
                # генерирует новое число 2 или 4 на пустом месте
                board.new_gen(1)

        # изменение объектов
        screen.fill((205, 193, 180))

        board.render(screen)
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()

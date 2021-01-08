# v2_classic branch
import pygame

FPS = 60


class Board:
    def __init__(self, width, height, scr):
        """
        конструктор объекта Доска
        :param width: ширина доски в кол-ве клеток
        :param height: высота доски в кол-ве клеток
        """
        self.width = width
        self.height = height
        self.screen = scr
        # таблица числовых значений каждой клетки
        self.board = [[0] * width for _ in range(height)]
        # позиция верхнего левого угла картинки по умолчанию
        self.left = 10
        self.top = 10
        # размер клетки по умолчанию
        self.cell_size = 150
        # цвет фона клетки - ключ int, цвет цифры в клетке - ключ char
        self.colorit = {0: (205, 193, 180), 2: (238, 228, 218), 4: (238, 225, 201), 8: (243, 178, 122),
                        16: (246, 150, 100), 32: (247, 124, 95), 64: (247, 98, 60), 128: (237, 208, 115),
                        256: (237, 204, 98), 512: (237, 201, 80), 1024: (238, 198, 66), '8': (249, 246, 242),
                        '4': (119, 110, 101)}
        # цвет границы
        self.border = (187, 173, 160)
        # счет игры - за каждый ход прибавляет значение в изменившейся клетке
        self.score = 0
        self.board[1][2] = 1024
        self.board[2][3] = 2
        self.board[0][0] = 256
        self.board[3][2] = 8
        self.board[3][0] = 4

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
            dx = 11
            dim = 80
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

    def board_new(self):
        """ обновление состояния доски после получения слотом сигнала"""
        pass

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
        pass

    def event_k_right(self):
        pass

    def event_k_up(self):
        pass

    def event_k_down(self):
        pass

    def new_values(self):
        pass


def main():
    pygame.init()
    size = 620, 620
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('2048')

    board = Board(4, 4, screen)
    board.set_view(10, 10, (size[0] - 20) // 4)
    clock = pygame.time.Clock()
    running = True
    while running:
        # задержка
        clock.tick(FPS)

        # цикл обработки событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
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

        # изменение объектов
        screen.fill((205, 193, 180))
        # новое случайное [2, 4] значение на пустом месте поля
        board.new_values()
        board.render(screen)
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()

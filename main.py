# v2_classic branch
import pygame

FPS = 60

class Board:
    def __init__(self, width, height):
        # конструктор объекта Доска
        self.width = width
        self.height = height
        # таблица значений каждой клетки
        self.board = [[0] * width for _ in range(height)]
        # позиция верхнего левого угла картинки
        self.left = 10
        self.top = 10
        # размер клетки
        self.cell_size = 50
        # цвет фона клетки - ключ int, цвет цифры в клетке - ключ char
        self.colorit = {0: (205, 193, 180), 2: (238, 228, 218), 4: (238, 225, 201), 8: (243, 178, 122),
                        16: (246, 150, 100), 32: (247, 124, 95), 64: (247, 98, 60), 128: (237, 208, 115),
                        256: (237, 204, 98), 512: (237, 201, 80), 1024: (238, 198, 66)}
        # цвет границы
        self.border = (187,173,160)
        # счет игры - за каждый ход прибавляет значение в изменившейся клетке
        self.score = 0
        self.board[1][2] = 2

    def render(self, screen):
        # значения рабочей таблицы
        color = self.border
        for y in range(self.height):
            for x in range(self.width):
                color_cell = self.colorit[self.board[x][y]]
                if self.board[x][y] == 0:
                    pygame.draw.rect(screen, pygame.Color(color), (
                        x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                        self.cell_size), 20)
                elif self.board[x][y] == 2:
                    pygame.draw.rect(screen, color_cell, (
                        x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                        self.cell_size))
                    pygame.draw.rect(screen, pygame.Color(color), (
                        x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                        self.cell_size), 20)
                elif self.board[x][y] == 4:
                    pygame.draw.rect(screen, color_cell, (
                        x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                        self.cell_size))
                    pygame.draw.rect(screen, pygame.Color(color), (
                        x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                        self.cell_size), 20)
                elif self.board[x][y] == 8:
                    pygame.draw.rect(screen, color_cell, (
                        x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                        self.cell_size))
                    pygame.draw.rect(screen, pygame.Color(color), (
                        x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                        self.cell_size), 20)
                elif self.board[x][y] == 16:
                    pygame.draw.rect(screen, color_cell, (
                        x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                        self.cell_size))
                    pygame.draw.rect(screen, pygame.Color(color), (
                        x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                        self.cell_size), 20)
                elif self.board[x][y] == 32:
                    pygame.draw.rect(screen, color_cell, (
                        x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                        self.cell_size))
                    pygame.draw.rect(screen, pygame.Color(color), (
                        x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                        self.cell_size), 20)
                elif self.board[x][y] == 64:
                    pygame.draw.rect(screen, color_cell, (
                        x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                        self.cell_size))
                    pygame.draw.rect(screen, pygame.Color(color), (
                        x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                        self.cell_size), 20)
                elif self.board[x][y] == 128:
                    pygame.draw.rect(screen, color_cell, (
                        x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                        self.cell_size))
                    pygame.draw.rect(screen, pygame.Color(color), (
                        x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                        self.cell_size), 20)
                elif self.board[x][y] == 256:
                    pygame.draw.rect(screen, color_cell, (
                        x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                        self.cell_size))
                    pygame.draw.rect(screen, pygame.Color(color), (
                        x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                        self.cell_size), 20)
                elif self.board[x][y] == 512:
                    pygame.draw.rect(screen, color_cell, (
                        x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                        self.cell_size))
                    pygame.draw.rect(screen, pygame.Color(color), (
                        x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                        self.cell_size), 20)
                elif self.board[x][y] == 1024:
                    pygame.draw.rect(screen, color_cell, (
                        x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                        self.cell_size))
                    pygame.draw.rect(screen, pygame.Color(color), (
                        x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                        self.cell_size), 20)
                elif self.board[x][y] == 2048:
                    pygame.draw.rect(screen, color_cell, (
                        x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                        self.cell_size))
                    pygame.draw.rect(screen, pygame.Color(color), (
                        x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                        self.cell_size), 20)

    def set_view(self, left, top, cell_size):
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

    board = Board(4, 4)
    board.set_view(10, 10, 150)
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

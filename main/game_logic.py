from main.grid import Grid
import random


class minesweeper_game:
    def __init__(self, y: int, x: int, mines: int):
        self.y = y
        self.x = x
        self.mines = mines
        self.reveal_count = (y * x) - mines
        self.board = Grid(self.y, self.x)
        self.first_click = True

    def initialise_game(self, click_y, click_x):

        planting_mines = self.mines

        while planting_mines > 0:
            if planting_mines >= self.x * self.y:
                planting_mines = 0
                print("Invalid mines number. 0 mines have been planted.")
            rand_x = random.randint(0, self.x - 1)
            rand_y = random.randint(0, self.y - 1)
            if rand_x == click_x and rand_y == click_y:
                continue
            if self.board.grid[rand_y][rand_x].isbomb is False:
                self.board.grid[rand_y][rand_x].isbomb = True
                planting_mines += -1

        for y in range(self.board.height):
            for x in range(self.board.width):
                self.board.grid[y][x].counter = self.board.calculate_adjacent(self.board.grid[y][x])


def print_game_state(board):
    for y in range(board.height):
        line = []
        for x in range(board.width):
            if board.grid[y][x].isreveal is True:
                if board.grid[y][x].isbomb is True:
                    line.append("X")
                else:
                    line.append(str(board.grid[y][x].counter))
            else:
                line.append("-")
        print(line)

from grid import Grid
import random


class minesweeper_game:
    def __init__(self, y: int, x: int, mines: int):
        self.y = y
        self.x = x
        self.mines = mines
        self.reveal_count = (y * x) - mines
        self.board = self.initialise_game()

    def initialise_game(self):

        board = Grid(self.y, self.x)
        planting_mines = self.mines

        while planting_mines > 0:

            rand_x = random.randint(0, self.x - 1)
            rand_y = random.randint(0, self.y - 1)

            if board.grid[rand_y][rand_x].isbomb is False:
                board.grid[rand_y][rand_x].isbomb = True
                planting_mines += -1

        for y in range(board.height):
            for x in range(board.width):
                board.grid[y][x].counter = board.calculate_adjacent(board.grid[y][x])

        return board


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

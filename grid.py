from square import Square
from collections import deque


class Grid:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.grid = self.create_grid(height, width)
        self.adjacent = [
            (1, 0),
            (1, 1),
            (0, 1),
            (-1, 1),
            (-1, 0),
            (-1, -1),
            (0, -1),
            (1, -1),
        ]

    def create_grid(self, height, width):
        result = []
        for y in range(height):
            row = []
            for x in range(width):
                row.append(Square((y, x)))
            result.append(row)
        return result

    def calculate_adjacent(self, case):
        count = 0
        for adj in self.adjacent:
            visiting_height = case.pos[0] + adj[0]
            visiting_width = case.pos[1] + adj[1]
            if (
                visiting_height >= 0
                and visiting_width >= 0
                and visiting_width < self.width
                and visiting_height < self.height
            ):
                if self.grid[case.pos[0] + adj[0]][case.pos[1] + adj[1]].isbomb == True:
                    count += 1
        return count

    def reveal(self, square):
        counter = 0
        visited = set()
        queue = deque()
        queue.append(square.pos)
        while queue:
            current = queue[0]
            for adj in self.adjacent:
                visit_y = current[0] + adj[0]
                visit_x = current[1] + adj[1]
                if (visit_y, visit_x) in visited:
                    continue
                visited.add((visit_y, visit_x))

                if (
                    visit_y >= 0
                    and visit_x >= 0
                    and visit_x < self.width
                    and visit_y < self.height
                ):
                    if self.grid[visit_y][visit_x].isbomb == False:
                        if self.grid[visit_y][visit_x].isreveal == False:
                            self.grid[visit_y][visit_x].isreveal = True
                            counter += 1
                        if self.grid[visit_y][visit_x].counter == 0:
                            queue.append((visit_y, visit_x))
            queue.popleft()
        return counter

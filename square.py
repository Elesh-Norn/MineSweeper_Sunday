class Square:
    def __init__(self, pos):

        self.pos = pos
        self.isbomb = False
        self.isreveal = False
        self.counter = 0
        self.ismarked = False

    def mark(self):
        if self.ismarked is False:
            self.ismarked = True
        else:
            self.ismarked = False

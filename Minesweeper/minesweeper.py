class MinesweeperGame:
    def __init__(self, mines, x, y):
        self.mines = mines
        self.x = x
        self.y = y
        if x*y <= mines:
            raise ValueError("Too many mines for the field")


    def plot_grid(mines, x, y):
        pass

game = MinesweeperGame(5, 10, 10)
print(game.mines)
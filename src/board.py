class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

if __name__ == "__main__":
    b = Board(9, 9)
    print(b.rows, b.cols)

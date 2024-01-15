class ROW:
    def __init__(self, t):
        self.cells = t

    def new(cls, t):
        return cls(cells=t)
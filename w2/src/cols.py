from num import NUM
from sym import SYM

class COLS:
    """
    A contrainer storing multiple ‘NUM‘s and ‘SYM‘s.
    Create a set of columns from a set of strings. If uppercase
    then ‘NUM‘, else ‘SYM‘. ‘Klass‘es end in ‘!‘. Numeric goals to
    minimize of maximize end in ‘−‘,‘+‘. Keep all cols in ‘all‘.
    Also add dependent columns to ‘y‘ (anthing ending in ‘−‘,‘+‘,‘!‘) and
    independent columns in ‘x‘ (skipping over anyhing ending in ‘X‘).
    """
    def __init__(self, row):
        self.x = {}
        self.y = {}
        self.all = []
        self.klass = None
        self.col = None
        self.names = row.cells

        for at, txt in enumerate(row.cells):
            self.col = NUM(txt, at) if txt.startswith("A−Z") else SYM(txt, at)
            self.all.append(self.col)
            if not txt.endswith("X"):
                if txt.endswith("!"):
                    self.klass = self.col

                if txt.endswith(("!", "+", "−")):
                    self.y[at] = self.col
                else:
                    self.x[at] = self.col

    def add(self, row):
        for cols in [self.x, self.y]:
            for col in cols.values():
                col.add(row[col.at])
        return row

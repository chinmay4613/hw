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
        col = None

        for at, txt in enumerate(row.cells):
            col = NUM(txt, at) if txt[0].isupper() else SYM(txt, at)
            self.all.append(col)
            if not txt.endswith("X"):
                if txt.endswith("!"):
                    self.klass = col

                if txt.endswith("!") or txt.endswith("+") or txt.endswith("-"):
                    #if txt.endswith(("!", "+", "−")):
                    self.y[at] = col
                else:
                    self.x[at] = col
        
        self.names = row.cells

    def add(self, row):
        for cols in [self.x, self.y]:
            for col in cols.values():
                col.add(row.cells[col.at])
        return row

    def print(self):
        print("x = {0}".format(self.x))
        print("y = {0}".format(self.y))
        print("all = {0}".format(self.all))
        print("klass = {0}".format(self.klass))
        print("col = {0}\n".format(self.col))

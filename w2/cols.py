class COLS:
    def __init__(self, row):
        self.x = {}
        self.y = {}
        self.all = []
        self.klass = None
        self.names = row

        for at, txt in enumerate(row):
            col = (NUM if txt[0].isupper() else SYM)(txt, at)
            self.all.append(col)
            if not txt.endswith("X"):
                if txt.endswith(("!","-","+")):
                    self.y[at] = col
                self.x[at] = col

    def add(self, row):
        for cols in [self.x, self.y]:
            for col in cols.values():
                col.add(row[col.at])
        return row

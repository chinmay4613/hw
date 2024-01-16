from cols import COLS
from row import ROW
import utils

class DATA:
    def __init__(self, src, fun=None):
        self.rows = []
        self.cols = None
        if isinstance(src, str):
            for line_count, x in utils.csv(src):
                self.add(x, fun)
        else:
            if not src:
                src = []
            for x in src:
                self.add(x, fun)

    def add(self, t, fun=None):
        row = t.cells if t else ROW(t)
        if self.cols:
            if fun:
                fun(self, row)
            self.rows.append(self.cols.add(row))
        else:
            self.cols = COLS(row)

    def mid(self, cols=None):
        u = []
        for col in (cols if cols else self.cols.all):
            u.append(col.mid())
        return ROW(u)

    def div(self, cols=None):
        u = []
        for col in (cols if cols else self.cols.all):
            u.append(col.div())
        return ROW(u)

    def small(self):
        u = []
        for col in self.cols.all:
            u.append(col.small())
        return ROW(u)

    def stats(self, cols=None, fun=None, ndivs=2):
        u = {".N": len(self.rows)}
        for col in self.cols[cols if cols else "y"]:
            method = getattr(col, fun if fun else "mid")
            u[col.txt] = utils.rnd(method(col), ndivs)
        return u

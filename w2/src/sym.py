import math

class SYM:
    def __init__(self, s=None, n=None):
        self.txt = s if s is not None else " "
        self.at = n if n is not None else 0
        self.n = 0
        self.has = {}
        self.mode = None
        self.most = 0

    def add(self, x):
        if x != "?":
            self.n += 1
            self.has[x] = 1 + self.has.get(x, 0)
            if self.has[x] > self.most:
                self.most, self.mode = self.has[x], x

    def mid(self, *args, **kwargs):
        return self.mode

    def div(self, e=0):
        e = 0
        for v in self.has.values():
            e = e - v / self.n * math.log(v / self.n, 2)
        return e

    def print(self):
        print("txt = {0}".format(self.txt))
        print("at = {0}".format(self.at))
        print("n = {0}".format(self.n))
        print("has = {0}".format(self.has))
        print("mode = {0}".format(self.mode))
        print("most = {0}\n".format(self.most))


    """
    # Currently not supported
    def small(self):
        return 0

    def like(self, x, prior):
        pass
    """

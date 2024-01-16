
class NUM:
    def __init__(self, s=None, n=None):
        self.txt = s if s is not None else " "
        self.at = n if n is not None else 0
        self.n = 0
        self.mu = 0
        self.m2 = 0
        self.hi = -1E30
        self.lo = 1E30
        if s and s.endswith("-"):
            self.heaven = 0
        else:
            self.heaven = 1

    def add(self, x):
        d = None
        if x != "?":
            self.n += 1
            d = x - self.mu
            self.mu += d / self.n
            self.m2 += d * (x - self.mu)
            self.lo = min(x, self.lo)
            self.hi = max(x, self.hi)

    def mid(self, *args, **kwargs):
        return self.mu

    def div(self, *args, **kwargs):
        return 0 if self.n < 2 else (self.m2 / (self.n - 1)) ** 0.5

    def norm(self, x):
        return x if x == "?" else (x - self.lo) / (self.hi - self.lo + 1E-30)

    def print(self):
        print("txt = {0}".format(self.txt))
        print("at = {0}".format(self.at))
        print("n = {0}".format(self.n))
        print("mu = {0}".format(self.mu))
        print("m2 = {0}".format(self.m2))
        print("hi = {0}".format(self.hi))
        print("lo = {0}".format(self.lo))
        print("heaven = {0}\n".format(self.heaven))


    """
    # Currently not supported
    def small(self):
        return the["cohen"] * self.div()

    def like(self, x, _):
        mu, sd = self.mid(), (self.div() + 1E-30)
        nom = 2.718 ** (-0.5 * (x - mu) ** 2 / (sd ** 2))
        denom = (sd * 2.5 + 1E-30)
        return nom / denom
    """

import re
import ast
import fileinput
import math

def oo(x):
    print(o(x))
    return x

def o(x):
    return x.__class__.__name__ + "{" + (" ".join([f":{k} {v}" for k, v in sorted(x.items()) if k[0] != "_"])) + "}"

def coerce(s):
    try:
        return ast.literal_eval(s)
    except Exception: 
        return s

def csv(file="-"):
    with fileinput.FileInput(None if file == "-" else file) as src:
        for line in src:
            line = re.sub(r'([\n\t\r"\' ]|#.*)', '', line)
            if line: 
                yield [coerce(x) for x in line.split(",")]

def rnd(n, ndecs):
    if not isinstance(n, float):
        return n
    if math.floor(n) == n:
        return n
    mult = 10 ** (ndecs if ndecs is not None else 2)
    return math.floor(n * mult + 0.5) / mult

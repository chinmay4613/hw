import re
import ast
import fileinput
import math
import sys

def oo(x):
    print(o(x))
    return x

def o(t, n=None):
    if isinstance(t, (int, float)):
        # Assuming l.rnd rounds the number. Python's round function can be used.
        return str(round(t, n))
    if not isinstance(t, dict):
        return str(t)
    
    u = []
    for k in t:
        # Check if key is a string and does not start with an underscore
        if isinstance(k, str) and not k.startswith("_"):
            if isinstance(t, list):
                u.append(o(t[k], n))
            else:
                # Assuming l.fmt is a string formatting function. Using Python's format method.
                u.append("{}: {}".format(o(k, n), o(t[k], n)))
    
    return "{" + ", ".join(u) + "}"

def coerce(s):
    try:
        return ast.literal_eval(s)
    except Exception: 
        return s

def csv(file="-"):
    with fileinput.FileInput(None if file == "-" else file) as src:
        for i, line in enumerate(src):
            line = re.sub(r'([\n\t\r"\' ]|#.*)', '', line)
            if line: 
                yield i + 1, [coerce(x) for x in line.split(",")]

def rnd(n, ndecs):
    return round(n, ndecs)
    """
    if not isinstance(n, (int, float)):
        return n
    if math.floor(n) == n:
        return n
    mult = 10 ** (ndecs if ndecs is not None else 2)
    return math.floor(n * mult + 0.5) / mult
    """

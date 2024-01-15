"""
mylo: to understand "it",  cut "it" up, then seek patterns in the pieces. E.g. here
we use cuts for multi- objective, semi- supervised, rule-based explanation.
(c) Tim Menzies <timm@ieee.org>, BSD-2 license

OPTIONS:
  -c --cohen  small effect size                 = .35
  -f --file   csv data file name                = "../data/diabetes.csv"
  -h --help   show help                         = false
  -k --k      low class frequency kludge        = 1
  -m --m      low attribute frequency kludge    = 2
  -s --seed   random number seed                = 31210
  -t --todo   start up action                   = help
"""

import re
from utils import coerce

def oo(x):
    print(o(x))
    return x

def o(x): 
    return x.__class__.__name__ + "{" + (" ".join([f":{k} {v}" for k, v in sorted(x.items()) if k[0] != "_"])) + "}"

"""
In this code, global settings are kept in `the` (which is parsed from `__doc__`).
This variable is a `slots`, which is a neat way to represent dictionaries that
allows easy slot access (e.g. `d.bins` instead of `d["bins"]`)
"""

class SLOTS(dict): 
    __getattr__ = dict.get; __setattr__ = dict.__setitem__; __repr__ = o

def get_default_config():
    the = SLOTS(**{m[1]: coerce(m[2]) for m in re.finditer(r"--(\w+)[^=]*=\s*(\S+)", __doc__)})
    return the


if __name__ == '__main__':
    # Only for testing
    the = get_default_config()
    the.k = 22
    the.k += 1
    print(the)

    print("the.cohen = {0}".format(the.cohen))
    print("the.file = {0}".format(the.file))
    print("the.help = {0}".format(the.help))
    print("the.k = {0}".format(the.k))
    print("the.m = {0}".format(the.m))
    print("the.seed = {0}".format(the.seed))
    print("the.todo = {0}".format(the.todo))

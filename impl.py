from datetime import *
import math
import sys
import inflect

def formula(x):
    return math.exp(20.3444*(x**3)+3) - math.exp(3)


# http://stackoverflow.com/a/20911144/1290530
def fromDecimal(start):
    year = int(start)
    rem = start - year

    base = datetime(year, 1, 1)
    result = base + timedelta(seconds=(base.replace(year=base.year + 1) -
        base).total_seconds() * rem)

    return result

class MyFormatter:

    def __contains__(self, item):
        return item == "{bar}"

    def split(self, item):
        if item == "{bar}":
            return '{desc}{percentage:3.0f}%|', RightFormat()

    def __str__(self):
        return self

class RightFormat:
    def format(self, **kwargs):
        return get_formatter(kwargs['percentage'] / 100)


def get_formatter(x):
    cur = datetime.now()
    past = formula(x)
    diff = cur.year - past
    p = inflect.engine()

    if diff > 0:
        return fromDecimal(diff).strftime("%B %Y")
    else:
        return p.number_to_words(int(round(past, 2-len(str(int(past)))))) + " years ago"

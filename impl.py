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


if __name__ == "__main__":
    cur = datetime.now()
    past = formula(float(sys.argv[1]))
    diff = cur.year - past
    p = inflect.engine()

    if diff > 0:
        print(fromDecimal(diff).strftime("%B %Y"))
    else:
        print(p.number_to_words(int(round(past, 3-len(str(int(past)))))), "years agp")

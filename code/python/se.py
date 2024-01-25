import math
import statistics

def se(x):
    out = statistics.stdev(x)/math.sqrt(len(x))
    return(out)

v = (1,3,5,6,2)
my_se = round(se(x = v),3)
print(my_se)
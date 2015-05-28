from math import acos
from math import pi
a=float(input())
b=float(input())
c=float(input())
cosC=(a**2+b**2-c**2)/(2*a*b)
arch=acos(cosC)
degree=arch*180/pi
print "%.1f"%degree

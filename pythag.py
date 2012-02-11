import math
SUM = 1000

for a in range(1, SUM/2):
  for b in range(a, int(math.ceil((SUM-a)/2))):
    c = SUM-a-b
    if a**2 + b**2 == c**2:
      print a*b*c, a, b, c

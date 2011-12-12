"""
This module, collatz.py, includes methods to work with the collatz or 3n+1
conjecture. It contains three functions: collatz, dictionary, and orbit. More
information is available in the docstrings of these fucntions.
"""

def collatz(n):
  "If n is even, return n/2. If n is odd, return 3n+1."
  if n%2:
    return 3*n+1
  else: 
    return n/2

def dictionary(maxval):
  """Returns a tuple: a dictionary of numbers 1 to maxval as keys and their
  orbits as values, and the key of the highest value."""
  dict = {1:0}
  highest = 1
  for i in range(1, maxval+1):
    j = i
    steps = 0
    while True: #rely on break to exit loop
      if j not in dict:
        j = collatz(j)
        steps += 1
      else:
        dict[i] = dict[j] + steps
        if dict[i] > dict[highest]:
          highest = i
        break
  return dict, highest

def orbit(n):
  "Returns the number of steps for n to converge to 1."
  steps = 0
  while(n > 1):
    n = collatz(n)
    steps += 1
  return steps

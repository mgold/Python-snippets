import math

def nthPrime(n):
  primes = [2]
  unchecked = 3
  while (len(primes) < n):
    couldBePrime = True
    threshold = math.ceil(math.sqrt(unchecked))
    for p in primes:
      if not unchecked%p: #if p divides unchecked
        couldBePrime = False #then it isn't prime
        break
      if p > threshold:
       break
    if couldBePrime:
      primes.append(unchecked)
    unchecked += 2
  return primes[n-1]

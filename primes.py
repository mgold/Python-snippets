"""
This module provides functions that work with prime numbers.

lessthan(max) and first(n) return sorted lists of all primes less than a cutoff.

check(n) returns True if n is prime, false otherwise.

filter(L) returns a list containing the elements of L that are prime.

factor(n) returns a sorted list of the prime factors of n. 


1 is not condsidered prime, and will never be in a returned list.

Unchecked runtime errors are documented in the docstrings for each function, but
essentially forbid passing non-positive or non-integer arguments.

"""

def check(n):
    """
    Returns True if n is prime, and False otherwise.
    
    U.R.E. for n to be non-positive or non-integer.
    """
    if filter([n]) == []:
        return False
    return True

def filter(L):
    """
    Return a list containing the elements of list L that are prime.
    
    U.R.E. for L not to be a list. U.R.E. for L to contain anything besides
    positive integers.
    """
    P = lessthan(int(max(L)**0.5)+1)
    F = []
    for l in L:
        if l > 1:
            for p in P:
                if not l%p and l!=p:
                    break
            else:
                F.append(l)
    return F 

def factor(n):
    """
    Returns a sorted list of the prime factors of n.

    If n is prime, [n] is returned. No list ever contains 1.
    
    U.R.E. for n to be less than 2 or non-integer.
    """
    L = []
    P = lessthan(int(n**0.5)+1)
    for p in P:
        while not n%p:
            n /= p
            L.append(p)
    if n != 1:
        L.append(n)
    return L


def lessthan(max):
    """
    Returns a sorted list of all primes strictly less than max."
    
    U.R.E. for max to be non-integer. If n < 2, returns [].
    """
    return __generator(max) 

def first(n):
    """
    Returns a sorted list of the first n primes.
    
    U.R.E. for max to be non-integer. If n < 1, returns [].
    """
    
    cap = 15*n
    P = __generator(cap)
    while len(P) < n:
        cap *=2
        P = __generator(cap)
    return P[:n]
    
    
    if n < 26:
        return __generator(100)[:n]
    return __generator(int(1.2**n))[:n]


def __generator(n): 
    if n<=2: 
        return []
    odds = range(3,n+1,2)
    threshold = n ** 0.5
    sievesize=len(odds)
    for i, m in enumerate(odds):
        if m >= threshold:
            break
        if m:
            j = (m*m-3)/2
            while j<sievesize:
                odds[j]=0
                j += m
    tr = [2]+[x for x in odds if x]
    if tr[-1] == n:
        tr.pop()
    return tr

# OLD CODE BELOW

def __jumpstart(n, P):
    odds = range(3, n+1, 2)
    j = 1 #start at 1 to avoid 2
    lenP = len(P)
    for i, o in enumerate(odds):
        if o == P[j]:
            j += 1
            if j == lenP:
                break
        else:
            odds[i] = 0
    return odds

def __firstGuard(primes, max):
    if len(primes) > max:
        return False
    return True

def __lessthanGuard(primes, max):
    if primes[-1] < max:
        return True
    return False

def __upto(max, guard): 
    primes = [2]
    unchecked = 3
    while (guard(primes, max)):
        couldBePrime = True
        threshold = int(unchecked**0.5)+1
        for p in primes:
             if not unchecked%p: #if p divides unchecked
                couldBePrime = False #then it isn't prime
                break
             if p > threshold:
                break
        if couldBePrime:
            primes.append(unchecked)
        unchecked += 1

    primes.pop() #pop the prime that failed guard
    return primes

import primes

def sumPrimePowers(STOP):
    A = int(STOP**0.5)+1
    B = int(STOP**(1.0/3.0))+1
    C = int(STOP**0.25)+1
    P = primes.first(A)
    Results = set([])
    for a in range(A):
        for b in range(B):
            for c in range(C):
                n = P[a]**2 + P[b]**3 + P[c]**4
                if n < STOP:
                    Results.add(n)
    return len(Results)

print sumPrimePowers(5000000)

import primes, itertools

for n in range(10, 1, -1):
    permutations = list(itertools.permutations(range(1, n)))
    l = []
    for p in permutations:
        l.append(int(str(p).strip('[]()').replace(", ",""))) #tuple to int

    selected = primes.filter(l)
    if len(selected) != 0:
        print max(selected)
        exit()

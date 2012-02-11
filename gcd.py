def one(a, b, calls):
    calls += 1
    if a > b:
        a, b = b, a
    c = b-a
    if c == 0:
        print calls
        return a
    return one(a, c, calls)

def two(a, b, calls):
    calls += 1
    if b == 0:
        print calls
        return a
    return two(b, a%b, calls)

def three(a, b, calls):
    calls += 1
    if a > b:
        a, b = b, a
    if a == 0:
        print calls
        return a
    return two(a, b%a, calls)

one  (867, 1989, 0)
two  (867, 1989, 0)
three(867, 1989, 0)

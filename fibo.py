l = [1, 1]
total = 0
while l[-1] < 4000000:
    l.append(l[-1] + l[-2])
l.pop()

for n in l:
    if not n%2:
        total += n
print total, l[-1]

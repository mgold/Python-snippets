l = [1, 1]
while len(str(l[-1])) < 1000:
    l.append(l[-1] + l[-2])
print len(l)


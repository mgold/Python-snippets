f = open('words.txt')
words = f.read()
f.close()
words = words.replace('"', '')
words = words.split(",") 

trinums = []
for i in range(20):
    trinums.append((i*(i+1))/2)

grandTotal = 0
for w in words:
    total = 0
    for l in w:
        total += ord(l)-64 #64 = ord('A')+1
    if total in trinums:
        grandTotal += 1
print grandTotal

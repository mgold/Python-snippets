f = open('names.txt')
names = f.read()
f.close()
names = names.replace('"', '')
names = names.split(",") 
names.sort()

grandTotal = 0
for i, n in enumerate(names):
    total = 0
    for l in n:
        total += ord(l)-64 #64 = ord('A')+1
    total *= i+1 #i starts at 0
    grandTotal += total
print grandTotal

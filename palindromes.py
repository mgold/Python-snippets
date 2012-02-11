import math

def has2ThreeDigitFactors (big):
	for i in range(1, int(math.ceil(math.sqrt(big)))):
		if((not big%i) and len(str(big/i)) == 3 and len(str(i)) == 3):
			return True
	return False

def palindrome (base):
	tr = base * 1000
	tr += int(str(base)[2:3])*100
	tr += int(str(base)[1:2])*10
	tr += int(str(base)[0:1])*1
	return tr

for i in range (999, 100, -1):
	if has2ThreeDigitFactors(palindrome(i)):
		print palindrome(i)
		break
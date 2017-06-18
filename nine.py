#Nine
# a^2 + b^2 = c^2
# a + b + c = 1000

import math

summ = 1000

for a in range(1, summ/3):
	for b in range(a+1, summ/2):
		c = summ - a - b
		if (a*a + b*b == c*c):
			print str(a) + ' ' + str(b) + ' ' + str(c)
			print "The product is " + str(a*b*c)

'''
A = list(range(1, summ))

for a in range(1, summ):'''

for num in xrange(20, 999999999):
	if all(num % n ==0 for n in range(11, 21)):
		print num
number = 600851475143
i = 2

while i < number:
	while number % i == 0:
		number = number / i
	i = i + 1

print "The largest prime factor is " + str(number)
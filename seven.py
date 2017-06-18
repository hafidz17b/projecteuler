def is_prime(num):
	point = 1
	for i in range(2, num+1):
		if num % i == 0:
			point += 1
		if point > 2:
			return False
	return True

def count_prime(n):
	counted = 0
	start_num = 1

	while True:
		if is_prime(start_num) == True:		
			if counted == n:
				print "The " + str(n) + "th prime  number is " + \
			       str(start_num)
				break
			counted += 1
		start_num += 1

print count_prime(10001)
def is_prime(num):
	if num == 2:
		return True
	elif num == 1:
		return False
	elif num == 3:
		return True
	elif num % 2 == 0:
		return False
	else:
		for i in range(4, num):
			if num % i == 0:
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
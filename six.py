num = 100

def square(n):
	result = []
	for i in range(1, n+1):
		i = i * i 
		result.append(i)
	return sum(result)

def sum_square(n):
	result = []
	for i in range(1, n+1):
		result.append(i)
	return sum(result) * sum(result)

print square(num)
print sum_square(num)
print "Difference " + str((sum_square(num) - square(num)))
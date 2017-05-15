numbers = 1000
result = 0
results = []

for i in range(1,numbers):
	if (i % 3 and i % 5) == 0:
		results.append(i)

print "List of number multiples of 3 or 5 are " + str(results)
print "Sum of list is " + str(sum(results))
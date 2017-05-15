series = [1, 2]
even_number = []

while True:
	number = series[-1] + series[-2]
	if number > 4000000:
		break
	series.append(number)

for i in series:
	if i % 2 == 0:
		even_number.append(i)


print series
print "Even number " + str(even_number)
print "The sum is " + str(sum(even_number))

number1 = range(100,1000)
number2 = range(100,1000)
num = 0
result = []

for i in number1:
	for j in number2:
		num = i * j
		result.append(num)


paltot = []

for k in result:
	pal = str(k)
	pal2 = pal[::-1]
	if pal == pal2:
		paltot.append(int(pal))

print "The largest palindrome made by two 3-digit is " +\
    str(max(paltot))
'''
string = "12321"
reversed_string = string[::-1]
if string == reversed_string:
	print reversed_string
	'''
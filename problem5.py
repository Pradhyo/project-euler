# Problem 5 from project Euler

''' What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20? '''

number = 20
factorsofanswer = {}

def factor(number):
	"""Given a number, return its factors as a dictionary """
	factors = {}
	for i in range(2,(number+2)/2):
		while number % i == 0:
			factors[i] = factors.get(i,0) + 1
			number /= i
	if number != 1:
		factors[number] = 1
	return factors

def productoffactors(factors):
	"""Given factors and powers as dictionary, return the number """
	number = 1
	for factor in factors:
		number *= factor ** factors[factor]
	return number

for i in range(number,number/2,-1):
	factors = factor(i)
	for each in factors:
		if factors[each] > factorsofanswer.get(each,0):
			factorsofanswer[each] = factors[each]

print productoffactors(factorsofanswer)





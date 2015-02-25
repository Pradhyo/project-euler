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
	return factors





# Problem 12 from Project Euler

''' The sequence of triangle numbers is generated by adding the natural numbers. 

What is the value of the first triangle number to have over five hundred divisors? '''

def triangle_number(number):
	"""The sequence of triangle numbers is generated by adding the natural numbers. 
	This function returns the sum of natural numbers including number"""
	return number * (number + 1) / 2

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

def number_of_divisors(number):
	"""return number of factors of number"""
	total_factors = 1
	prime_factors = factor(number)
	for current_factor in prime_factors:
		total_factors *= prime_factors[current_factor] + 1
	return total_factors

min_divisors = 50
current = 0



while True:
	current += 1
	current_triangle_number = triangle_number(current)
	divisors_count = 0	
	for i in range(1,current_triangle_number + 1):
		if current_triangle_number % i == 0:
			divisors_count += 1
		if divisors_count >= min_divisors:
			print current_triangle_number
			break
	if divisors_count >= min_divisors:
		break
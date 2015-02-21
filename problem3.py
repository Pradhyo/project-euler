# Problem 3 from project Euler

'''What is the largest prime factor of the number 600851475143 ?'''

number = 600851475143

def is_prime(number):
	if number in [0,1]:
		return None
	for i in range(2,number):
		if number % i == 0:
			return False
	return True

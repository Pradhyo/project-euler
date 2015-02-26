# Problem 7 from project Euler

'''What is the 10 001st prime number?'''

def is_prime(number):
	if number == 0 or number == 1:
		return None
	for i in range(2,int(number**0.5)+1):
		if number % i == 0:
			return False
	return True
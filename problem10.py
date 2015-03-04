# Add problem 10 from project Euler

''' Find the sum of all the primes below two million. '''

def is_prime(number):
	if number in [0,1]:
		return None
	if number in [2,3]:
		return True
	if number % 2 == 0 or number % 3 == 0:
		return False
	for i in range(5,int(number**0.5)+1,6):
		if number % i == 0 or number % (i+2) == 0:
			return False
	return True

answer = 0

for i in range(2000000):
	if is_prime(i):
		answer += i

print answer

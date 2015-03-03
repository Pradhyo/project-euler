# Add problem 10 from project Euler

''' Find the sum of all the primes below two million. '''

def is_prime(number):
	if number in [0,1]:
		return None
	for i in range(2,int(number**0.5)+1):
		if number % i == 0:
			return False
	return True

answer = 0

for i in range(2000000):
	if is_prime(i):
		answer += i

print answer

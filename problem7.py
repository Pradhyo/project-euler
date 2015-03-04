# Problem 7 from project Euler

'''What is the 10 001st prime number?'''

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

count = 0
i = 1
number = 10001
while count<number:
	i += 1
	if is_prime(i) == True:
		count += 1

print i
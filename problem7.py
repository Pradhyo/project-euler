# Problem 7 from project Euler

'''What is the 10 001st prime number?'''

def is_prime(number):
	if number == 0 or number == 1:
		return None
	for i in range(2,int(number**0.5)+1):
		if number % i == 0:
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
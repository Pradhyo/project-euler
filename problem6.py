# Problem 6 from project Euler

''' Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum. '''

def sumofpermutations(number):
	"""Return sum of all possible pairs from 1 to number not including squares
	For 3, return 1(2) + 1(3) + 2(1) + 2(3) +3(1) + 3(2)"""
	sum = 0
	for i in range(1,number):
		for j in range(i+1,number+1):
			sum += i * j
	return 2 * sum

''' Essentially, answer is (a + b + c)^2 - (a^2 + b^2 + c^2) which is nothing 
but 2 (ab + bc + ac). Similarly for first hundred, the above function would 
return the answer'''
print sumofpermutations(100)
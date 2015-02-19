# Problem 1 from project Euler

''' If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the
multiples of 3 or 5 below 1000.'''

'''n = 1000
answer = 0
for i in range(1,n):
	if i % 3 == 0 or i % 5 == 0:
		answer += i

print answer'''

maximum = int(raw_input("Enter the upper limit (not included): "))
maximum -= 1

def sumofintegers(n):
	"""Return sum of intergers from 1 to n"""
	return n * (n + 1) / 2

sumof3s = 3 * sumofintegers(maximum / 3)
sumof5s = 5 * sumofintegers(maximum / 5)
sumof15s = 15 * sumofintegers(maximum / 15)

'Subtract sum of multiples of 15 as they are included twice'
answer = sumof5s + sumof3s - sumof15s

print answer


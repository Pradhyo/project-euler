# Problem 2 from project Euler

'''Find the largest palindrome made from the product of two 3-digit numbers'''

def is_palindrome(number):
	return str(number) == str(number)[::-1]

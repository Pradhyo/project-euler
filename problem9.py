# Problem 9 from Project Euler

'''There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc (a<b<c). '''

number = 1000

answer = [a*b*(number-(a+b)) for a in range(1,number/3) 
							 for b in range(a+1,(number-a)/2) 
							 if a*a + b*b == (number-a-b)**2]
							 
print answer
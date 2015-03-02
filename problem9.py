# Problem 9 from Project Euler

'''There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc (a<b<c). '''

"a cannot be 333, as b=334, c=335 will give sum >1000"

answer = [a*b*c for a in range(1,333) for b in range(a+1,1000) for c in range(b+1,1000) if a+b+c == 1000 and a*a + b*b == c*c]

print answer
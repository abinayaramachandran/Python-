# Program by Abinaya Ramachandran 
# Fibonacci checker

import math

def isPerfectSquare(n):
	n_sqrt = int(math.sqrt(n))
	return n == n_sqrt * n_sqrt;

def isFibonacciNumber(n):
	# n is Fibinacci if one of 5*n*n + 4 or 5*n*n - 4 or both 
    # is a perferct square 
	return isPerfectSquare( 5 * n * n + 4) or isPerfectSquare(5*n*n -4)

n = int(input("Enter Number to check if it is Fibonacci : "))
print(isFibonacciNumber(n))
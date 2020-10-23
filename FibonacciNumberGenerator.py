# Program by Abinaya Ramachandran 
# Fibonacci Number

# Print nth Fibonacci number
def fibonacciNumber(n):
	if n <= 0:
		return 0
	elif n == 1 or n == 2:
		return 1
	else:
		return fibonacciNumber(n - 1) + fibonacciNumber(n - 2)

n = int(input("Enter Number to get Fibonacci : "))
print(fibonacciNumber(n))




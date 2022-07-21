print("Nth Fibonacci")

def nthFibonacci(n):
	if n == 1:
		nthFibonacciValue = 0
	elif n == 2:
		nthFibonacciValue = 1
	elif n == 3:
		nthFibonacciValue = 1
	else:
		nthFibonacciValue = "I don't know"
	return nthFibonacciValue


n = 8
print(f"n is equal to {n}")
fibValue = nthFibonacci(n)
print(f"The nth Fibonacci value is: {fibValue}")
print("Nth Fibonacci")

def nthFibonacci(n):
	a = 0
	b =1

	if n == 1:
		return 0
	if n == 2:
		return 1	
	
	for counter in range(3,n+1):
		swap = b  
		b = a + b 
		a = swap
	return b
	
n =  9
print(f"n is equal to {n}")
fibValue = nthFibonacci(n)
print(f"The nth Fibonacci value is: {fibValue}")
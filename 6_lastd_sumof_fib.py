
def pisanoPeriod(m):
	previous, current = 0, 1
	for i in range(0, m * m):
		previous, current = current, (previous + current) % m
		if (previous == 0 and current == 1):
			return i + 1

 
def last_dig(n):
	
	pisano_period = pisanoPeriod(10)

	n = n % pisano_period
	
	previous, current = 0, 1
	if n==0:
		return 0
	elif n==1:
		return 1
	for i in range(n-1):
		previous, current = current, previous + current + 1
		
	return (current % 10)


if __name__ == '__main__': 
	n = int(input())
	print(last_dig(n))

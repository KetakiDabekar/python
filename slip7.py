a=int(input("Enter the number:"))

def sumsquare(n):
	sm=0
	for i in range(1,n+1):
		sm=sm+(i*i)
	
	return sm
print(sumsquare(a))


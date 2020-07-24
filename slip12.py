a=int(input("Entre the number:"))
sum=0
for i in range(1,a):
	if(a%i==0):
		sum=sum+i
		
if(a==sum):
	print("number is perfect:",a)
else:
	print("number is not perfect:",a)

	
	

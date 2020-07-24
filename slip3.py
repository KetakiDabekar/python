a=int(input("enter a number:"))
ans=True
for i in range(2,a/2):
	if(a%i==0):
		ans=False
		break;
if(ans==True):
	print("number is prime:",a)
else:
	print("number is not  prime:",a)
		


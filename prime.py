n=int(input("Enter a number"))
ans=True
for k in range(2,n/2):
	if(n%k==0):
		ans=False
		break;
if ans == True:
	print("Prime Number")
else:
	print("Not prime Number")

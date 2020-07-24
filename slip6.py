a=int(input("Enter the number"))
temp=a
digit=0
while(temp!=0):
	digit+=1
	
	temp=temp//10

print("no.of digit:",digit)

temp=a
ans=0
while(temp!=0):
	ans=ans+(temp%10)**digit
	temp=temp//10

if(a==ans):
	print("number is armstrong:",a)
else:
	print("number is not armstrong:",a)




jug1,jug2=0,0

jug1cap=int(input("Enter the capacity of jug1:"))
jug2cap=int(input("Enter the capacity of jug2:"))

d=int(input("Enter amt:"))

if(jug1cap>=0 and jug2cap>=0):
	c2=1
	print(jug1,":",jug2)
	
while True:
	if(jug1==0 and c2==1):
		jug1=jug1cap
		print(jug1,":",jug2)
		jug2=jug1
		jug1=0
		print(jug1,":",jug2)
		
	if(jug1==0):
		jug1=jug1cap
		print(jug1,":",jug2)
	
	if(jug2!=jug2cap):
		jug2+=(jug2cap-jug1)
		jug1-=(jug2cap-jug1)	
		print(jug1,":",jug2)
	
	if(d==jug1 or d==jug2):
		break;
		#print(jug1,":",jug2)
		
	if(jug2==jug2cap):
		jug2=0
		print(jug1,":",jug2)

	c2+=1

print("final solution:",jug1,jug2)

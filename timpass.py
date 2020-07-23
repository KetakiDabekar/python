jug1=0
jug2=0

j1cap=int(input("Enter Jug1's capacity"))
j2cap=int(input("Enter Jug2's capacity"))

d=int(input("Enter d"))
if(j1cap>=0 and  j2cap>=0):
	c2=1
	print(jug1,":",jug2," in start wala if")

while True:
	if(jug1==0 and c2==1):
		jug1=j1cap
		print(jug1,":",jug2," in 1st if")
		jug2=jug1
		jug1=0
		print(jug1,":",jug2," in 1st if")
		
	if(jug1==0):
		jug1=j1cap
		print(jug1,":",jug2," in 2nd if")
		
	if(jug2!=j2cap):
		jug2+=(j2cap-jug1)
		jug1-=(j2cap-jug1)
		print(jug1,":",jug2," in 3rd if")
		
	if(d==jug1 or d==jug2):
		break
		#print(jug1,":",jug2," in 4th if")
		
	if(jug2==j2cap):
		jug2=0
		print(jug1,":",jug2," in 5th if")
		
	c2+=1
		
print("Final solution:",jug1,jug2)

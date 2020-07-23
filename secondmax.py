list1=[12,101,1120,78,67]
max1=0
max2=0

for i in list1:
	if i>max1:
		max1=i

for i in list1:
	if i<max1 and i>max2:
		max2=i

print("second last largest number:",max1)		
print("second last largest number:",max2)	

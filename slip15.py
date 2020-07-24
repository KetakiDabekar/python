list=[1,4,5,6,7,9,10,12,13,15]
max1,max2,=0,0
for i in list:
	if i>max1:
		max1=i
		
for i in list:
	if i<max1 and i>max2:
			max2=i
print(max1)
print(max2)




list1=[1,2,-3,-4,5,-6,7,8,-9,-10]
pos_count,neg_count=0,0
for num in list1:
	if num>=0:
		pos_count+=1
	else:
		neg_count+=1

print("positive numbers in list:",pos_count)
print("negative numbers in list:",neg_count)


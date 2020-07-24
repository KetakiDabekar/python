list1=[1,-2,-3,4,-5,6,-7,8,-9]
pos_cnt,neg_cnt=0,0

for num in list1:
	if num>=0:
		pos_cnt+=1
	else:
		neg_cnt+=1
		
print("postive count:",pos_cnt)
print("negative count:",neg_cnt)


list1=[1,4,7,9,3]
print("Elements of list:",list1)


n=int(input("Enter number of elements to append"))
for i in range(0,n):
    str=input("enter element ::")    #append  or Add
    list1.append(str)
print("List after append ",list1)  

list1.extend([11,14])  #Extend 
print "List after Extend :",list1

print("conacatenation",list1+[1,5,7,8,3,2])

print("Using iteration")                    #Iteration
for i in list1:
	print(i)

	
print("the length of the list is::",len(list1))                #Length


index=list1.index(5)
print "index of 5 is :",index


x=input("Delete :: enter the element you wanna delete")
list1.remove(x)                         #Delete
print "new list ",list1








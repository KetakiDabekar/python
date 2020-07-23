number=int(input("Enter the number:"))

print("orignal number is:"+str(number))

res=str(number)==str(number)[::-1]

print("number is palindrome or not?:"+str(res))

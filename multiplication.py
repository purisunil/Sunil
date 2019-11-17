#write a program to print the multiplication table of the number entered by the user.
num=int(input("enter the number"))
print("the multiplication table is %s" % num)
for x in range(1,11):
    print("%s * %s = %s" %(num, x, num*x))

#wap using function to find factorial of number.

def fact(a):
    fact = a*(a-1)
    return fact
num = int(input("enter a number\t"))
factorial = fact(num)
print("the factorial of %s is %s"%(num, factorial))

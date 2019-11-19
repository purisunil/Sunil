#wap to find armstrong or not

def arm(n):
    sum = 0
    while n > 0:
        num = n%10
        sum = sum+num**3
        n//=10
    return sum
num=int(input("enter the number\t"))
sum1=arm(num)
if sum1 ==num:
    print("it is armstrong num")
else:
    print("sorry,it is not armstrong num")

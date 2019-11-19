#wap to show number is palindrome or not.

def palindrome(a):
    rev_num=0
    while a>0:
        b=a%10
        rev_num=rev_num*10+b
        a=a//10
    return rev_num
num=int(input("enter a number\t"))
check_num = palindrome(num)
if check_num ==num:
    print("the num is palindrome")
else:
    print("the num is not palindrome")

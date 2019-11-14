#To check even or odd
Number=int(input("Enter the Number"))
if Number==0 :
    print("0")
elif Number%2==0:
    print("even")
elif Number<=0:
    print("invalid")
else:
    print("odd")
marks=int(input("enter the marks"))
if marks>=90 and marks<=100 :
    print("you have grade 'A'")
elif marks>=70 and  marks<=90 :
    print("you have grade 'B'")
elif marks>=40 and marks<=70 :
    print("you have grade 'C'")
elif marks<40 and marks>=0 :
    print("you are fail")
else :
    print("INVALID")

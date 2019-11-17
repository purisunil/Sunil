#wap to ask user name, age and mob number with validations

name=input("enter your name")
while name.isalpha()==False or len(name)<3:
    print("sorry wrong input")
    name=input("enter your name")
mob_num=input("enter your phone number")
while len(mob_num)!=10 or mob_num.isalpha():
    print("sorry, enter your original number")
    mob_num=input("enter your phone number")
age=input("enter your age")
while age.isdigit()==False or int(age)<19:
    print("enter you age rightly")
    age=input("enter your age")
print("your name is", name)
print("your mob number is", mob_num )
print("your age is", age)
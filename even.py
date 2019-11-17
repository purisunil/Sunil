#from a list of number make a new list cotaining only the even number
list=[]
i=0
n=int(input("enter the number of elements"))
while i<n:
    print("enter the element")
    element=int(input())
    list.append(element)
    i+=1
print(list)
even_list=[]
for i in list:
    if i%2==0:
        even_list.append(i)
print("the even number list is:", even_list)
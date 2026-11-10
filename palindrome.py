#write a prigram to chake if list contain palindrome or not
lis=[1,2,3,3,3,2,1]
copyl=lis.copy()
copyl.reverse()
if(copyl==lis):
    print("valid palindrome")
else:
    print("invalid")    

#write a program to count student with grade "A"
grade=("A","B","G","J","A","E")
print(grade.count("A"))


grade2=["A","B","G","J","A","E"]
grade2.sort()
print(grade2)
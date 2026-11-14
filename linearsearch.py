#search for a number X in list using loop

lis=(11,22,33,44,55,66)
target=int(input("enter target"))
i=0
while i<len(lis):
    if(lis[i]==target):
         print("found at:",i)
    i=i+1    


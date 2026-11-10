# n=1
# #while loop
# while n<=10:  #condition
#     print("hello")
#     n+=1    #increment
# #print numbers from 1-5
# i=1
# while i<=5:
#     print(i)
#     i+=1
# #print numbers from 5-1
# j=5
# while j>=1:
#     print(j)
#     j=j-1

# #print num from 1-100
# k=1
# while k<=100:
#     print(k)
#     k+=1    
# #print num from 100-1
# l=100
# while l>=1:
#     print(l)
#     l=l-1        

#print multiplication table of number n
#n=int(input("enter ur num"))
# i=1
# while i<=10:
#     print(n*i)
#     i+=1
#print element of list using loop
list=[1,2,3,4,4,55,66,7,8,8,8]  
i=0  
#traverse
while i<len(list):
    print(list[i])
    i+=1


#break keyword used to ternimate loop 
mk=[11,22,55,77,8,8]
i=0
while i<len(mk):
    print(mk[i])
    if(i==3):   #loop will terminate when index = 3
        break
    i+=1

#continue keywrd:it skip current iteration

i=0
while i<=5:
    
    if(i==3):
     i+=1
     continue
    print(i)
    i+=1
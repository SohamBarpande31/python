eg=[1,3,4,3,4,2,7,8,9]
for g in eg:
   print(g)

#search for num X  using for loop

hg=[2,44,54,21,43,89,9]
tar=45
for i in hg:
   if(i==tar):
      print("foundddd")
else:
   print("not found")   

#range function  , syntax: range(start,stop,step)
for i in range(5):
   print(i)   

print("....................")

for j in range(2,10):   #range(start,stop)
   print(j)            

print(">>>>>>>.>>>>>>>>>>>>>>.>>>>>>>>>")   

for k in range(2,100,2):   #range(start,stop,step). step mens how much gap 
   print(k)

#pass statement: it does nothing and used as placeholder for future code 
for i in range(5):
     pass   
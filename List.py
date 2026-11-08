#list
marks=[45,90,56,78,65]
print(marks)
print(marks[0])
print(marks[1])

#lists are mutable soo we can assign or update new value
marks[0]=93
print(marks[0])  #93 is assigned to 0 index

#slicing
print(marks[1:4])

id=[201,908,208,301,108]
id.append(233)  #add element at end
print(id)

#sort
id2=[22,33,12,23,45,65,76]
id2.sort()  #sort element in ascending order
print(id2)

#to reverse the list
li=["a","v","b","d","f","o"]
li.reverse()
print(li)

#insert
lit=[23,67,87,65,43,32,21,38]
lit.insert(1,2000) #first we gave a index on which we want to insert and then the value that we want to insert
print(lit[1])  

#pop (it delet elemnt at given index)
lit.pop(7) #item at 7th index is deleted
print(lit)

#string is datatype that stores a sequence of characters
str1="heyy,\n Good morning"
print(str1)

#basic operations
#concatination
a="soham"
b=" barpande"
str=a+b
print(a+b)

#length of sting
print(len(a))

#indexing
c="BMW"
print(c[1])
#c[2]="N" #we cannot modify characters 
print(c[2])

#slicing
d="london"
print(d[0:5])
#to manipulate from backward we use negative letters
print(d[-3:-1])

#endswith : it chake if given strings last part ends with given letter if yes then it return true
hobby="cricket"
print(hobby.endswith("et"))  #cricket ends with "et" so it retuend true

#capatilize it make first character of string capital(it do nnot modify original string)
print(hobby.capitalize())

#replace : it replace given word from string 
print(hobby.replace("i","l")) #we replaced i with l

#find:it return first inted of first index of that given word
print(hobby.find("i"))

#count:it count the occurance of sustring
print(hobby.count("c"))
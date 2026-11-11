#Dictionary
#it is used to store data in key:value pairs
#they are unordered ,mutable,and do not allow duplicate keys
info={
    "name":"soham",
    "age":22,
    "isadult":True,
    "marks":[23,45,66,78,8,22,]
}
print(info)
print(info["name"])  #to acess value we use key
info["name"]="sonu"  #we assign new value to exixting key
print(info["name"]) 

#Nested Dictionaries
mrk={
    "name":"soham",
    "score":{
        "maths":45,
        "chem":45,
        "phy":55
    }
}
print(mrk)
print(mrk["score"]["maths"])

#To return all keys
print(mrk.keys())
#To return all values
print(mrk.values())
#length of student
print(len(mrk))
#return all key (value , pair) as tuple
print(mrk.items())
#we can also acess value using key by using .get 
print(mrk.get("name"))

#store word with their meanin in dictionary
myinfo={
    "table":"A piece of furniture",
    "Cat":"A small animal"
}

print(myinfo)
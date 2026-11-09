#sets
#it is collection of unordered item
#it must be unique and immutable
nums={1,2,3,4,5,6}
print(nums)
print(type(nums))
#length
print(len(nums)) 

num=set()
num.add(23)
num.add(33)
#num.clear() to delete all elment
print(num)
num.pop()
print(num) #delete last element from set

st1={1,2,3,4}
st2={1,4,6,3}
print(st1.union(st2))

triyal={9,"9.0"}
print(triyal)
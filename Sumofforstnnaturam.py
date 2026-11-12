#write a program to calculate sum of first n natural number
def sum(n):
    if(n==0):
        return
    print(n+n-1)
    sum(n-1)

sum(5)    
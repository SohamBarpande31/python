age=22

if(age>=18):
    print("yes u can drive")
else:
    print("doo not drive")    


#signal system
light=input("enter signal light")
if(light=="red"):
    print("stoppp!!!")
elif(light=="yellow"): #indentation
    print("start the vehicle")
else:
    print("goooo!!")       

#grade student based on marks
marks=40

if(marks>=90):
    print("Grade A")
elif(marks>=60):
    print("Grade B")
elif(marks>=40):
    print("Grade C")       
else:
    print("fail")    


#nesting
ag=84
if(ag>=18):
    if(ag>=80):
        print("cannot drive")
    print("can drive")
else:
    print("cannot drive")    

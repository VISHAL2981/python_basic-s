a=9
b=8
c=sum((a,b))#built in functional


def function1(a,b):
    print("hello you are in function 1",a+b)

def function2(a,b):
    """This is a function which will calculate average of two number"""
    average=(a+b)/2 
    # print (average)
    return average

print(function2.__doc__)

v= function2(5,7)  
print(v) 


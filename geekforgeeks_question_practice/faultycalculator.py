# Exercise 2 - Faulty Calculator
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Design a calculator which will correctly solve all the problems except
# the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Your program should take operator  and the two numbers as input from the user
# and then return the result
#
print("enter your 1st number")
n1=int(input())
print("enter your 2nd number")
n2=int(input())

print("select operator?","+,-,/,%,*")
n3=(input())


if n1==45 and n2==3 and n3=="*":
    print("555" )
elif n1==56 and n2==9 and n3=="+":
    print("77")
elif n1==56 and n2==6 and n3=="/":
    print("4")
elif n3=="*":
    n4=n1*n2
    print(n4)
elif n3=="/":
    n4=n1/n2
    print(n4)
elif n3=="+":
    n4=n1+n2
    print(n4)
elif n3=="-":
    n4=n1-n2
    print(n4)
elif n3=="%":
    n4=n1%n2
    print(n4)
else:
    print("plz..! check your input")




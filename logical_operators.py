# Operators In Pythons
# Arithmetic Operators
# Assignment Operators
# Comparison Operators
# Logical Operators
# Identity Operators
# Membership Operators
# Bitwise Operators

# Arithmetic Operators
print("5 + 6 is ", 5+6)
print("5 - 6 is ", 5-6)
print("5 * 6 is ", 5*6)
print("5 / 6 is ", 5/6)
print("5 ** 3 is ", 5**3)
print("5 % 5 is ", 5%5)
print("15 // 6 is ", 15//6)

# assignment operator
x=5
print(x)
x+=7
print(x)
x/=7
print(x)
x%=7
print(x)
x-=7
print(x)

# comparison operators
print("comparison operator")
i=8
# print(1==5)  #false
print(1==8) #true
print(i<=8) #true
print(i>=8) #true
print(i>9) #false


# logical operators
print("logical operator")

a=True
b=False

print(a and a)#true
print(a and b)#false
print(b and b) #false


print("membership operator")

list=[3,4,5,6,43,52,6,78,65]
print(324 not in list)#true
print(3 not in list)# false


print("bitwise operator")

#0=00
#1=01
#2=10
#3=11

print(0 & 1)
print(0 | 3)
# 00
# 01
# and[| 0r &]{sign of (or) and (&) operator} operator use
# 11 =3
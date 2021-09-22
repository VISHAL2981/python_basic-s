# EXAMPLE1:
# Input : P = 10000
#         R = 5
#         T = 5
# Output :2500
# We need to find simple interest on 
# Rs. 10,000 at the rate of 5% for 5 
# units of time.

# P = 10000
# R = 5
# T = 5

# si=float((P*T*R)/100)

# print(si)


# EXAMPLE2:
# Input : P = 3000
#         R = 7
#         T = 1
# Output :210


def simpleintrest(p,t,r):

  print('The principal is', p)
  print('The time period is', t)
  print('The rate of interest is',r)
      
  si = (p * t * r)/100

  print("the si is",si)

simpleintrest(8,6,8)





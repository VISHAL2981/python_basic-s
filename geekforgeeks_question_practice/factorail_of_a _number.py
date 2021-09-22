#recursive approach
def factorial(n):
    return 1 if (n==0 or n==1) else n * factorial(n-1)
       

    
n=int(input())

print("factorial of a",n,"is",factorial(n) )



# #inbuilt function

# import math
 
# def factorial(n):
#     return(math.factorial(n))
 
 
# # Driver Code
# n = 3
# print("Factorial of", n, "is",
#       factorial(n))

    


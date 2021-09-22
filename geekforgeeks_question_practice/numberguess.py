n=18
noofguess=0


print("lets start or begin the number guessing game ")

while(noofguess<10):
 num1=int(input())
 if(num1==n):
    print("you are correct congratulations you win the game")
    break
 elif(num1<n):
    print("you are wrong try bigger number")
    noofguess=noofguess+1
    print("no of guess left",10-noofguess)
    continue
    


 elif(num1>n):
    print("you are wrong try smaller number")
    noofguess=noofguess+1
    print("no of guess left",10-noofguess)
    continue


print("game over")

    

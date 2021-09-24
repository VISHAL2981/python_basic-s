def getdate():
    import datetime
    return datetime.datetime.now()

def clientname(client):
    info = True
    while (info):
        
        print("what do want to log for\n press \n (1) For Excercise \n (2) For diet ")
        giveyourname=int(input())
        if giveyourname ==1:
            with open(client+"excercise.txt","a") as f:
                print("enter the type of excercise you have done")
                kasrat=(input())
                f.write("["+str(date)+"]"+"\t"+kasrat+"\n")

        elif giveyourname==2:
            with open(client+"Diet.txt","a") as f:
                print("enter the type of diet you take")
                kasrat1=(input())
                f.write("["+str(date)+"]"+"\t"+kasrat1+"\n") 
       
        else: print("enter the valid input sir ")   



date = getdate()
print("please enter the client name:-\n press\n [0] For Radhika \n [1] for Vishal \n [2] for Ritika")
clients=["Radhika","vishal","Ritika"]
names=int(input())
c1=clients[names]
client=clientname(c1)




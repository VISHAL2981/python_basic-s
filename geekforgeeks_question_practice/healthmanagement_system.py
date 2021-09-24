# # Health Management System
# # 3 clients - vishal, Radhika and Ritika

# # def getdate():
# #     import datetime
# #     return datetime.datetime.now()

# # Total 6 files
# # write a function that when executed takes as input client name
# # One more function to retrieve exercise or food for any client

# # print("choose your client name")
# # def clientdetails(vishal,radhika,ritika):
# #     # clientname = int(input("1 vishal\n  2 radhika\n  3 ritika\n"))
# #     print("what you want to log for vishal..?")

        
# #     # clientname = int(input())

# def log():
#     print("Choose your client")
#     client = int(input("1. Harry \n2. Rohan \n3. Hammad"))
#     con = 1
#     if client == 1:
#         while con == 1:
#             print("What do you want to log for Harry?")
#             choice = int(input("1. Diet \n2. Activity"))

def getdate():
    import datetime
    return datetime.datetime.now()

def client_name(client):
    info = True
    while (info):
        print("What do you want to log \n Press \n (1) Excercise\n (2) Diet")
        option = int(input())
        if option == 1:
            with open(client+"_excercise.txt","a") as f:
                print("Enter the type of excercise done")
                food = input()
                f.write("["+str(date)+"]"+"\t"+food+"\n")
                info = False

        elif option == 2:
            with open(client + "_diet.txt", "a") as f:
                print("Enter the type of diet done")
                excercise = input()
                f.write("[" + str(date) + "]" + "\t" + excercise+"\n")
                info = False
        elif option == 3:
            with open(client + "_diet.txt", "a") as f:
                print("Enter the type of diet done")
                excercise = input()
                f.write("[" + str(date) + "]" + "\t" + excercise+"\n")
                info = False
        else:
            print("Please enter a valid input\n")


date = getdate()
print("Please enter the client name : \n (0) harry \n (2) rohan \n (3) hammad ")
clients = ["harry","rohan","hammad"]
i = int(input())
cl = clients[i]
client = client_name(cl)





  

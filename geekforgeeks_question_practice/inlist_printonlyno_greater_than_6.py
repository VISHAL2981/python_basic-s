list1=["float","int","vishal",1,3,5,774,2,1,14,53,5,85,4,5,21,32,448,3,34,56,78,96,44,54,6,78]

for item in list1:
    if str(item).isnumeric() and item>6:
        print(item)
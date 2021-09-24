# f = open("vishal_01.txt","rb")#in binary
f = open("vishal_01.txt","rt")#default


# content = f.read()
# print(content)

# content = f.read(3324)
# print("1",content)
#sara content  1 mai hi aagya bcoz vha read kai 3324 character dale maine 2 mai kuch nhi ayega dump ho jyenge 1 mai hi

# content = f.read(3234)
# print("2",content)




# print(f.readline())#read only one line print new line too
# print(f.readline())#read only one line
# print(f.readline())#read only one line


print(f.readlines())#it prints list

f.close()
   
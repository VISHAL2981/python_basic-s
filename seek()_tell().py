f=open("vishu.txt")
# print(f.tell())
print(f.readline())
f.seek(0) #reset lines
# print(f.tell())
print(f.readline())
# print(f.tell())

f.close()
#What if we want to know the position of the file(read/write) pointer.
# For this purpose, we use the tell() function. f.tell() returns an integer giving the file pointer current position in the file represented as a number of bytes. File Pointer/File Handler is like a cursor, which defines from where the data has to be read or written in the file. Sometimes it becomes important for us to know the position of the File Pointer. With the help of tell(), this task can be performed easily
# print(f.tell())
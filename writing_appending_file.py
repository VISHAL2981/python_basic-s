# f =open("vishal_01.txt","a")
# a=f.write("vishal want to became an ias officer and he show so much efforts \n")
# print(a)
# f.close() 

# handle read and write both
  
f =open("vishal_01.txt","r+")
print(f.read())

f.write("yes vishal will became an ias officer")
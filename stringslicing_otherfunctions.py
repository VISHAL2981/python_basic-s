mystr = "vishal is good by nature and a brave boy and want to became an ias"
print(len(mystr))
print(mystr[0:8])
print(mystr[::9])
print(mystr[::55566])
print(mystr[-15:-9])
#to make string ulta
print(mystr[::-1])
print(mystr[::-2])


print(mystr.isalnum())# it is false bcoz there is spaces in my str

print(mystr.isalpha())# it is false bcoz there is spaces in my str

print(mystr.endswith("boy"))# it is false bcoz last word or mystrng is not end with boy
print(mystr.endswith("ias"))# now its true



print(mystr.count("b"))


print(mystr.count("o"))

print(mystr.capitalize())

print(mystr.find("brave"))


print(mystr.lower())


print(mystr.upper())

print(mystr.replace("is","are"))

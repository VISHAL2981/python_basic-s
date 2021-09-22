s=set()
#print(type(s))
# l=[1,2,3,4,5]
# setlist = set(l)
# print(setlist)
# print(type(setlist))

s.add(1)
#s.add(1)#it will retain unique  value value only
s.add(2)
s.add(5)
s.add(6)
s.remove(2)
# s1 = s.union({1,2,3,4,5})
s1 = s.intersection({1,2,3,4,5})
print(len(s))
print(type(s))
print(max(s))
print(min(s))





print(s,s1)
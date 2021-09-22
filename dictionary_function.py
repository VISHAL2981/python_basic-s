# Dictionary is nothing but key value pairs

d1 = { }
# print(type(d1))


d2={"harry":"burger","vishal":"chicken","ramu":"bread","radhika":"idli","mummy":"dalroti","shubham":{"b":"maggie","c":"guava","d":"banana"}}


d2["ankit"]="junk food"
d2["qareem"]="kebab"
# print(d2)
# print(d2["shubham"])
# del d2["shubham"]

# d3=d2.copy()#it will return shallow copy 
# del d3["harry"]


# print(d2.get("harry"))
# d2.update({"vishu":"radhika"})
# print(d2)
print(d2.keys())
print(d2.items())







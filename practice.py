a = "harry" 
b= 4
v=9.0
c='''hello
guys,
nice to meet u'''
d= True
z = b+v
print(a)
print(type(a))
print(type(b))
print("sum of 3+4 is",z)
print("sum of 3+4 is",b+v)
print("u",3*4)
print("g",12/4)
print("u",3+4)
print("a",3-4) 

a = 34

a -= 12 
a *= 12
a /= 12
print(a)

b = (14>7)
b = (14<=7)
b = (14>=7)
b = (14<7)
b = (14==7)
j= (14!=7)
print(b)
print(j)
bool1 = True 
bool2 = False
print("The value of bool1 and bool2 is",bool1 and bool2)
print("The value of b1 or b2",bool1 or bool2)
print("The value of b1 and b2 is",  not bool1 )
print("The value of not bool2",not bool2) 

d = "3456"
d = int(d)
print((type(d)))
print(d+67)

f ="hi"
h = " himanshi"
print(h[1]) #slicing 
print(f + h)
print(f[0])
print(h[-3])
print(h[0:4]) # 4 not included
print(h[-3:-1]) # -1 is not included 
print(h[:3])
print(h[4:]) # first and the last are the default ones
print(d,f)
print(len(f)) # length of the str
i ="Hello guy how are you all"
# skip value
print(i[1:21:3]) # will skip 3 -3 and will go until the last one

print(i[1:14:4])
print(i.endswith("all")) 
print(i.endswith("guy"))
print(i.startswith("all")) # gives true or false
print(i.count("o"))
print(i.capitalize())
print(i.find("guys")) #  -1 as the word is not found there
print(i.find("o")) # will give the index where it comes for the first time only
print(i.replace("guy","guys")) # will replace everywhere

#  lists
a = [46,78,78.0,"sfu"]
print(a[3])
a[2]=56
print(a)
print(a[0:4])
b = [34,78,9,67]
b.sort()
print(b)
b.reverse()
 print(b)
a.append(68)
print(a.append)
a.insert(2,34)
a.pop(3)
a.remove(34)
print(a)

#tuple
t = (1,34,"fhvg",56)
print(t)

# dictionary

mydict = {
    "fast" : "runner",
    "harry" : "name",
    "marks" : [1,2,3],
    "anotherdict": {"hello" : "hi"}
}
print(mydict['fast'])
mydict['marks'] = ['78,89,96']
print(mydict)
print(list(mydict.keys()))
print(mydict.items())
print(mydict.values())
updatedict = {
    "car" : "Means of transport",
    "current" : "charge per unit time"
}
mydict.update(updatedict)
mydict.update({"dancer" : "Aperson who dances"})
print(mydict.update)
print(mydict.get("harry")) # will give the value of harry

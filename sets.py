## also used to store variors items in asingke variables .
## use { } , ## are unordered ##(i.e. can't be indexed)
##no duplications are allowed , ## still new thinge can be added or removed.

a = {1,2,3,4} 
print(type(a))

# the repeated elements are not printed here  ## no repetition is allowed
a = {1,2,3,4,1}
print(a)
 # this syntax will create an empty dict. in place of empty set 
a = {} 
print(type(a)) 
## constructor method :-
t = (20, 30.1, "hello",True)
d=set(t)

# to have an empty set we have :-

b = set()
print(type(b))

# set methods :-

b.add(6) # will add the element 6 in the empty set b
b.add(5)
b.add(5)# won't add 5 twice , as repetition is not allowed
 #b.add[4,5,6] # we can't add list here as list canbe changed later on 

b.add((2,6,8,9))  # but we can add tuple as it can't be changed

 
#b.add({ "apple":"a fruit"})  can't add dict alson as it can also be changed
print(b)

 # length of a set 
print(len(b))

 # remove an elemnet 
b.remove(6) 
# if we try to remove something which is not there , error comes
 #b.remove(678) 
  
  # to remove one item and then return , the removed one , we can't write anything inside the pop one , ye khud se hta deta hai kisi ko bhi :)
print(b.pop()) ## will give the removed item
## to delete it completely :-
b.discard
print(d)
b.clear # won't give anything
print(b)

#  for union of two sets :-
a = {1,2,4,6,7} 
b = {3,6,7,8,9}  
print("union of the sets a and b is: ", a|b)
c = a.union(b)
print(c)
print("intersectionof a and b is:" , a&b)
d = a.intersectio(b)
print(d)
print("the difference of set a and b is:" , a-b)
print("the symmetric diff. of a and b is :" , a^b) # jo common wale honge items unhe hta ke baki sab return kar dega

## can't have duplicates( basically the repeating values)

## we can loop through that if the value is prsnt or not :-
for x in a :
  print(x) 
      ## Or
  print(200 in a) ## gives either T or F  

  ## to add one set to another :-
c = {"hello" , 2 , 3.9, True}
d={"hi" , 4 , 55.6,False}
c.update(d)
print(c) 
e =[60,469,'list']
c.update(e)
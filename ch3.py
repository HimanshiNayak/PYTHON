b = 'himanshi'#string
c =" himanshi's phone " #the comma we strat for writing should be one we end with 
d = '''himanshi's and 
himanshi....
himanshi''' #mostly used for multiple lines .
print(b)
print(c)
print(d) 
#   concatenating (adding ) two strings together (+):-
greeting = "Good Morning , " # space after , is compulsory 
name ="Himanshi "
print(greeting + name )
 # OR ...
 
e= greeting + name 
print(e)
#slicing strings:- 
# always starts counting from 0 , 
f= "good"
print(f[0]) #always use the []
# we cant change any element , we can only find what is there on that place 
#eg :- f[3] = "r  , can't happen .
# to write more than one :- ## the position we write at last is excluded .
print(f[0:3]) # here only 0 , 1 ,2 are counted.
print(f[:2]) # blank is replaced by 0
print(f[0:]) #blank will be automatically becoming 3

## negative index :-
print(f[-4:-1]) # is the same as 0:3 # start counting from the r.h.s

##  skip values :-

print(f[0::3]) # will print every third alphabet after the zeroth one.
g=  "amazon"
print(g[0::2]) 


## string functions :-
print(len("amazon")) # we haveto write the whole world here.
print(len("google"))
story = "once upon a time there was a crow , who was very thirsty . he searched for water everwhere but didn`t get it ."
print(len("story"))
print(story.endswith("jhdchgd"))
print(story.endswith("it"))
# gives the no. of times the given element occurs in the function.
print(story.count("o"))
print(story.count("ea"))
print(story.capitalize()) # we have to leave it empty as it only capitalizes the first alphabet of the first word of thegiven string .
 # .find :_ the thing we between the "" , this fun. gives its value .
#the value here starts from 0 and if we write a word which is not there ,
# then it will give -1 for that.
# it will give only the no. at which that element comes for the first time .
print(story.find("was"))
print(story.find("peacock"))
print(story.find("once")) # but here we need to take care of the case .

print(story.replace("crow" , "peacock"))

# escape characters :-
story ="sea is big . \n ocean is even bigger"
print(story)
story = "Hi  guys , \n  My name is \t and i\'m a good boy \\ ."
print(story)




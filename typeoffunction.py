# used to convert one type of function to another .
a = "3454" #is a str
print(type(a))
# print(a+5) ,..... would give an error as its a string and we cant add an int to a string .
# but 
a = int(a) #this converts the a into a int 
print(type(a))
print(a+5)
# but 
b = "34jhhgdejgdsh78" # this is just a str , bcz its inside ""
## b= int(b) , is invalid bcz b can never be an int
c = 34.0
print(type(c)) # is a lfloat 
c = int(c) # gets converted to int
print(c +67)
d = 65
print(type(d))
d= float(d)
print(d + 2.0) # gives the answer without error
print(d + 5) # gives float as answer  , sice one was float
e = 31.6
e= int(e) 
print(e +5) # gives int as answer
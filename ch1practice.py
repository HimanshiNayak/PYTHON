# two add two numbers 
a = 3
b = 4 
print("the sum of a and b is " , a+b)
# remainder 
a = 45
b=3
print("the remainder when a is divided by b is " , a%b)
#check the type of the varible using input function 
a = input("enter something")
print(type(a)) # always str
  # comparison operators to see whether a is greater than b or not
  
a =34
b=80
print(a>b)
print(b>a)
a = input("enter a no.w")
b= input ("enter a no. z")
#print("the average of w and x is" , (w +x)/2 )#here the answer is wrong ,  because input one is always a str 
# we have to define first what is average . then we can do it
a = int(a)
b= int(b)
avg = (a+b)/2
print("the average of a and b is " , avg) # always a float
#
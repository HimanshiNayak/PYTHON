# it is  block of code thwt only runs or executes , when it is called.

## does only the task provided to it , while loop just repeates.
## we can't copy paste everytime . 
## so we use def function : 
## we don't have to type again and again , just call the function

def printText(): ## printtext is the name we gave to the func.  
    print("hello")
    print("hello")
    print("bye")
print(1)
printText()
print(2)
print(3)
print(4)
printText()
print(5)
printText()
print(6)

#def printName(john):
   # print('My name is'+ john)
#printName()
#() 
   ## repeats john evertime 
def printName(name):## we can't write more than 1 element
    print("My Name is "+ name)
printName("peter")
printName("abdul")## these names are called arguments
printName("abc")
printName("efg")


def printName(name, age):
    print("My name is "+ name+"my age is " , age)
printName("peter", "10")
printName("abdul","20")
printName("abc","30")
printName("efg","40")

def printnum(num1, num2):
    print(num1 + num2)
printnum(10 , 20)
printnum(30 , 40) ## the ones written after the def are called parameters , while the one we write below it , to print them are arguments


## arbitrary arguments :- when we are not sure about the no. of arguments that can be passed inside a function , add * to the parameter
# here we need to add a * to the parameter , here we get arguments in tuple form
def myName(*name):# name is parameter
    print("My name is " + name[1])   ## will give john, here we write index as without[ , error is there , now its a tuple so , we can use all tup.methods
    print("My name is " + name[2])   
    print("My name is " + name[3])

## keywords arguments
# we can send the argumensts in the form as key value pairs
def myName(name1, name2, name3):
            myName('john', 'peter','raj') ## in place of thesee two lines we can have 
                               ## print(name1="john" , name2='peter' and so on )
myName(name1='john' , name2='peter' ,name3='raj')
print("My name is  "+ name1  + name2 + name3)
## the keywords come in tuple type
## arbitrary keyword arguments


## no. of parameters and no.of arguments should be same . 
## arbitrary keyword arguments :- here we use ** , here we get arguments in dictionary form

def myName(**name):
    print(name)
    print("my name is " +name["name2"])

    myName(name1='john' , name2='peter' ,name3='raj')

## since we always need one argument , to not to get error
## so we have default parameter value 

def myFunc(age ='40'):
    print('My age is '+ age)

myFunc('10')
myFunc('20')
myFunc('30')

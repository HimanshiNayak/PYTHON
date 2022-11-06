## we can write dict inside a dict , strings , lists , no. 
myDict = {
    "Fast": "In a quick manner" ,
    "Apple": "A fruit" ,
    "Marks": [1,3,4,5] ,
    "anotherDict": {'apple' :'a fruit' },
    'ananotherDict': {'marks' : [1,3,5]} # these are called nested dictipnaries
}

print(myDict['Fast'])
print(myDict['Apple'])
print(myDict['Marks'])
print(myDict['anotherDict']['apple'])
print(myDict['ananotherDict']['marks'])

myDict['Marks']= [67,879]
print(myDict['Marks']) # will change the values as can't keep two values for 1
 

 ## how to fill inn  an empty dictionary 
myDict = {}
a = "key"
b = "lock"
c = "look"
d =  [1,2,3,4]
e = (1,5,6,9)
f = 6788
g = input("Enter your name user .\n")

myDict['key']       = 'chabhi'
myDict['lock']      = 'tala'
myDict['look']      = 'dekhna'
myDict['[1,2,3,4]'] = 'list'
myDict['(1,5,6,9)'] = 'tuple'
myDict['6788']      = 'int'
myDict['user']      = g
print(myDict)
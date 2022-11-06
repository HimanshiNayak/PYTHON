myDict = {
    "Fast": "In a quick manner" ,
    "Apple": "A fruit" ,
    "Marks": [1,3,4,5] ,
    "anotherDict": {'apple' :'a fruit' },
    'ananotherDict': {'marks' : [1,3,5]}
    } 
print(myDict.keys()) # will print all the keys 
print(list(myDict.keys())) # converts it into a list form 
print(myDict.values())
print(myDict.items()) # item prints all the keys along with their values 
# ho nwto update a dict . by adding a pair of key value at the last of the original dict
print(myDict)
updateDict = {
    "banana" : "a fruit" ,
    "hina" : "a name",
    "Apple" : "a vegetable" # will get updated
}
myDict.update(updateDict)
print(myDict) 

print(myDict.get("hina"))
print(myDict["hina"]) #  both will give the same thing here
# but ,
 
# if we write some ke which is not there in the dict , the get function will give the answer as None , 
print(myDict.get("school"))

# while the [] syntax will throw erroe as there was no such key inside our dictionary
print(myDict[school])
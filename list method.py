l1 =[1,6,9,345,86]
l2 =[5,78,8090,233]
# how to put them in inc order 
l1.sort()
print(l1)
l2.sort
print(l2)
# reverses the list 

l1.reverse()
print(l1) 
l2.reverse
print(l2)

# append the lsit  :- will add the given , at the end of the list .
l1.append(67)
print(l1)
l2.append(5678)
print(l2)

# insert in the list :- .insert(0 , 567) , the first no.is :- the position on which we need to insert the second no. written there
# counting starts from zero .
l1.insert(0 , 789)
print(l1)
l2.insert(1,5678)
print(l2)

# pop :- to remove some element 
l1.pop(4)
l2.pop(3)  # where 3 and 4 are the positions


 # use remove when we write the no. not the position .
l1.remove(67)
l2.remove(5)

# sum the elements of a list :-
l3 =[1,23,345,556] 
print(sum(l3)) 
# or print(l3[0]+l3[1]+l3[2]+l3[3])
 # to give the no. of occurancesof the given element 
t = (1,2,3,1,4,5)

print(t.count(1))

 # to know what is there on the given no. :

print(t.index(2))

## range of indexes
print(t[2:5])## will give the 2, 3, 4 place things .
print(t[-1::-6]) ## wrong , write it in inc order always 
print(t[-6:-1])
 ## how to update a tuple , as we can't changeit after witing .
## here we use the list to tuple conversion .
 

t1 = (10,"Hello",True ,None,20.1)
l1=list(t1)
l1[2]="Hi"
t1=tuple(l1)
print(t1)


t3=('apple','banana','guava',10,20.1,True,None)
l3=list(t3)
l3[5]=False
t4=tuple(t3)
print(t4)

## append tuple with another tuple :-
t4=(10,20,30,40)
x=(50,)
t4 = t4 + x 
print(t4)
# remove elements :- first ci=onvert  to a list then do it
t5 =(10,20,40,60,80,90,100)
l1=list(t5)
l1.remove(90) ## don't use []
t6=tuple(l1)
print(t6)

## Add something in a tuple :-
t6=(11,20,40,56,78)
l2=list(t6)
l2.append(86) 
t7=tuple(l2)
print(t7)
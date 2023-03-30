# list and tuple they have the following differences :-
# 1. here we use ()  
# 2. the elements of a tuple can't be manipulated 
#3. heterogenous ordered set

 #creating a tuple using ()
from multiprocessing.reduction import duplicate


t = (1,2,3) 
t1 = () # empty tuple 
 # t2 = (1 ) ;, wrong way to describe a tuple ,
t2 = (1 ,) 
t3= (2,6, "str",4.87)

 # printing the elements of a tuple :-
print(t[2]) 
print(t[-1])
print(t[1:4])
print(t1) 
print(t2)
# cannot update the values of a tuple :-
 ##t[0] = 34   # error is there 
print(t1+t2+t3) # we can't add it ,it jus t writes one after the other 
## here  the order matters as the one we give first , those elements will come first 
print(len(t))
print(t*3) ## to repeat a tuple
print((t*3)+(t3))
print(min(t))
##print(max(t3)) ## erro r as all are different
print(max(t))
 
 ## tuple can have duplicate values ;
t4 = (1,3,2,1,4,2,4,3) 
print(t4)


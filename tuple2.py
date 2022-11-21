##packing a tuple :- just giving values to it 
## unpacking :- we can extract the values int different variables .

num=(10 , 20 ,30) # packing
(num1,num2,num3)= num
print(num1) # unpacking 
print(num2)
print(num3) ## no. of variable should match the no. of items in tuple 
no=(30,60,70,80,100)
#(num1,num2,num3)=no ##if the no. of variables defined and the no. we unpack are differnt , error 
#print(num1)
#print(num2)
#print(num3)

## if we need to unpack only some use *

(num1,num2,*num3)=no
print(num1)
print(num2)
print(num3) ## adds rest in a list
 ## after the place we add * , everythinhg is listed.

 ## loops  
 # for loop 
t2= (2,6, "str",4.87)
for x in t2:
    print(x)
 
## looping through no. 
print(len(t2))
print(range(len(t2))) ##gives (0,4) . 4 not incl

for x in range(len(t2)):
    print(x) 

    ## joining tuples :-

t3 =(10, 20, 30)
t4=(40,50,60,70,80,90)
t5=t3+t4  ## the order in which the tup are written is the oder , they get combined in
print(t5)

## mul of tuple :-

t3 =(10,20,30)
t4 = t3^3
print(t4)



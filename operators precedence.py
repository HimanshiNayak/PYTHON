# multiplication has a higher precedence over sub./add
print(10-4*2)
print(10+4*4)
## ( ) has higher pre. over mult.
# if we want to do sub first :- use the brackets .
print((10-4)*2)
print((10+4)*4)

# associativity from [left to right]:- 
# when two operators have same precedence , then they will get operated from left to right .
print(5*2//3) #, we get 3  both have same precedence  ## here 3 is the ans
print(5//2*3)  # // just gives the numerical part   #3 here 6 is ans


print(2**3**3) ## 8 to the power 3
print(3**2**2) ##9 with power 2
print(2**3**1) ## 8 , but from right to left its 9

## exponent operator has right to left associativity.


#x==y
#x!=y 
#x>y
#x<y 
#x<=y 
#x>=y

x=23
y=30

if x>y:
    print('y is greater then x.')
else:
        print("y is smaller then x.")

if (100>=400):
    print("Hello")
else:
    print('Bye') 

    ##  one liner fpr if - else 
print('anyeong') if 10>=5 else print("ola")





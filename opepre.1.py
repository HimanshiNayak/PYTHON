x = 200
y = 500
z=2000
if x>y and z<y: ## checks if the condition is true
    print("Hello")
elif x<=y and y<=z:
    print("anyeong")
else :
     print("nihao")


a = int(input('Enter a no.\n'))
b= int(input("Enter another no.\n"))
c= int(input("Enter a different no.\n"))
if a>=0 and b>=500 and c>=1000:
    print("The no. lie between the range 0 -1000")
elif a<100 or b<500 or c<1000:
    print("the no. lies in the range 0-1000 , excluding 0 and 1000")
else :
    print("the no. doesnt lie in the above range.")

## nested if- else conditions

## one inside the other
x = int(input("Enter a no.\n"))
if (x<60):
    print("x is less than 60 .")
    if(x<50):
        print('x is also less than 50.')
    else :
        print("x is either equal to or greater than 50")
else:
    print("x is either equal to or greater than 60.")

if (x<5):
    pass ## use this to avoid error
else:
    print("hi")
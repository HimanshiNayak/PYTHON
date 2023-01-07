# ch1

# print("this is a \\\\ double backslash")
# print("this is /\\/\\/\\/\\ mountain")
# print("he is \t awesome")
# print("\\ \" \\n \\t \\ \'")

# ch2
# num1 = input("enter first no.")
# num2 = input("enter second no.")
# num3 = input("enter third no.")
# print(f'average of three no. is : {(int(num1))+ (int(num2)) + (int(num3))}')
# num1, num2, num3 =input("enter 3 no. seperated by commas 5").split(",")
# print(f'average of three no. is : {(int(num1))+ (int(num2)) + (int(num3))}')
#  withput strt ns stop argument , will give the whole string

# ch3
# name = input("Enter your name \n")
# print(name[::-1])

# name  , alphabet = (input("Enter your name and an alphabet seperated by commas \n").split(","))
# print(f"length of your name is {len(name)}")
# print(f"the no. repetion{name.count(alphabet)}") , is case sensitive , but we need case insensitive
# print(f"char count:{name.lower().count(alphabet.lower())}")
# print(f" char count: {name.strip().lower().count(alpabet.strip().lower())}")

# no.guessing:-


# num = int(input("Enter any no. in the range 0-100 :\n")) # winning no.16
# if num == 16 :
#     print("You Won")
# if  0<=num<=15 :
#     print("Too Low.\n")
#     print("Better Luck Next Time .\n")
# else :# no condition with else
#     print("Too High.\n")
#     print("Better Luck Next Time .\n")

# watch coco
# name = input("Enter your name.\n")
# age =  int(input("Enter your age.\n"))
# if name[0]=="A"or name[0]=='a' and age >10 :
#     print("You can watch  coco movie.")
# else:
#     print(" Sorry ,you cannot watch coco.")

# # sum of n natural no.
# total = 0
# n = int(input("Enter a natural no.\n"))
# i = 1 ## always 
# while i <= n :
#     total +=i
#     i +=1
# print(f"the sum of {n} natural no. is",total)   ## when we write something out of " , use ","

# # problem :- ask user to input a a no. with more than 1 digit
#calculate the sum of its digits and print 

# steps :::---- 1. take input
                #  2. int(n[0])= ......int(len(N-1))
                # print

# n =input("Enter a no. with more than one digit in it.\n") 
# total = 0
# i = 0 # here 0 as we have to start from the 0 th position of the str
#while i< len(n) # bcz the len of the fun is 1 greater than the no. of dig present., cusz the digits startbform 0 and len from 1
    #total+=int(n[i]) # i.e total starts from the 0 th index of nn
#       i += 1
# print(total)

# #  ask user name
# print count of each alphabet and symbol

# logic : pahle name mein indexing , phir count , phir usse print

# name = input("Enter your name .\n")
# i = 0 
# while i <len(name):
    # print(f"{name[i]} : {name.count(name[i])} ")   # 1st name i for the alphabet and name i in count as we have to count the no. of times that index came in the str    # use format instead of makeing a new str for that and use placeholder
    # i += 1
    
    # now the problem is , its repeating many
    # for that create a variable , check if that is there in it, if not print
    # temp ko bhi aage bndaha hai like total

# name = input("Enter your name .\n")
# temp_var =""
# i = 0 
# while i <len(name):
    # if name[i] not in temp_var:

        # print(f"{name[i]} : {name.count(name[i])} ")  
        # temp_var +=name[i]
        # i += 1

  

# for loop 
# n= int(input("Enter a no."))
# total = 0
# i = 0
# for i in range(n): or range(1,n+1)
    # total +=i
    # print(total)
    # i+=1
# total =0
# num = (input())
# for i in range( 0,len(num)):
    # total += int(num[i])
    # print(total)
    # i+=1
  
# name , count , index aur name 

name = input("Enter your name ")
temp_var = " "
i = 0
# temp_var = ""
for i in range (0, len(name)):
    if name[i] not in temp_var:
        print(f"{name[i]} : {name.count(name[i])}")
        temp_var += name[i]
        i += 1


    















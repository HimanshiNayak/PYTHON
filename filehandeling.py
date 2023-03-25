# # file handeling
f = open("hello.txt","r")
data = f.read() # this line is to extract data or to show the data of the file
print(data)
f.close
f = open("hello.txt")
data = f.read()
print(data)
f.close

# or er can open a file as :
# f = open("file address","r")


# #  to read linewise linewise

# # first line
f = open("hello.txt","r")
data = f.readline()
print(data)

# # second line
data = f.readline()
print(data)

# # third line
data = f.read()
print(data)
f.close

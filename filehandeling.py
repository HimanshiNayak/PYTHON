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

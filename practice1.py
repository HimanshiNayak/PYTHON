class Person:
    name = "harry"
    occupation= "software developer"
    networth = 10
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a= Person()
b= Person()
c= Person()
a.name = "subham"
a.occupation= "accountant"
b.name = "nikita"
b.occupation = "hr"

a.info()
b.info()
c.info()


# car modelname

class car:
    def __init__(self,modelname,year):
          self.modelname = modelname
          self.year = year
    def display(self):
        print(self.modelname , self.year)

c1 = car("toyota" , 2016)
c1.display()

# singer

class singer:
    no_of_fans = "millions"  ## class variable
    popularity  = "worldwide"
    
    def __init__(self,name,nationality,language): ## constructor
        self.name = name
        self.nationality = nationality
        self.language = language
    def display(self):    ## method
        print(f"{self.name} is  band from {self.nationality} they sing in {self.language}.")
  

a = singer("BTS","Korea","Korean")
b = singer("Blackpink","Korea","Korean")
c = singer("TXT","Korea","korean")

a.display()
a.popularity = "indian" ## can be changed like , this , but will be changed for particular obj
print(a.popularity)
print(a.no_of_fans)
singer.no_of_fans = "billions" ## to change this we use class itself
b.display()
print(b.no_of_fans)
print(b.popularity)
c.display()

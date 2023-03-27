# instance methods
# like pop and all                                        

class Person:
    def __init__(self ,firstname , lastname , age):
           self.firstname = firstname
           self.lastname = lastname 
           self.agename = age
def full_name(self):
    return f"{self.firstname}  {self.lastname}"

p1 = Person('ghjgd','hgsfd',24)

print(full_name(p1))

# 
class Hello1:
    def __init__(self,hindi,english , korean):
        self.hindi= hindi
        self.english = english
        self.korean = korean

def correction(self):
    return ( f"{self.hindi}" "huukkh" )


l1 =Hello ('namaste','hi','annyeong')
l2 =Hello('kaun','who','dugusaye')
print(correction(l1))


# class variable: common wale ko barr barr na likhna pdhe toh

class circle:
    pi = 3.14
    def __init__(self , radius):
        self.radius = radius
        
    def calc_circumference(self):
        return 2*circle.pi*self.radius

c = circle(4)
c1 = circle(2)
print(c.calc_circumference())

class laptop:
    discount = 10
    def __init__(self, brandname,price):
        self.brandname = brandname
        self.price = price
    
    def discount(self):
        off_price
        off_price =(laptop.discount/100)*self.price
        return self.price - off_price

laptop1 = laptop('hp',66000)
laptop2 = laptop('dell',55000)
print(laptop1.discount())
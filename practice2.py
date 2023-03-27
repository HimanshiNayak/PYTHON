# instance variable :-diferent for each

class Person:
    na = 1.5

    def __init__(self ,firstname , lastname , age,salary):
           self.firstname = firstname
           self.lastname = lastname 
           self.agename = age
           self.salary = salary
    def increment(self):
        self.salary = int(self.salary *self.increment)

p1 = Person('rani','newton',18,100000)
p2 = Person('selena','cruise',19,1000000)
print(p1.firstname)
print(p1.salary)
print(p1.increment)

class Hello:
    def __init__(self,hindi,english , korean):
        self.hindi= hindi
        self.english = english
        self.korean = korean

l1 =Hello ('namaste','hi','annyeong')
l2 =Hello('kaun','who','dugusaye')

print(l1.hindi)

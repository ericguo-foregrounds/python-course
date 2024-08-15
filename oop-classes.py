# In python, we can find the type of an object using
x = 9
y = "hello"
z = False

print(type(x), type(y), type(z))

# These are all instances of the int class, string class, and boolean class, respectively.
# methods are attributes of an object
print(y.upper()) # upper method of string object. We cannot do x.upper() bc no attribute upper exists for the int class.

# let's define a class named dog
class Dog:
    # __init__ or constructor
    def __init__(self, name, age):
        self.name = name # creates attribute called name
        self.age = age
    # let's define a method called bark
    # for each method we must define a self parameter as when it is called the object itself invisibly gets passed in
    def bark(self):
        print("WOOF!")

    def add_one(self, x):
        return x + 1
    
    # getter method
    def get_name(self):
        return self.name
    
    # setter method
    def set_name(self, name):
        self.name = name
    
d = Dog("Billy", 6)
print(type(d)) # class Dog main module
d.bark()
print(d.get_name())
d.set_name("Bill")
print(d.get_name())

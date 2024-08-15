# to define a function use def keyword
def func():
    print("I am a function")

func() # calls function, code inside function runs

# function with arguments
def multiply(x, y):
    return x * y # and return things

print(multiply(5, 6))

# you can return multiple things
def calculator(x, y):
    return x + y, x - y, x * y, x / y # this will return a tuple

add, sub, mult, div = calculator(5, 6) # destructure the tuple
print(add, sub, mult, div)

# default params
def n(x, y, z=""):
    print(x, y, z)

n(5, 6)
n(5, 6, 7)

# Functions are objects in python, which means we can return them
def func_maker():
    def func():
        print("I was created by func_maker")

    return func # returns the function

func2 = func_maker()
func2()

# another way
func_maker()() # calls the function that is returned

# unpack operator
# Let's say you have a list
x = [1, 2, 3, 4, 5, 6, 7]
# the unpack operator * takes out each element and passes it in as an argument
print(*x)

# Here's an example with functions and Tuples
def exponentiate(base, exponent):
    x = 1
    for i in range(exponent):
        x *= base

    return x

list = [(2, 3), (3, 2), (4, 2), (2, 5)]

for pair in list:
    print(exponentiate(pair)) # unpacks each tuple and passes in the two numbers as the args
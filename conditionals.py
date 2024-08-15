x = "Hello"
y = "Hello"
a = 7
b = 7.0
c = 7.5

# Conditional operators
print(x == y) # True

print(a > c) # False
print(a == b) # True
print(a + 2 > c) # True you can add arithmetic expressions on a side of an operator

result = 6 == 6.0
print(result) # True

# chained conditionals
result1 = True
result2 = False
result3 = False

print(not result3) # True - not flips whatever is on its right
result4 = result3 or not result1 # changes result1 from True to False
print(result4) # False

print(result1 and result2) # False

# order of operations: not, and/or whichever comes first
print(False or not True and True) # False!

name = input("Name: ")
if name.lower() == "eric": 
    print("Hi Eric")
elif name == "Bob":
    print("Bob the Builder")
else:
    print(name, "I don't know you")
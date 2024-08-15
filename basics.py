# data types
# int
40590
-8899

# float
297.0
-9.8

# string - anything surrounded by single or double quotes
"hello"
'hello'
'4.6'

# boolean - must be capitalized in Python - unlike java and javascript
True # 1
False # 0

# printing
print("Hello World")
print(4.5)
print(4.5, "Hello", False)

# end at print - default behavior is to go onto a new line, however, can prevent that thru
print("Hello", 4.5, False, end="")
print("ad;kl")

# this will print Hello 4.5 Falsead;kl

# variable - name = value
# variable conventions: use snake case like hello_world instead of helloWorld (camel case). 
# rules: cannot start with a number (ex. 9hello) or use any other special characters other than underscore (ex. hello*world)
num = 10
print(num)
world = "world"
print(world)

first = "eric"
last = "guo"
last = first
print(last)
first = "tim" # last should not change bc last was set to first when first = "eric"
print(last)

# user input
# name = input("Name: ")
# print(name)
# last = input("Last name: ")
# print("Hello", name, last)

# arithmetic operators
# Note: make sure the data types on the left and right sides are the same or both numbers
# Note: if there is a float on one side of an operator, you will get a float back
# division - will always result in a float
result = 9 / 3 # 3.0
print(result)
# casting to int
print(int(result))
# or, floor diviision
result = 9 // 3
print(result)

# exponents
x = 4
y = 2
print(x**y) # 16

# mod - returns a remainder
y = 3
print(x % y) # 1

num = input("Number: ") # input will always convert input into string
print(int(num) - 5) # so we must cast it to an int

# String methods
str = "Hello"
# uppercase
print(str.upper()) # HELLO
# lowercase
print(str.lower()) # hello
# capitalize and format
str2 = "heLLO World"
print(str2.capitalize()) # Hello world5

# String length - use len()
print(len(str)) # 5

# count() to see if there is a substring within a string - returns number of times found
print(str2.count('ll')) # 0
print(str2.lower().count('ll')) # 1

# String operations
# concatenation (addition)
str3 = "Hi"
str4 = "yes"
z = 5
print(str3 + str4) # Hiyes
# print(str3 + z + str4) cannot do

# multiplication - repeats the string z times
print(str4 * z) # yesyesyesyesyes
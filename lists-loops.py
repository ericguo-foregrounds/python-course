# list
arr = [4, "Hello", True] # do not need to be the same type

# methods
print(len(arr)) # gives length of list - 3

arr.append("fjfjfjfjfjf") # adds this to the end of the list
print(arr)

arr.extend([1, 2, 3, "a", "b", "c"]) # adds this new list to the end of list arr
print(arr)

last_element = arr.pop() # pop removes last element and returns it
print(last_element)
print(arr)

# accessing elements by index
list2 = ["joe", "ann", "matthew", "richard", "sarah"]
print(list2[3]) # richard

list2.pop(3) # removes element in index 3. Bye Richard!
print(list2)

# changing element by index
list2[1] = "anna"
print(list2) # ann has been replaced by anna. Lists are mutable.

# Tuples - use round brackets instead of square brackets. Tuples are immutable!
tup = (1, 2, 3, "hello", "yes")
print(tup[0])
# Cannot reassign elements, or append, or pop, or extend.

# Slice operator - forms a substring or a part of a list or Tuple
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# the slice operator can take up to three arguments [start:stop:step], for example
sliced1 = x[1:6:2] # has a start of index 1, stop of index 6 (will not include index 6) and step of 2
print(sliced1) # [1, 3, 5]
sliced2 = x[:6] # stops at 6
print(sliced2)
sliced3 = x[1:] # starts at 1
print(sliced3)
# you can also go backwards
sliced4 = x[4:2:-1] # [4, 3]
print(sliced4)
# to reverse a list
print(x[::-1]) 
# slice on strings
s = "Happy Birthday"
print(s[2:9:3])
print(s[::-1])
# for loop - always for i in something (we can use range to print out number 0 thru 9)
for i in range(10):
    print(i)
# the range() function creates a collection of numbers and can take up to 3 values, start, stop, step
# if only one value is passed in, then that's the stop
range(10) # starts at 0 and increments by 1 but does not include 10
range(2, 10) # two arguments: start, stop. Example
range(10, 1, -1) # three arguments: start, stop, step. Step can be positive or negative.

# iterating thru a list
for i in [3, 4, 2, 5, 6, 7, 1]: # this will print every element of the list
    print(i)

# another way to iterate thru a list - similar to how we do it in javascript
list3 = [3, 4, 2, 5, 6, 7, 1]
for i in range(len(list3)):
    print(list3[i])

# another way - to print element index and then element
for i, element in enumerate(list3):
    print(i, element)

# while loop - will run while condition == True
i = 0
while i < 10:
    print(i)
    i+=1 # no i++ in python

# or can use a break statement
j = 0
while True:
    print(j)
    j+=1
    if j == 10:
        break
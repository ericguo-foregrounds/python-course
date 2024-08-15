# For lists, if we remove the first element, all of the other elements shift position.
# ORder does not exist in sets.
# Use sets when you don't care about the order of elements, you only want to know if an element exists.
s = {4, 32, 2} # this is a set
# empty set
e = set()
print(type(e)) # must use set constructor
print(type({})) # this is not a set by a dictionary!

# no duplicate elements in set
x = {2, 12, 12, 15, 16, 15, 17, 9, 0, 1, 2, "hello", "hi", "hello"}
print(x) # will order them and remove duplicates

# adding elements
x.add(5)
print(x)
x.remove(2)
print(x)

# to check if element is in set
print(12 in x) # True

# other operations
s2 = {6, 7, 8, 9, 10, 11}
print(x.union(s2)) # union of sets as a new set - basically adds the two together
# can also do other math operations with sets

# dicts - these are kinda like Javascript objects and JSON objects as they have key value pairs
d = {'key': 4}

# add a key
d['key2'] = 5
print(d)

# another example
d[3] = "bye"
print(d)
#This does not work
# d[g] = "jjj" g is not defined. Unlike JS objects.

# how to get a list with the values
print(list(d.values()))

# how to get a list with all the keys
print(list(d.keys()))

# how to delete a key
del d["key2"]
print(d)

# Looping over
print(list(d.items())) # this returns a list with both keys and items in Tuples
for key, value in d.items():
    print(key, value)

# another way
for key in d:
    print(key, d[key])

# destructuring
arr = [1, 2, 3]
# say I want to assign each element inside this list to a variable
a, b, c = arr
print(a, b, c) # a = 1, b = 2, c = 3




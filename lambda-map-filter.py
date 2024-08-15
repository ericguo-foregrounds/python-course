# Lambda is an anonymous one-line function, similar to an arrow function x => x+ 2 in Javascript
# Used in callbacks

x = lambda x: x+2
print(x(7)) # 9

f = lambda x, y: x + y
print(f(3, 4)) # 7

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Let's say we want to create a new list but with each of the elements multiplied by 10
# map takes two arguments - one which is a callback function and the other is a which list you want to map. Returns a map object
mp = list(map(lambda num: num * 10, a))
print(mp)

# Let's say we only want even numbers now
# For filter, the lambda function must return True or False
evens = list(filter(lambda num: num % 2 == 0, a))
print(evens)

# Note: in both math and filter, the callback does not need to be a lambda
# lambda's body is a single expression, not a block of statements.
# we can quickly make ad-hoc functions without needing to properly define a function using def
#lambda arguments : expression

#ex1:
from Filter_function import square


print("-----------ex1--------------")
add = lambda a,b: a+b   # def add(a,b): return a + b
print(add(6,8))

#ex2:
print("-----------ex2--------------")
square = lambda x: x ** 2
print(square(8))

#ex3:lambda with filter
print("-----------ex3--------------")
numbers = [ 1, 2, 3, 4, 5, 6]
evev = list(filter(lambda x:x % 2 == 0, numbers))
print(evev)

#ex4:lambda with map
print("-----------ex4--------------")
numbers_1 = [ 1, 2, 3, 4]
result = list(map(lambda x:x ** 2, numbers_1))
print(result)


#Syntax of function
def my_function():
    print("Hello in a function")

#Call Frunction
my_function()

#Sum number by using return
def sum_number(x,y):
    return x+y
total = sum_number(5,7)
print(total)

print('-------------------------------')

# Arguments :By default, a function must be called with the correct number of arguments.
# Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments,
# not more, and not less
def sum_number(x,y):
    print (x+y)
total = sum_number(5,7)

print('-----------default_Arguments--------------------')

#type one_Default Parameter Value :If we call the function without argument, it uses the default value:
#ex1:
print('-----------default_Arguments:ex1--------------------')

def my_function(country = "Yemen"):
    print("I am from " + country)
my_function("Egypt")
my_function("Palestine")
my_function()

print('-----------default_Arguments:ex2--------------------')

#ex2:
def sum(a=10,b=30,c=100):
    print(a+b+c)
sum(16,70)
sum(4,90,-2)
sum()

print('-----------default_Arguments:ex3--------------------')

#ex3:
def details(device,price,disc=0):
    print(f'The price of the {device} is {price} and the discount is {disc}%')
details('TV',40)
details('Laptop',100,50)
#details('Cap')  #(TypeError)

print('--------------Keyword Arguments-----------------')

# Type Tow_Keyword Arguments :You can also send arguments with the key = value syntax.
# This way the order of the arguments does not matter.
def car(car1, car2, car3):
    print("The car is " + car3)
car(car1 = "Toyota", car2 = "Hyundai", car3 = "kia")

print('-------------Arbitrary Arguments------------------')

# Type Three_Arbitrary Arguments, *args : add a * before the parameter name in the function definition
# do that if you do not know how many arguments that will be passed into your function
def Arbitrary_sum(*num):
    total=0
    for i in num:
        total=total+i
    print(total)    
Arbitrary_sum()
Arbitrary_sum(-3,4,5)
Arbitrary_sum(1,2,3,4,5)

print('-----------Arbitrary Keyword Arguments--------------------')

# Arbitrary Keyword Arguments, **kwargs :Python offers a way to handle arbitrary numbers of keyworded arguments.
# Instead of creating a tuple of values, **kwargs builds a dictionary of key/value pairs
def Keyword_Arguments(**Person):
    print("His last name is " + Person["lname"])
Keyword_Arguments(fname = "Ali", lname = "Hasan")

print('-----------Combination of variable length-----------------')

#Combination of variable length and other types of arguments
def types_of_argument(name,attempts=0,*scores):
    print(f'The person {name} do the exam {attempts} times and the results are:')
    for i in scores:
        print(i)    
types_of_argument('Ali',3,46,70,53)

print('-----------pass Statement--------------------')

#The pass Statement :function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.
def pass_function():
    pass

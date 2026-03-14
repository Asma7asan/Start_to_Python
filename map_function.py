# Allows you to " map " a function to an iterable object. 
# you can quickly call the same function to every item in an iterable
#ex1:
print("-----------ex1--------------")
def square(num):
    return num**2
my_nums = [1,2,3,4,5]
print(list(map(square,my_nums)))

#ex2:
print("-----------ex2--------------")
def check_even(num):
    return num%2==0   
nums = [0,1,2,3,4,5,6,7,8,9,10]
print(list(map(check_even,nums)))

#ex3:
print("-----------ex3--------------")
a = [1,2,3]
b = [4,5,6]
sum_num = map(lambda x,y: x+y, a,b)
print(list(sum_num))


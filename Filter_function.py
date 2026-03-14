# filter function syntax: filter(function,iterable)
# Meaning you need to filter by a function that returns either True or False.
#ex1:
print("-----------ex1--------------")
def square(num):
    return num%2==0
my_nums = [1,2,3,4,5]
print(list(filter (square,my_nums)))

#ex2:
print("-----------ex2--------------")
words = ["cat","dog","Lion","Tiger","Zebra"]
def long_word(word):
    return len(word) > 4
print(list(filter (long_word,words)))

#ex3:
print("-----------ex3--------------")
names = ["Ahmed","Ail","Lila","Lina","Arwa"]
def start_with_a(name):
    return name.startswith('A')
print(list(filter (start_with_a,names)))

#ex4:
print("-----------ex4--------------")
def greater_than_ten(number):
    return number > 10
numbers = [5,8,19,4,12]
print(list(filter (greater_than_ten,numbers)))


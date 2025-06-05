def modify(lst):
    lst.append(4)
   
numbers = [1, 2, 3]
modify(numbers)
print(numbers)

data = {'a': 1, 'b': 2}
data['c'] = data.get('a', 0) + data.get('b', 0)
print(data['c'])

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
       
print(factorial(4))

numbers = [1, 2, 3, 4, 5]
result = numbers.pop(2)
print(result, numbers)

def change_list(my_list):
    my_list = [10, 20, 30]
   
original = [1, 2, 3]
change_list(original)
print(original)

print('abc'.center(7, '*'))

def func(a=[], b={}):
    print(f"a={a}, b={b}")
func()


def func(a, b, *args, **kwargs):
    print(len(args) + len(kwargs))
   
func(1, 2, 3, 4, x=5, y=6)

for i in range(5):
    if i % 2 == 0:
        pass
    else:
        print(i, end=" ")
        
words = ["hi" if i % 2 == 0 else "hello" for i in range(4)]
print(words)

data = {'a': 1, 'b': 2}
data['c'] = data.get('a', 0) + data.get('b', 0)
print(data.items())

def modify_list(lst):
    lst.append(4)
    lst = [7, 8, 9]
    return lst

my_list = [1, 2, 3]
new_list = modify_list(my_list)
print(my_list, new_list)

my_dict = {'a': 1, 'b': 2}
my_dict.setdefault('c', 3)
print(my_dict)

text = "Python"
print(text.ljust(10, '*'))

def greet(name, message="Hello"):
    return f"{message}, {name}!"
   
print(greet("John", message="Hi"))

fruits = ['apple', 'banana', 'cherry']
print('apple' in fruits)

data = {'a': 1, 'b': 2}
print(data.get('c', 3))
print(data)

my_list = [1, 2, 3]
my_list.insert(10, 4)
print(len(my_list))

def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

my_counter = counter()
print(my_counter())
print(my_counter())
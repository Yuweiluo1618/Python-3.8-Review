# map
list1 = [1, 2, 3, 4]


def func(x):
    return x ** 2


result = map(func, list1)


print(result)
print(list(result))
print(list1)

#reduce
import functools

def func1(a, b):
    return a+b

result = functools.reduce(func1, list1)
print(result)

#filter

def func2(a):
    return a % 2 == 0

result = filter(func2, list1)
print(result)
print(list(result))

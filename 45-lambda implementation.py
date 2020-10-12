fn1 = lambda a, b: a+b
print(fn1(1,2))

fn2 = lambda: 100
print(fn2())

fn3 = lambda a,b=100: a+b
print(fn3(100))

fn4 = lambda *args: args
print(fn4(10,220))

fn5 = lambda **kwargs: kwargs
print(fn5(name='python'))

fn6 = lambda a, b: a if a > b else b
print(fn6(2,1))
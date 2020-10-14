#任意两个数字在整理后求和
def sum_num(a, b, f):
    return f(a)+f(b)

result = sum_num(-5,7,abs)
print(result)



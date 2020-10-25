try:
    f = open('exception.txt', 'r')

except:
    f = open('59-exception.txt', 'w')

try:
    print(num)

except NameError:

    print("fault")


try:
    print(1/0)

except (ZeroDivisionError, NameError):
    print('error')


try:
    print(num)

except (NameError, ZeroDivisionError) as result:

    print(result)
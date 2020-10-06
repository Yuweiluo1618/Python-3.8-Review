#位置参数
def user_info(name, age, gender):
    print(f"{name}{age}{gender}")

user_info("hi", "hi", 'hi')

#关键字参数

#默认参数
def user_info1(name, age, gender = '男'):
    print(f"{name}{age}{gender}")
user_info1(1,2)

#不定长参数
#包裹位置传递
def user_info2(*args):
    print(args)

user_info2('tom')

#包裹关键字传递
def user_info3(**kwarg):
    print(kwarg)


user_info3(name='tom')

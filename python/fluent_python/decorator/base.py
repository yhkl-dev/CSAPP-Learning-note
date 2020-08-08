'''
    装饰器是可调用的对象，其参数是另一个函数（被装饰的函数），
    装饰器可能会处理被装饰的函数，然后把它返回，或者将其替换成另一个
    函数或可调用对象

'''


def deco(func):
    def inner():
        print("running inner()")
    return inner


@deco
def target():
    print("running target()")


target()

'''
    Python 何时执行装饰器

    装饰器的一个关键特性就是，他们再被装饰的函数定义后立即执行
    这通常是在模块加载时

'''

registry_list = []


def registry(func):
    print('running register(%s)' % func)
    registry_list.append(func)
    return func


@registry
def f1():
    print('running f1()')


@registry
def f2():
    print('running f2()')


def f3():
    print('running f3()')


def main():
    print("running main()")
    print('registry ->', registry_list)
    f1()
    f2()
    f3()


if __name__ == "__main__":
    main()

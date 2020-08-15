class Demo:

    '''
        classmethod,
        定义操作类，而不是操作实例的方法，classmethod改变了调用方法的方式
        因此类方法的第一个参数是类本身, 而不是实例
        classmethod最常见的用途是定义备选构造方法

        staticmethod装饰器也会改变方法的调用方式，但是第一个参数不是特殊的值
        其实，静态方法就是普通的函数，只是碰巧在类的定义体中，而不是在模块层定义
    '''
    @classmethod
    def klassmeth(*args):
        return args

    @staticmethod
    def statmeth(*args):
        return args


if __name__ == "__main__":
    print(Demo.klassmeth())
    print(Demo.klassmeth('spam'))
    print(Demo.statmeth())
    print(Demo.statmeth('spam'))

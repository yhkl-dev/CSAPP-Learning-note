'''
    Python 不能像Java那样使用private修饰符创建私有属性，
    但是Python有个简单的机制，能避免子类意外覆盖‘私有’属性

    举个例子：有人编写了一个名为Dog的类，这个类的内部用到了
    mood实例属性，但是没有将其开放
    现在你创建了Dog的子类：Beagle. 如果你再毫不知情的情况下
    有创建了名为mood的实例属性，那么再继承的方法中就会把Dog
    类的mood属性覆盖掉，这是个难以调试的问题

    为了避免这种情况，如果以__mood的形式（两个前导下划线）
    尾部没有或者最多有一个下划线，命令实例属性，Python会把
    属性名存入实例的__dict__类，而且会在前面加上一个下划线和类名
    ，因此。对Dog 类来说 __mood会变成 _Dog__mood 对Beagle类来说
    会变成_Beagle_mood，这个语言特性叫做名称改写（name managing）

    名称改写是一种安全措施，不能保障万无一失，它的目低是避免意外访问
    不能防止故意做错事


    绝对不要使用两个前导下划线，这是很烦人的自私行为，如果担心名称冲突
    应该明确使用一种名称改写方式（如_MyThing_blahblab）, 这其实与使用
    双下划线一样，不过自己定的规则比双下划线易于理解
'''


class Dog:

    def __init__(self, name):
        self.name = name

    def __mood(self):
        print("in dog")


class Beagle(Dog):

    def __init__(self, name):
        super(Beagle, self).__init__(name)

    def __mood(self):
        print('in beagle')


if __name__ == "__main__":
    b = Beagle('tina')
    print(b.__dict__)
    print(b._Beagle__mood())

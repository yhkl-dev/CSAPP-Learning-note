class Number(object):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def reducible(self):
        return False


class Add(object):
    
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return "{} + {}".format(str(self.left), str(self.right))

    def reducible(self):
        return True

    def reduce(self):
        if self.left.reducible():
            return Add(self.left.reduce(), self.right)
        if self.right.reducible():
            return Add(self.left, self.right.reduce())
        else:
            return Number(eval(self.__str__()))


class Multiply(object):

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return "{} * {}".format(str(self.left), str(self.right))

    def reducible(self):
        return True

    def reduce(self):
        if self.left.reducible():
            return Multiply(self.left.reduce(), self.right)
        if self.right.reducible():
            return Multiply(self.left, self.right.reduce())
        else:
            return Number(eval(self.__str__()))

if __name__ == "__main__":
    print(Add(
        Multiply(Number(1), Number(2)),
        Multiply(Number(4), Number(3)
    )))
    print("-" * 20)
    expression = Add(
        Multiply(Number(1), Number(2)),
        Multiply(Number(3), Number(4))
    )
    print(expression.reducible())
    expression = expression.reduce()
    print("expression", expression)
    print(expression.reducible())
    expression = expression.reduce()
    print("expression", expression)
    print(expression.reducible())
    expression = expression.reduce()
    print("expression", expression)
    print(expression.reducible())




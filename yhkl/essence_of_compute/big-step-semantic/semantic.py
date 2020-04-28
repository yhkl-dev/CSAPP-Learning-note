class Number(object):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def evaluate(self, environment):
        return eval(self.__str__())

class Boolean(object):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def evaluate(self, environment):
        return eval(self.__str__())

class Variable(object):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def evaluate(self, environment):
        return environment[self.name]


class Add(object):

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return "{} + {}".format(str(self.left), str(self.right))

    def evaluate(self, environment):
        return Number(self.left.evaluate(environment) +
                      self.right.evaluate(environment))

class Multiply(object):

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return "{} * {}".format(str(self.left), str(self.right))


class LessThan(object):

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return "{} < {}".format(self.left, self.right)



class DoNothing(object):

    def __str__(self):
        return "do-nothing"

    def eq(self, other_statement):
        return isinstance(other_statement, DoNothing)



class Assign(object):

    def __init__(self, name, expression):
        self.name = name
        self.expression = expression

    def __str__(self):
        return "{} = {}".format(self.name, self.expression)


class If(object):

    def __init__(self, condition, consequence, alternative):
        self.condition = condition
        self.consequence = consequence
        self.alternative = alternative

    def __str__(self):
        return "if ({}) ({}) else ({})".format(self.condition, self.consequence,
                                               self.alternative)


class Sequence(object):

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __str__(self):
        return "{}; {}".format(self.first, self.second)


class While(object):

    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

    def __str__(self):
        return "while (%s) { %s }" % (self.condition, self.body)


if __name__ == "__main__":
    print("aaa")

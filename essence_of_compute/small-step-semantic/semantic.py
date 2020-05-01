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

    def reduce(self, environment):
        if self.left.reducible():
            return Add(self.left.reduce(environment), self.right)
        if self.right.reducible():
            return Add(self.left, self.right.reduce(environment))
        else:
            return Number(eval(str(self.left)) + eval(str(self.right)))


class Multiply(object):

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return "{} * {}".format(str(self.left), str(self.right))

    def reducible(self):
        return True

    def reduce(self, environment):
        if self.left.reducible():
            return Multiply(self.left.reduce(environment), self.right)
        if self.right.reducible():
            return Multiply(self.left, self.right.reduce(environment))
        else:
            return Number(eval(str(self.left)) * eval(str(self.right)))


class Boolean(object):
    
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def reducible(self):
        return False


class LessThan(object):

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return "{} < {}".format(self.left, self.right)

    def reducible(self):
        return True

    def reduce(self, environment):
        if self.left.reducible():
            return LessThan(self.left.reduce(environment), self.right)
        elif self.right.reducible():
            return LessThan(self.left, self.right.reduce(environment))
        else:
            print(Boolean(eval(self.__str__())))
            return Boolean(eval(self.__str__()))


class Variable(object):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def reducible(self):
        return True

    def reduce(self, environment):
        return environment[self.name]


class DoNothing(object):

    def __str__(self):
        return "do-nothing"

    def eq(self, other_statement):
        return isinstance(other_statement, DoNothing)

    def reducible(self):
        return False


class Assign(object):

    def __init__(self, name, expression):
        self.name = name
        self.expression = expression

    def __str__(self):
        return "{} = {}".format(self.name, self.expression)

    def reducible(self):
        return True

    def reduce(self, environment):
        if self.expression.reducible():
            return [Assign(self.name, self.expression.reduce(environment)),
                    environment]
        else:
            environment[self.name] = self.expression
            return [DoNothing(), environment]

class If(object):

    def __init__(self, condition, consequence, alternative):
        self.condition = condition
        self.consequence = consequence
        self.alternative = alternative

    def __str__(self):
        return "if ({}) ({}) else ({})".format(self.condition, self.consequence,
                                         self.alternative)

    def reducible(self):
        return True

    def reduce(self, environment):
        if self.condition.reducible():
            return [If(self.condition.reduce(environment), self.consequence, self.alternative), 
                    environment]
        else:
            if eval(str(self.condition)):
                return [self.consequence, environment]
            else:
                return [self.alternative, environment]


class Sequence(object):

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __str__(self):
        return "{}; {}".format(self.first, self.second)

    def reducible(self):
        return True

    def reduce(self, environment):
        if DoNothing().eq(self.first):
            return [self.second, environment]
        else:
            reduce_first, reduce_environment = self.first.reduce(environment)
            return [Sequence(reduce_first, self.second), reduce_environment]


class While(object):

    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

    def __str__(self):
        return "while (%s) { %s }" % (self.condition, self.body)

    def reducible(self):
        return True

    def reduce(self, environment):
        return [If(self.condition, Sequence(self.body, self), DoNothing()), environment]



if __name__ == "__main__":
    environment = {"x": Number(2)}
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
    expression = expression.reduce(environment)
    print("expression", expression)
    print(expression.reducible())
    expression = expression.reduce(environment)
    print("expression", expression)
    print(expression.reducible())
    expression = expression.reduce(environment)
    print("expression", expression)
    print(expression.reducible())

    print("-" * 10)
    statement = Assign("x", Add(Variable("x"), Number(1)))
    print("statement", statement)   
    statement, environment = statement.reduce(environment)
    print("statement", statement)   
    statement, environment = statement.reduce(environment)
    print("statement", statement)   

    print("Boolean", Boolean(True))
    print("Boolean", Boolean(False))

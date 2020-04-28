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
        return Number(int(str(self.left.evaluate(environment))) +
                      int(str(self.right.evaluate(environment)))).evaluate(environment)


class Multiply(object):

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return "{} * {}".format(str(self.left), str(self.right))

    def evaluate(self, environment):
        return Number(int(str(self.left.evaluate(environment))) *
                      int(str(self.right.evaluate(environment)))).evaluate(environment)


class LessThan(object):

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return "{} < {}".format(self.left, self.right)

    def evaluate(self, environment):
        return Boolean(int(str(self.left.evaluate(environment))) < int(
            str(self.right.evaluate(environment)))).evaluate(environment)


class DoNothing(object):

    def __str__(self):
        return "do-nothing"

    def eq(self, other_statement):
        return isinstance(other_statement, DoNothing)

    def evaluate(self, environment):
        return environment


class Assign(object):

    def __init__(self, name, expression):
        self.name = name
        self.expression = expression

    def __str__(self):
        return "{} = {}".format(self.name, self.expression)

    def evaluate(self, environment):
        environment[self.name] = self.expression.evaluate(environment)
        return environment


class If(object):

    def __init__(self, condition, consequence, alternative):
        self.condition = condition
        self.consequence = consequence
        self.alternative = alternative

    def __str__(self):
        return "if ({}) ({}) else ({})".format(
            self.condition, self.consequence, self.alternative)

    def evaluate(self, environment):
        if self.condition.evaluate(environment):
            return self.consequence.evaluate(environment)
        else:
            return self.alternative.evaluate(environment)


class Sequence(object):

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __str__(self):
        return "{}; {}".format(self.first, self.second)

    def evaluate(self, environment):
        return self.second.evaluate(self.first.evaluate(environment))


class While(object):

    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

    def __str__(self):
        return "while (%s) { %s }" % (self.condition, self.body)

    def evaluate(self, environment):
        if self.condition.evaluate(environment):
            self.evaluate(self.body.evaluate(environment))
        return environment


if __name__ == "__main__":
    print(Number(23).evaluate({}))
    print(Variable("x").evaluate({"x": Number(20)}))
    print(
        LessThan(
            Add(Variable("x"), Number(2)),
            Variable("y")
        ).evaluate({"x": Number(3), "y": Number(5)})
    )

    statement = Sequence(
        Assign("x", Add(Number(1), Number(1))),
        Assign("y", Add(Variable("x"), Number(3)))
    )
    print(statement)
    print(statement.evaluate({}))

    print("-" * 20)

    statement = While(
        LessThan(Variable("x"), Number(5)),
        Assign("x", Multiply(Variable("x"), Number(3)))
    )
    print(statement)
    print(statement.evaluate({"x": Number(1)}))

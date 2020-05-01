class Number:

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def to_py(self):
        return "lambda e: %s" % self.value


class Boolean:

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def to_py(self):
        return "lambda e: %s" % self.value


class Variable:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def to_py(self):
        return "lambda e: e['%s']" % self.name


class Add:

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return "{} + {}".format(str(self.left), str(self.right))

    def to_py(self):
        return "lambda e: ({})(e) + ({})(e)".format(self.left.to_py(),
                                                    self.right.to_py())


class Multiply:

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return "{} * {}".format(str(self.left), str(self.right))

    def to_py(self):
        return "lambda e: ({})(e) * ({})(e)".format(self.left.to_py(),
                                                    self.right.to_py())


class LessThan:

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return "{} < {}".format(self.left, self.right)

    def to_py(self):
        return "lambda e: ({})(e) < ({})(e)".format(self.left.to_py(),
                                                    self.right.to_py())


class DoNothing:

    def __str__(self):
        return "do-nothing"

    def eq(self, other_statement):
        return isinstance(other_statement, DoNothing)

    def to_py(self):
        return "lambda e: e"


class Assign:

    def __init__(self, name, expression):
        self.name = name
        self.expression = expression

    def __str__(self):
        return "{} = {}".format(self.name, self.expression)

    def to_py(self):
        return "lambda e: e.update({}=({})(e))".format(self.name,
                                                       self.expression.to_py())


class If(object):

    def __init__(self, condition, consequence, alternative):
        self.condition = condition
        self.consequence = consequence
        self.alternative = alternative

    def __str__(self):
        return "if ({}) ({}) else ({})".format(
            self.condition, self.consequence, self.alternative)

    def to_py(self):
        return "lambda e: ({})(e) if ({})(e) else ({})(e)".format(
            self.consequence.to_py(), 
            self.condition.to_py(),
            self.alternative.to_py())


class Sequence(object):

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __str__(self):
        return "{}; {}".format(self.first, self.second)

    
    def to_py(self):
        return "lambda e: ({})(({})(e))".format(
            self.second.to_py(),
            self.first.to_py())
    

class While(object):

    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

    def __str__(self):
        return "while %s: %s" % (self.condition, self.body)

    def to_py(self):
        return "lambda e: ({})(e) and ({})(e)".format(self.condition.to_py(),
                                                      self.body.to_py())

if __name__ == "__main__":
    print(Number(5).to_py())
    expression = eval(Number(5).to_py())
    print(expression)
    print(expression({}))
    print(Boolean(True).to_py())

    print("-" * 100)
    expression = Variable("x")
    print("expression", expression)
    print('expression.to_py', eval(expression.to_py()))
    proc = eval(expression.to_py())
    print(proc({"x": 1}))

    print("-" * 100)
    print(Add(Number(3), Number(4)).to_py())
    statement = eval(Add(Number(3), Number(4)).to_py())
    print(statement({}))

    print("-" * 100)
    print(LessThan(Add(Variable("x"), Number(1)), Number(2)).to_py())
    statement = eval(LessThan(Add(Variable("x"), Number(1)),
                              Number(2)).to_py())
    print(statement({"x": 2}))

    print("-" * 100)
    statement = Assign("y", Add(Variable("x"), Number(3)))
    print("statement: ", statement)
    print("statement: ", statement.to_py())
    exp = eval(statement.to_py())
    environment = {"x": 1}
    print(exp(environment))
    print(environment)
    print("-" * 100)
    statement = While(
        LessThan(Variable("x"), Number(5)),
        Multiply(Variable("x"), Number(3))
    )
    print(statement)
    print(statement.to_py())
    proc = eval(statement.to_py())
    print(proc)
    print(proc({"x": 3}))

from semantic import Number, Add, Multiply, LessThan, Variable


class Machine(object):

    def __init__(self, expression, environment):
        self.expression = expression
        self.environment = environment

    def step(self):
        self.expression = self.expression.reduce(self.environment)

    def run(self):
        while self.expression.reducible():
            print(self.expression)
            self.step()
        print(self.expression)


if __name__ == "__main__":
    Machine(
        Add(
            Multiply(Number(1), Number(2)),
            Multiply(Number(3), Number(4)),
        ),
        {}
    ).run()

    print("-" * 20)
    Machine(
        LessThan(Number(5), Add(Number(2), Number(10))),
        {}
    ).run()
    
    print("-" * 20)
    Machine(
        Add(Variable("x"), Variable("y")),
        {"x": Number(3), "y": Number(4)}
    ).run()

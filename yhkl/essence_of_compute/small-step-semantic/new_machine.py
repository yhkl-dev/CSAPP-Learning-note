from semantic import Number, Add, LessThan, Variable, Assign, If, \
        Boolean, DoNothing, Sequence, While, Multiply


class Machine(object):

    def __init__(self, statement, environment):
        self.statement = statement
        self.environment = environment

    def step(self):
        self.statement, self.environment = \
        self.statement.reduce(self.environment)

    def run(self):
        while self.statement.reducible():
            print(self.statement, self.environment)
            self.step()
        print(self.statement, self.environment)


if __name__ == "__main__":
    '''
    print(Number(2))
    print(Add(Number(2), Number(5)))
    print(LessThan(Number(5), Add(Number(2), Number(10))))
    print("-" * 20)
    print({"x": Number(2)})
    Machine(
       Assign("x", Add(Variable("x"), Number(1))),
        {"x": Number(2)}
    ).run()
    print("-" * 10)
    Machine(If(
        Variable("x"),
        Assign("y", Number(1)), 
        Assign("y", Number(2))
        ),
        {"x": Boolean(True)}
    ).run()
    print("-" * 10)
    Machine(If(
        Variable("x"),
        Assign("y", Number(1)), 
        DoNothing()
        ),
        {"x": Boolean(True)}
    ).run()
    print("\n")
    print("-" * 10)
    Machine(
        Sequence(
            Assign("x", Add(Number(1), Number(2))),
            Assign("y", Add(Variable("x"), Number(3)))
        ),
        {}
    ).run()
    '''
    print("-" * 10)
    Machine(
        While(
            LessThan(Variable("x"), Number(5)),
            Assign("x", Multiply(Variable("x"), Number(3))),
        ),
        {"x": Number(1)},
    ).run()

from semantic import Number, Add, LessThan, Variable, Assign, If, Boolean,DoNothing


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

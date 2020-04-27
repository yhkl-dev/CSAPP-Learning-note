from semantic import Number, Add, Multiply


class Machine(self):

    def __init__(self, expression):
        self.expression = expression

    def step(self):
        self.expression = self.expression.reduce()

    def run(self):
        while self.expression.reducible():
            print(self.expression)
            self.step()

        print(self.expression)

if __name__ == "__main__":


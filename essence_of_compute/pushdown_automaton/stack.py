class Stack(object):

    def __init__(self, contents):
        self.contents = contents

    def push(self, character):
        self.contents.append(character)
        return Stack(self.contents)

    def pop(self):
        self.contents.pop(-1)
        return Stack(self.contents)

    def top(self):
        return self.contents[-1]

    def __str__(self):
        return "#Stack ({})({})".format(self.top(),
                                        "".join(self.contents[:-1]))


if __name__ == "__main__":
    s = Stack(['a', 'b', 'c', 'd', 'e'])
    print(s.top())
    print(s.pop().pop().top())
    print(s.push("x").push('y').top())
    print(s.push("x").push('y').pop().top())

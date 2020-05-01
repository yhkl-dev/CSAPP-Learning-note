class Pattern(object):

    def __init__(self, precedence):
        self.precedence = precedence

    def bracket(self, outer_precedence):
        if self.precedence < outer_precedence:
            return "({})".format(self.__str__())
        else:
            return self.__str__()

#    def __str__(self):
 #       return "//"



class Empty(Pattern):

    def __init__(self):
        self.precedence = 3

    def __str__(self):
        return ''


class Literal(Pattern):

    def __init__(self, character):
        super(Pattern, self).__init__()
        self.character = character
        self.precedence = 3

    def __str__(self):
        return self.character


class Concatenate(Pattern):

    def __init__(self, first, second):
        super(Pattern, self).__init__()
        self.precedence = 1
        self.first = first
        self.second = second

    def __str__(self):
        return "|".join(list(map(self.bracket, [self.first, self.second])))


class Choose(Pattern):
    
    def __init__(self, first, second):
        super(Pattern, self).__init__()
        self.precedence = 0
        self.first = first
        self.second = second

    def __str__(self):
        print(self.precedence)
        return "|".join(list(map(self.bracket, [self.first, self.second])))


class Repeat(Pattern):
    def __init__(self, pattern):
        super(Pattern, self).__init__()
        self.precedence = 2
        self.pattern = pattern

    def __str__(self):
        print(self.precedence)
        return "*{}".format(self.pattern.bracket(self.precedence))

if __name__ == "__main__":
    pattern = Repeat(
        Choose(
            Concatenate(Literal("a"), Literal("b")), 
            Literal("a")
        )
    )
    print(pattern)

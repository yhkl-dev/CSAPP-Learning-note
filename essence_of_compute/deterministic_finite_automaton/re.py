class Pattern(object):

    def __init__(self, precedence):
        self.precedence = precedence

    def bracket(outer_precedence):
        if self.precedence < outer_precedence:
            return "({})".format(self.to_s())


class Empty(Pattern):

    def __init__(self):
        self.precedence = 3

    def to_s(self):
        return ''


class Literal(Pattern):

    def __init__(self, character):
        super(Pattern, self).__init__()
        self.character = character
        self.precedence = 3

    def to_s(self):
        return self.character


class Concatenate(Pattern):

    def __init__(self, first, second):
        super(Pattern, self).__init__()
        self.precedence = 1
        self.first = first
        self.second = second

    def to_s(self):
        return "|".join(list(map(self.bracket, [self.first, self.second])))


class Choose(Pattern):
    
    def __init__(self, first, second):
        super(Pattern, self).__init__()
        self.precedence = 0
        self.first = first
        self.second = second

    def to_s(self):
        return "|".join(list(map(self.bracket, [self.first, self.second])))


class 

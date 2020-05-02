from nfa import NFARulebook, NFADesign, FARule


class Pattern(object):
    precedence = 0

    def bracket(self, outer_precedence):
        if self.precedence < outer_precedence:
            return '({})'.format(self.__str__())
        else:
            return self.__str__()


class Empty(Pattern):
    precedence = 3

    def __str__(self):
        return ''

    def to_nfa_design(self):
        start_state = None
        accept_states = [start_state]
        nfa = NFADesign(start_state, accept_states, NFARulebook([]))
        return nfa


class Literal(Pattern):
    precedence = 3

    def __init__(self, character):
        self.character = character

    def __str__(self):
        return '{}'.format(self.character)
    
    def to_nfa_design(self):
        start_state = type('', (), {})()
        accept_states = type('', (), {})()
        rule = FARule(start_state, self.character, accept_states)
        rulebook = NFARulebook([rule])
        nfa = NFADesign(start_state, [accept_states], rulebook)
        return nfa


class Concatenate(Pattern):
    precedence = 1

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __str__(self):
        return "{}".format(''.join([self.first.bracket(self.precedence),
                                    self.second.bracket(self.precedence)]))


class Choose(Pattern):
    precedence = 1

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __str__(self):
        return "{}".format('|'.join([self.first.bracket(self.precedence),
                                     self.second.bracket(self.precedence)]))


class Repeat(Pattern):
    precedence = 2

    def __init__(self, pattern):
        self.pattern = pattern

    def __str__(self):
        return self.pattern.bracket(self.precedence) + "*"


if __name__ == "__main__":
    pattern = Literal('a')
    print("pattern", pattern)

    pattern = Concatenate(Literal('a'), Literal('b'))
    print("pattern", pattern)

    pattern = Repeat(
        Choose(
            Concatenate(Literal('b'), Literal('b')),
            Literal('a')
        )
    )

    print('pattern', pattern)
    
    nfa_design = Empty().to_nfa_design()
    print(nfa_design.is_accepting(""))
    print(nfa_design.is_accepting("a"))

    nfa_design = Literal('a').to_nfa_design()
    print(nfa_design.is_accepting(""))
    print(nfa_design.is_accepting("a"))
    print(nfa_design.is_accepting("b"))

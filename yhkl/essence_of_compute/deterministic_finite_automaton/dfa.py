class FARule(object):

    def __init__(self, state, character, new_state):
        self.state = state
        self.character = character
        self.new_state = new_state
    
    def applies_to(self, state, character):
        return self.state == state and self.character == character

    def follow(self):
        return self.new_state

    def __str__(self):
        return "#<FARule {} -- {} --> {}>".format(self.state, self.character,
                                                 self.new_state)


class DFARuleBook(object):
    
    def __init__(self, rules):
        self.rules = rules

    def next_state(self, state, character):
        return self.rule_for(state, character)

    def rule_for(self, state, character):
        for rule in self.rules:
            if rule.applies_to(state, character):
                return rule.follow()

class DFA(object):

    def __init__(self, current_state, accept_states, rulebook):
        self.current_state = current_state
        self.accept_states = accept_states
        self.rulebook = rulebook

    def is_accepting(self):
        return self.current_state in self.accept_states

    def read_character(self, character):
        self.current_state = self.rulebook.next_state(self.current_state,
                                                      character)

    def read_string(self, string):
        for char in string:
            self.read_character(char)


class DFADesign(object):
    def __init__(self, start_state, accept_states, rulebook):
        self.start_state = start_state
        self.accept_states = accept_states
        self.rulebook = rulebook

    def to_dfa(self):
        return DFA(self.start_state, self.accept_states, self.rulebook)

    def is_accepting(self, string):
        dfa = self.to_dfa()
        dfa.read_string(string)
        return dfa.is_accepting()


if __name__ == "__main__":
    rule_book = DFARuleBook(
        [
            FARule(1, 'a', 2), FARule(1, 'b', 1),
            FARule(2, 'a', 2), FARule(2, 'b', 3),
            FARule(3, 'a', 3), FARule(3, 'b', 3)
        ]
    )

    print(rule_book)
    print(rule_book.next_state(1, 'a'))
    print(rule_book.next_state(1, 'b'))
    print(rule_book.next_state(2, 'b'))
    print(DFA(1, [1, 3], rule_book).is_accepting())
    print(DFA(1, [3], rule_book).is_accepting())

    dfa = DFA(1, [3], rule_book)
    print(dfa.is_accepting())
    dfa.read_character("b")
    print(dfa.is_accepting())
    dfa.read_character("a")
    dfa.read_character("a")
    dfa.read_character("a")
    print(dfa.is_accepting())
    dfa.read_character("b")
    print(dfa.is_accepting())

    
    dfa = DFA(1, [3], rule_book)
    print(dfa.is_accepting())
    print("-" * 100)
    dfa.read_string("baaab")
    print(dfa.is_accepting())

    print("-" * 100)

    dfa_design = DFADesign(1, [3], rule_book)

    print(dfa_design.is_accepting("a"))
    print(dfa_design.is_accepting("baa"))
    print(dfa_design.is_accepting("baba"))



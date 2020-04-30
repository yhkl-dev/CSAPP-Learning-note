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

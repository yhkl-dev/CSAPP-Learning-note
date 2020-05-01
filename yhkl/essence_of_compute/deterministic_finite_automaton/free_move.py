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


class NFARulebook(object):

    def __init__(self, rules):
        self.rules = rules

    def next_state(self, states, character):
        return set(self.follow_rules_for(states, character))

    def follow_rules_for(self, states, character):
        return self.rule_for(states, character)

    def rule_for(self, states, character):
        state_list = []
        for rule in self.rules:
            for state in states:
                if rule.applies_to(state, character):
                    state_list.append(rule.follow())
        return state_list

    def follow_free_moves(self, states):
        more_states = self.next_state(states, None)

        if more_states.issubset(states):
            return states
        else:
            return self.follow_free_moves(more_states | states)


class NFA(object):
    
    def __init__(self, current_state, accept_state, rulebook):
        self.accept_state = accept_state
        self.rulebook = rulebook
        self.current_state = self.rulebook.follow_free_moves(current_state) 

    def is_accepting(self):
        return bool(self.current_state.intersection(self.accept_state))

    def read_string(self, string):
        for s in string:
            self.read_character(s)

    def read_character(self, character):
        self.current_state = self.rulebook.next_state(self.current_state,
                                                      character)


class NFADesign(object):

    def __init__(self, start_state, accept_state, rulebook):
        self.start_state = start_state
        self.accept_state = accept_state
        self.rulebook = rulebook

    def is_accepting(self, string):
        nfa = self.to_nfa()
        nfa.read_string(string)
        return nfa.is_accepting()

    def to_nfa(self):
        return NFA(set([self.start_state]), self.accept_state, self.rulebook)


if __name__ == "__main__":
    rulebook = NFARulebook(
        [
            FARule(1, None, 2), FARule(1, None, 4),
            FARule(2, 'a', 3),
            FARule(3, 'a', 2),
            FARule(4, 'a', 5),
            FARule(5, 'a', 6),
            FARule(6, 'a', 4),
        ]
    )

    print(rulebook.next_state(set([1]), None))
    print(rulebook.follow_free_moves(set([1])))
    print("-" * 20)
    nfa_design = NFADesign(1, [2, 4], rulebook)
    print(nfa_design.is_accepting('aa'))
    print(nfa_design.is_accepting('aaa'))
    print(nfa_design.is_accepting('aaaaa'))
    print(nfa_design.is_accepting('aaaaaa'))

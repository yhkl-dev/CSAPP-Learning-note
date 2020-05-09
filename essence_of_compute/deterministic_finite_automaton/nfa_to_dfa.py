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
        n_states = []
        for state in states:
            s = self.follow_rules_for(state, character)
            n_states += s
        return set(n_states)

    def follow_rules_for(self, state, character):
        return [rule.follow() for rule in self.rule_for(state, character)]

    def rule_for(self, state, character):
        return [rule for rule in self.rules if rule.applies_to(state, character)]

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

    def accept(self):
        return bool(self.current_state & set(self.accept_state)) 

    def read_string(self, string):
        for s in string:
            self.read_character(s)

    def read_character(self, character):
        self.current_state = self.rulebook.next_state(self.current_state,
                                                      character)
        self.current_state = self.rulebook.follow_free_moves(self.current_state) 


class NFADesign(object):

    def __init__(self, start_state, accept_state, rulebook):
        self.start_state = start_state
        self.accept_state = accept_state
        self.rulebook = rulebook

    def is_accepting(self, string):
        nfa = self.to_nfa()
        nfa.read_string(string)
        return nfa.accept()

    def to_nfa(self, current_state=None):
        if not current_state:
            current_state = {self.start_state}
        return NFA(current_state, self.accept_state, self.rulebook)


class NFASimulation(object):

    def __init__(self, nfa_design):
        self.nfa_design = nfa_design 

    def next_state(self, state, character):
        nfa = self.nfa_design.to_nfa(state)
        nfa.read_character(character)
        return nfa.current_state

if __name__ == "__main__":
    rulebook = NFARulebook(
        [
            FARule(1, 'a', 1), FARule(1, 'a', 2), FARule(1, None, 2),
            FARule(2, 'b', 3),
            FARule(3, 'b', 1), FARule(3, None, 2)
        ]
    )

    nfa_design = NFADesign(1, [3], rulebook)
    print(nfa_design)
    print(nfa_design.to_nfa().current_state)
    print(nfa_design.to_nfa({2}).current_state)
    print(nfa_design.to_nfa({3}).current_state)

    nfa = nfa_design.to_nfa({2, 3})
    nfa.read_character('b')
    print(nfa.current_state)



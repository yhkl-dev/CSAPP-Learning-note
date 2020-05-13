from stack import Stack


class PDAConfiguration(object):
    STUCK_STATE = type("", (), {})()

    def __init__(self, state, stack):
        self.state = state
        self.stack = stack

    def stuck(self):
        return PDAConfiguration(self.STUCK_STATE, self.stack)

    def is_stuck(self):
        return self.state == self.STUCK_STATE


class PDARule(object):

    def __init__(self, state, character, next_state, pop_character,
                 push_character):
        self.state = state
        self.character = character
        self.next_state = next_state
        self.pop_character = pop_character
        self.push_character = push_character

    def applies_to(self, configuration, character):
        return self.state == configuration.state and \
            self.pop_character == configuration.stack.top() and \
            self.character == character

    def follow(self, configuration):
        return PDAConfiguration(
            self.next_state,
            self.next_stack(configuration))

    def next_stack(self, configuration):

        poped_stack = configuration.stack.pop()
        self.push_character.reverse()
        for s in self.push_character:
            poped_stack = poped_stack.push(s)

        return poped_stack


class DPDARulebook(object):

    def __init__(self, rules):
        self.rules = rules

    def next_configuration(self, configuration, character):
        rule = self.rule_for(configuration, character)
        return rule.follow(configuration)

    def rule_for(self, configuration, character):
        for rule in self.rules:
            if rule.applies_to(configuration, character):
                return rule


class DPDA(object):

    def __init__(self, current_configuration, accept_states, rulebook):
        self.current_configuration = current_configuration
        self.accept_states = accept_states
        self.rulebook = rulebook

    def accepting(self):
        return self.current_configuration.state in self.accept_states

    def read_character(self, character):
        self.current_configuration = self.rulebook.next_configuration(
            self.current_configuration, character)

    def read_string(self, string):
        for s in string:
            print('s', s)
            self.read_character(s)


    
class DPDADesign(object):

    def __init__(self, start_state, bottom_character, accept_states, rulebook):
        self.start_state = start_state
        self.bottom_character = bottom_character
        self.accept_states = accept_states
        self.rulebook = rulebook

    def accepting(self, string):
        return self.to_dpda().read_string(string).accepting()

    def to_dpda(self):
        start_stack = Stack([bottom_character])
        start_configuration = PDAConfiguration(self.start_state, start_stack)
        return DPDA(start_configuration, self.accept_states, self.rulebook)


if __name__ == '__main__':
    rule = PDARule(1, '(', 2, '$', ['b', '$'])
    configuration = PDAConfiguration(1, Stack(['$']))
    print(rule.applies_to(configuration, '('))

    print('-' * 100)

    rulebook = DPDARulebook([
        PDARule(1, '(', 2, '$', ['b', '$']),
        PDARule(2, '(', 2, 'b', ['b', 'b']),
        PDARule(2, ')', 2, 'b', []),
        PDARule(2, None, 1, '$', ['$']),
    ])
    configuration = rulebook.next_configuration(configuration, '(')
    configuration = rulebook.next_configuration(configuration, '(')
    configuration = rulebook.next_configuration(configuration, ')')
    print(configuration)

    print('-' * 100)
    dpda = DPDA(PDAConfiguration(1, Stack(['$'])), [1], rulebook)
    print(dpda.accepting())
    # dpda.read_string("(()")
    print('y-' * 100)
    # print(dpda.accepting())

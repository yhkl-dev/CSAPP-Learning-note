from stack import Stack


class PDAConfiguration(object):

    def __init__(self, state, stack):
        self.state = state
        self.stack = stack


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
        print('2')
        return PDAConfiguration(self.next_state, self.next_stack(configuration))

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
        print('rule', rule.__dict__)
        print(type(rule))
        return rule.follow(configuration)

    def rule_for(self, configuration, character):
        for rule in self.rules:
            if rule.applies_to(configuration, character):
                print('1')
                print(rule)
                return rule 


class DPDA(object):

    def __init__(self, current_configuration, accept_states, rulebook):
        self.current_configuration = current_configuration
        self.accept_states = accept_states
        self.rulebook = rulebook

    def accepting(self):
        return self.current_configuration.state in self.accept_states

    def read_character(self, character):
        self.current_configuration = \
                self.rulebook.next_configuration(self.current_configuration, character)

    def read_string(self, string):
        for s in string:
            self.read_character(s)

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
    print(configuration)

    print('-' * 100)
    dpda = DPDA(PDAConfiguration(1, Stack(['$'])), [1], rulebook)
    print(dpda.accepting())
    dpda.read_string("(()")
    print(dpda.accepting())
    

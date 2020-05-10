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
        return PDAConfiguration(self.next_state, slef.next_stack(configuration))

    def next_stack(self, configuration):

        poped_stack = configuration.stack.pop()
        for s in self.push_character.reverse():
            starck = poped_stack.


    

if __name__ == '__main__':
    rule = PDARule(1, '(', 2, '$', ['b', '$'])
    configuration = PDAConfiguration(1, Stack(['$']))
    print(rule.applies_to(configuration, '('))


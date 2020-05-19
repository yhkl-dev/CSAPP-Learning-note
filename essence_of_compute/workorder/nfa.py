'''
    流程状态定义:
        未提交 - UNCOMMITTED,
        审核通过 - VERIFIED,
        审核驳回 - REJECTED,
        等待执行 - UNEXECUTED,
        执行中 - EXECUTING,
        执行完成 - EXECUTED,
        执行失败 - FALIED,
        用户确认 - CONFIRM
        关闭 - CLOSED,

'''

class FARule(object):

    def __init__(self, state, character, next_state):
        self.state = state
        self.character = character
        self.next_state = next_state

    def applies_to(self, state, character):
        return self.state == state and self.character == character

    def follow(self):
        return self.state

    def __str__(self):
        return "<# FARule: {} -- {} -- {}>".format(self.state, self.character,
                                                  self.next_state)
    

class DFARulebook(object):

    def __init__(self, rules):
        sefl.rules = rules

    def rules_for(self, state, character):
        for rule in self.rules:
            if rule.applies_to(state, character):
                return rule

    def next_state(self, state, character):
        rule = self.rules_for(state, character)
        return rule.follow()

    def __str__(self):
        return "<# DFARulebook: {}>" .format([rule.__str__() for rule in \
                                              self.rules])


class DFA(object):

    def __init__(self, current_state, accept_states, rulebook):
        self.current_state = current_state
        self.accept_states = accept_states
        self.rulebook = rulebook

    def accepting(self):
        return self.current_state in self.accept_states

    def read_character(self, character):
        self.current_state = self.rulebook.next_state(self.current_state,
                                                      character)
        
    def read_string(self, string):
        for character in string:
            self.read_character(character)


class DFADesign(object):

    def __init__(self, start_state, accept_states, rulebook):
        self.start_state = start_state
        self.accept_states = accept_states
        self.rulebook = rulebook

    def to_dfa(self):
        return DFA(self.start_state, self.accept_states, self.rulebook)
    
    def accepts(string):
        dfa = self.to_dfa()
        return dfa.accepting()



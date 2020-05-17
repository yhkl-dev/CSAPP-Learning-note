import unittest
from pda import *
from stack import Stack

class TestPDA(unittest.TestCase):

    def setUp(self):
        print('start test')
        self.rule = PDARule(1, '(', 2, '$', ['b', '$'])
        self.configuration = PDAConfiguration(1, Stack(['$']))       
        self.rulebook = DPDARulebook([
        	PDARule(1, '(', 2, '$', ['b', '$']),
	        PDARule(2, '(', 2, 'b', ['b', 'b']),
    	    PDARule(2, ')', 2, 'b', []),
        	PDARule(2, None, 1, '$', ['$']),
    	]) 


    def test_rule_applies_to(self):
        want = True
        got = self.rule.applies_to(self.configuration, '(')
        print("got: {}, want: {}".format(got, want))
        assert got == want

    def test_configuraion(self):
        configuration = PDAConfiguration(1, Stack(['$']))       
        configuration = self.rulebook.next_configuration(configuration, '(')
        print(configuration)
        configuration = self.rulebook.next_configuration(configuration, '(')
        print(configuration)
        configuration = self.rulebook.next_configuration(configuration, ')')
        print(configuration)

    def test_dpda(self):
        dpda = DPDA(PDAConfiguration(1, Stack(['$'])), [1], self.rulebook)
        print('dpda', dpda.accepting())
        dpda.read_string("(()")

        print('dpda--->', dpda.accepting())
        print('configuration', dpda.current_configuration)

if __name__ == '__main__':
    unittest.main()


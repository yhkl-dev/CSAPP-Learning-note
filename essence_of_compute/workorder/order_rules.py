from nfa import FARule, DFARulebook


order_state_list = [
    (1, 'UNCOMMITTED'),
    (2, 'DRAFT'),
    (3, 'VERIFYING'),
    (4, 'VERIFTED'),
    (5, 'VERIFY-REJECTED'),
    (6, 'EXECUTING'),
    (7, 'EXECUTED'),
    (8, 'EXE-FAILED'),
    (9, 'CLOSED'),
    (10, 'REJECT-CLOSED'),
    (11, 'REVOKE-CLOSED')
]

user_operation_list = [
    (1, 'COMMIT'),
    (2, 'VERIFY'),
    (3, 'REJECT'),
    (4, 'CONFIRM-EXECUTE'),
    (5, 'EXECUTE-DONE'),
    (6, 'EXECUTE-FAILED'),
    (7, 'REVOKE'),
    (8, 'CONFIRM'),
    (9, 'RE-EXECUTE')
]

RULEBOOK = DFARulebook(
    [
        FARule('UNCOMMITTED', 'COMMIT', 'VERIFYING'),
        FARule('VERIFYING', 'VERIFY', 'VERIFIED'),
        FARule('VERIFYING', 'REJECT', 'VERIFYING'),
        FARule('VERIFYING', 'REVOKE', 'REVOKE-CLOSED'),
        FARule('VERIFIED', 'CONFIRM-EXECUTE', 'EXECUTING'),
        FARule('EXECUTING', 'EXECUTE-DONE', 'EXECUTED'),
        FARule('EXECUTING', 'EXECUTE-FAILD', 'EXE-FAILED'),
        FARule('EXECUTED', 'CONFIRM', 'CLOSED'),
        FARule('EXE-FAILED', 'RE-EXECUTE', 'EXECUTING')
    ]
)


class Order(object):
    
    state = 'UNCOMMITED'

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.x = x

    def receive_condition(self, condition):
        print(condition)

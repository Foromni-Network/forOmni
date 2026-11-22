"""Independent verifier-owned acceptance tests; built-in unittest, synthetic only."""
import unittest
from converge import TaskRequest, propose
from slices.evidence import Receipt, accepted_receipts
from slices.policy import AgentGrant, eligible
from slices.ranking import choose, wilson_lower

SHA='a'*40
TASK=TaskRequest('T-EXP3','P-A','frontend',SHA,'SUITE-1',7)

def r(id,agent,verdict='ACCEPT',source=SHA,evaluator='qa-independent',worker=None):
    return Receipt(id,agent,'historical-'+id,source,evaluator,worker or agent,verdict,'SUITE-1')

def g(agent,**overrides):
    base=dict(agent_id=agent,project_id='P-A',task_id='T-EXP3',capability='frontend',action='draft_isolated',epoch=7)
    base.update(overrides)
    return AgentGrant(**base)

class TaskA(unittest.TestCase):
    def test_independent_source_bound_evidence(self):
        self.assertEqual(accepted_receipts((r('1','A'),r('2','A',source='b'*40),r('3','B',evaluator='B'),r('4','C',verdict='FAIL')),
                                          source_sha=SHA,suite_id='SUITE-1'), {'A':1})
    def test_receipt_replay_fail_closed(self):
        with self.assertRaisesRegex(ValueError,'duplicate'):
            accepted_receipts((r('1','A'),r('1','A')),source_sha=SHA,suite_id='SUITE-1')

class TaskB(unittest.TestCase):
    def test_project_task_revocation_and_epoch(self):
        self.assertTrue(eligible(g('A'),project_id='P-A',task_id='T-EXP3',capability='frontend',action='draft_isolated',epoch=7))
        for grant in (g('A',project_id='P-B'),g('A',task_id='elsewhere'),g('A',revoked=True),g('A',suspended=True),g('A',epoch=6),g('A',action='merge_protected')):
            self.assertFalse(eligible(grant,project_id='P-A',task_id='T-EXP3',capability='frontend',action='draft_isolated',epoch=7))

class TaskC(unittest.TestCase):
    def test_risk_conservative_selection(self):
        self.assertEqual(choose({'A':(2,2),'B':(35,40)}),'B')
        self.assertLess(wilson_lower(2,2),wilson_lower(35,40))
        self.assertIsNone(choose({'A':(0,0)}))

class Integration(unittest.TestCase):
    def test_three_slices_converge_one_selection(self):
        receipts=tuple([r('a'+str(i),'A') for i in range(2)] + [r('b'+str(i),'B') for i in range(35)])
        out=propose(TASK,receipts,(g('A'),g('B'),g('C',project_id='P-B')),{'A':2,'B':40,'C':50})
        self.assertEqual(out,{'task_id':'T-EXP3','suggested_agent':'B','eligible_agents':['A','B'],'authority':'NONE','integration_status':'RESEARCH_ONLY'})
    def test_stale_receipts_cannot_win(self):
        receipts=(r('a','A',source='b'*40),r('b','B'))
        self.assertEqual(propose(TASK,receipts,(g('A'),g('B')),{'A':1,'B':1})['suggested_agent'],'B')
    def test_only_revoked_or_wrong_project_yields_no_assignment(self):
        self.assertIsNone(propose(TASK,(r('a','A'),), (g('A',revoked=True),g('C',project_id='P-B')),{'A':1})['suggested_agent'])
    def test_forged_self_qa_gains_no_credit(self):
        out=propose(TASK,(r('f','A',evaluator='A'),r('b','B')), (g('A'),g('B')), {'A':1,'B':1})
        self.assertEqual(out['suggested_agent'],'B')
        self.assertEqual(out['authority'],'NONE')

class ControlComparison(unittest.TestCase):
    def test_naive_raw_rate_control_vs_evidence_gated(self):
        # Historical A=2/2 vs B=35/40: a naive sorter chooses A.
        naive = max({'A':(2,2),'B':(35,40)}, key=lambda a: {'A':1.0,'B':35/40}[a])
        self.assertEqual(naive,'A')
        receipts = tuple([r('a'+str(i),'A') for i in range(2)] + [r('b'+str(i),'B') for i in range(35)])
        self.assertEqual(propose(TASK, receipts, (g('A'),g('B')), {'A':2,'B':40})['suggested_agent'],'B')

    def test_no_side_effect_authority_in_output(self):
        result=propose(TASK,(r('1','A'),),(g('A'),),{'A':1})
        self.assertEqual(result['authority'],'NONE')
        self.assertNotIn('grant',result)
        self.assertNotIn('credential',result)

if __name__=='__main__': unittest.main()

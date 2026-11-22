"""EXPERIMENT 4: synthetic-only end-to-end tests, not an actual separated QA principal."""
import unittest
from dataclasses import replace
from provenance import Receipt,issue_receipt,verified_counts,verify_receipt
from gate import ProposalGrant,eligible
from selection import select,lower_bound
from converge import Request,propose

KEYS={'qa-external':b'only-a-test-not-a-real-secret'}
SHA='a'*40
REQ=Request('P-A','new-task','frontend',SHA,'suite-1',7)

def receipt(agent,num,verdict='ACCEPT',**kwargs):
    fields=dict(project_id='P-A',task_id=f'history-{num}',attempt_id=f'attempt-{num}',agent_id=agent,
                evaluator_id='qa-external',worker_id=agent,source_sha=SHA,suite_id='suite-1',
                verdict=verdict,complexity='mixed',cost_cents=10)
    fields.update(kwargs)
    return issue_receipt(Receipt(**fields),KEYS['qa-external'])

def grant(agent,**kwargs):
    fields=dict(agent_id=agent,project_id='P-A',task_id='new-task',capability='frontend',
                action='draft_isolated',epoch=7,valid_until_epoch=7,owner_consented=True)
    fields.update(kwargs)
    return ProposalGrant(**fields)

class Evidence(unittest.TestCase):
    def test_signature_authenticates_original_fields(self):
        r=receipt('A',1)
        self.assertEqual(verify_receipt(r,KEYS,project_id='P-A',source_sha=SHA,suite_id='suite-1'),(True,'valid'))
        self.assertEqual(verify_receipt(replace(r,agent_id='B'),KEYS,project_id='P-A',source_sha=SHA,suite_id='suite-1'),(False,'invalid_signature'))
    def test_wrong_project_and_stale_source_rejected(self):
        r=receipt('A',1)
        self.assertEqual(verify_receipt(r,KEYS,project_id='P-B',source_sha=SHA,suite_id='suite-1')[1],'wrong_project')
        self.assertEqual(verify_receipt(r,KEYS,project_id='P-A',source_sha='b'*40,suite_id='suite-1')[1],'stale_source_or_suite')
    def test_unknown_evaluator_and_self_review_rejected(self):
        self.assertEqual(verify_receipt(receipt('A',1,evaluator_id='fake'),KEYS,project_id='P-A',source_sha=SHA,suite_id='suite-1')[1],'unknown_evaluator')
        self.assertEqual(verify_receipt(receipt('A',1,evaluator_id='A'),{'A':KEYS['qa-external']},project_id='P-A',source_sha=SHA,suite_id='suite-1')[1],'self_review')
    def test_distinct_receipt_ids_cannot_replay_same_attempt(self):
        r=receipt('A',1)
        with self.assertRaisesRegex(ValueError,'duplicate_valid_attempt'):
            verified_counts((r,r),KEYS,project_id='P-A',source_sha=SHA,suite_id='suite-1')
    def test_rejected_verdict_counts_denominator_and_cost(self):
        c,rej,cost=verified_counts((receipt('A',1),receipt('A',2,'REJECT')),KEYS,project_id='P-A',source_sha=SHA,suite_id='suite-1')
        self.assertEqual(c['A'],(1,2));self.assertEqual(cost['A'],20);self.assertEqual(rej,{})

class Policy(unittest.TestCase):
    def test_project_owner_revoke_epoch(self):
        self.assertTrue(eligible(grant('A'),project_id='P-A',task_id='new-task',capability='frontend',current_epoch=7))
        for g in (grant('A',project_id='P-B'),grant('A',revoked=True),grant('A',suspended=True),grant('A',epoch=6),grant('A',owner_consented=False),grant('A',action='merge_protected'),grant('A',valid_until_epoch=6)):
            self.assertFalse(eligible(g,project_id='P-A',task_id='new-task',capability='frontend',current_epoch=7))

class Ranking(unittest.TestCase):
    def test_conservative_favors_35_of_40_over_2_of_2(self):
        self.assertLess(lower_bound(2,2),lower_bound(35,40));self.assertEqual(select({'A':(2,2),'B':(35,40)},{'A','B'}),'B')
    def test_no_evidence_abstains(self):
        self.assertIsNone(select({'A':(0,0)},{'A'}))

class EndToEnd(unittest.TestCase):
    def test_three_task_convergence(self):
        receipts=tuple(receipt('A',i) for i in range(2))+tuple(receipt('B',i+2) for i in range(35))+tuple(receipt('B',i+37,'REJECT') for i in range(5))
        out=propose(REQ,receipts,(grant('A'),grant('B'),grant('C',project_id='P-B')),KEYS)
        self.assertEqual(out['suggested_agent'],'B');self.assertEqual(out['verified_counts']['B'],(35,40))
        self.assertEqual(out['eligible_agents'],['A','B']);self.assertEqual(out['verified_cost_cents']['B'],400)
        self.assertEqual(out['authority'],'NONE');self.assertIsNone(out['effective_grant'])
    def test_signed_receipt_tamper_cannot_win(self):
        a=replace(receipt('A',1),agent_id='B')
        out=propose(REQ,(a,receipt('A',2)),(grant('A'),grant('B')),KEYS)
        self.assertEqual(out['suggested_agent'],'A');self.assertEqual(out['rejected_receipts'],{'invalid_signature':1})
    def test_revoked_candidates_abstain(self):
        out=propose(REQ,(receipt('A',1),),(grant('A',revoked=True),),KEYS)
        self.assertIsNone(out['suggested_agent'])
    def test_all_rejected_or_stale_abstain(self):
        out=propose(REQ,(receipt('A',1,source_sha='b'*40),),(grant('A'),),KEYS)
        self.assertIsNone(out['suggested_agent']);self.assertEqual(out['rejected_receipts'],{'stale_source_or_suite':1})

if __name__=='__main__':unittest.main()

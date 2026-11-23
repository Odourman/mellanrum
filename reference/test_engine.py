"""Pure logic tests. These are NOT emulator/hardware/raster tests."""
import unittest
from dataclasses import replace
from engine import Room,initial,step,index,passable,intrusion_phase,INTRUSION_WINDOWS
from rooms import ROOMS

class TestRules(unittest.TestCase):
    def setUp(self): self.r=ROOMS[0]
    def test_15_rooms_validate(self):
        self.assertEqual(len(ROOMS),15)
        for r in ROOMS:r.validate()
    def test_mirror_index(self):
        for y in range(8):
            for x in range(10):self.assertEqual(index(x,y),index(9-x,y))
    def test_edit_is_reflected(self):
        s=initial(self.r)
        k=index(1,3)
        self.assertTrue(s.bits>>k&1)
        t=step(self.r,s,('tree',k))
        self.assertFalse(t.bits>>k&1)
        self.assertTrue(passable(self.r,t,1,3))
        self.assertTrue(passable(self.r,t,8,3))
    def test_immutable_tree_rejects(self):
        s=initial(self.r);before=s.bits
        self.assertEqual(step(self.r,s,('tree',index(0,0))).bits,before)
    def test_stone_changes_orientation(self):
        r=self.r;s=initial(r)
        # owl about to enter revised I-01 stone from x3,y5 to x4,y5
        s=replace(s,x=3,y=5,direction=0)
        q=step(r,s)
        self.assertEqual((q.x,q.y,q.direction),(4,5,1))
        q=step(r,s,('stone',-1))
        self.assertEqual((q.x,q.y,q.direction),(4,5,3))
    def test_echo_commits_and_reverts(self):
        r=ROOMS[5];s=initial(r);k=index(2,3);start=bool(s.bits>>k&1)
        s=step(r,s,('tree',k));self.assertEqual(len(s.queue),1)
        self.assertNotEqual(bool(s.bits>>k&1),start)
        # due for action in tick 0 = tick 3, processed on step #4
        for _ in range(2):s=step(r,s)
        self.assertNotEqual(bool(s.bits>>k&1),start)
        s=step(r,s)
        self.assertEqual(bool(s.bits>>k&1),start)
    def test_polarity_5_delays_old_due(self):
        r=ROOMS[5];s=initial(r);s=step(r,s,('stone',-1))
        s=step(r,s,('tree',index(2,3)))
        self.assertEqual(s.queue[0][1],6) # scheduled at tick 1+5
        s=step(r,s,('stone',-1))
        self.assertEqual(s.queue[0][1],6)
    def test_queue_same_cell_locked(self):
        r=ROOMS[5];s=initial(r);k=index(2,3)
        s=step(r,s,('tree',k));bit=s.bits
        s=step(r,s,('tree',k))
        self.assertEqual(s.bits,bit)
        self.assertEqual(len(s.queue),1)
    def test_queue_full_rejects_third(self):
        r=ROOMS[9];s=initial(r)
        ks=[index(x,y) for y,row in enumerate(r.half) for x,c in enumerate(row) if c in 'Tt']
        self.assertGreaterEqual(len(ks),3)
        s=step(r,s,('tree',ks[0]));s=step(r,s,('tree',ks[1]));self.assertEqual(len(s.queue),2)
        before=s.bits;s=step(r,s,('tree',ks[2]))
        self.assertEqual(s.bits,before)
    def test_inversion_changes_passability(self):
        r=ROOMS[10];s=initial(r)
        self.assertFalse(passable(r,s,0,0))
        s=step(r,s);s=step(r,s);s=step(r,s);s=step(r,s)
        self.assertEqual(s.phase,1)
        self.assertTrue(passable(r,s,0,0))
        self.assertTrue(passable(r,s,*r.stone))
        self.assertTrue(passable(r,s,*r.exit))
    def test_no_death_on_occupied_cell(self):
        r=ROOMS[10];s=initial(r)
        for _ in range(30):
            s=step(r,s)
            self.assertTrue(0<=s.x<10 and 0<=s.y<8)
    def test_reproducible(self):
        r=ROOMS[13]
        a=b=initial(r)
        for i in range(45):
            action=[('wait',-1),('stone',-1),('tree',index(2,3))][i%3]
            a=step(r,a,action);b=step(r,b,action)
            self.assertEqual(a,b)
    def test_is_readonly_by_audio(self):
        # Sound is not part of engine and cannot affect game rules.
        s=initial(self.r)
        self.assertEqual(step(self.r,s),step(self.r,s))

class TestIntrusionV51(unittest.TestCase):
    def test_foreshadow_is_audiovisual_only(self):
        r=next(r for r in ROOMS if r.id=='II-05')
        self.assertEqual(intrusion_phase(r,4),'glimpse')
        self.assertEqual(intrusion_phase(r,5),'none')
    def test_warning_before_intercept(self):
        for name,(start,duration) in INTRUSION_WINDOWS.items():
            r=next(r for r in ROOMS if r.id==name)
            self.assertEqual(intrusion_phase(r,start-1),'warning')
            self.assertEqual(intrusion_phase(r,start),'active')
            self.assertEqual(intrusion_phase(r,start+duration),'none')
    def test_intercept_tree_becomes_stone_flip(self):
        r=next(r for r in ROOMS if r.id=='III-04')
        s=initial(r)
        k=index(3,3)
        s=step(r,s) # tick 0 = warning
        self.assertEqual(intrusion_phase(r,s.tick),'active')
        before=s
        after=step(r,s,('tree',k))
        self.assertEqual(after.bits,before.bits)
        self.assertEqual(after.polarity,1-before.polarity)
        self.assertEqual(len(after.queue),len(before.queue))
    def test_first_active_tick_always_reorients_stone(self):
        r=next(r for r in ROOMS if r.id=='III-04')
        s=step(r,initial(r)) # warning
        before=s.polarity
        s=step(r,s,('wait',-1))
        self.assertEqual(s.polarity,1-before)
    def test_wait_during_presence_does_not_repeat_automatic_flip(self):
        r=next(r for r in ROOMS if r.id=='III-05')
        s=initial(r)
        for i in range(3):s=step(r,s)
        self.assertEqual(intrusion_phase(r,s.tick),'active')
        before=s.polarity
        s=step(r,s,('wait',-1))
        self.assertEqual(s.polarity,1-before) # compulsory first-beat incursion
        before=s.polarity
        s=step(r,s,('wait',-1))
        self.assertEqual(s.polarity,before) # no second automatic incursion
    def test_stone_operation_not_intercepted(self):
        r=next(r for r in ROOMS if r.id=='III-04')
        s=step(r,initial(r))
        before=s.polarity
        s=step(r,s,('stone',-1))
        self.assertEqual(s.polarity,before) # player's flip plus forced incursion = 2 flips
    def test_act_one_two_unmodified(self):
        self.assertEqual(len([r for r in ROOMS if r.act!=3 and r.id in INTRUSION_WINDOWS]),0)

if __name__=='__main__': unittest.main(verbosity=2)

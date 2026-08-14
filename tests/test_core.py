import unittest
from rooom_lab.core import Cell, ReactiveNotebook
class LabTests(unittest.TestCase):
 def test_reactive_order(self):
  n=ReactiveNotebook(); n.add(Cell('b','y=x+1\ny')); n.add(Cell('a','x=2\nx'))
  out=n.run(); self.assertEqual(out['b'],3); self.assertEqual(n.order(),['a','b'])
if __name__=='__main__': unittest.main()

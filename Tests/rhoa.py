import unittest
from Rho.rhoa import rho_a

class Test:
    def __init__(self, period, value, error):
        self.T = period
        self.val = value
        self.err= error
        
class Station:
    def __init__(self):
        self.Z = {}
        
    def read(self, t, p, e, component):
        self.Z[component] = Test(t, p, e)
        
class TestRhoA(unittest.TestCase):
    
    global stn
    stn=Station()
    
    def test_rho_a(self):
        stn.read(1, 2, 3, "ZXX")
        self.assertEqual(rho_a(stn.Z["ZXX"]), (1, 506605.9182116889, 1519817.7546350667))
                         
if __name__ == '__main__':
    unittest.main()

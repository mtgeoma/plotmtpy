import unittest
from Rho.phi import phi

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
        
class TestPhi(unittest.TestCase):
    
    global stn
    stn=Station()
    
    def test_phi(self):
        stn.read(1, 2, 3, "ZXX")
        self.assertEqual(phi(stn.Z["ZXX"]), (1, 0.0, 57.295779513082323))
                         
if __name__ == '__main__':
    unittest.main()
import unittest
import receiver


class receiver_test(unittest.TestCase):

    def test_minimum_temperature_sample(self):
        self.assertTrue(receiver.get_minimum_temperature_sample([109.4,73.4,102.2,158.0,96.8])==73.4)
    
    def test_maximum_temperature_sample(self):
        self.assertTrue(receiver.get_maximum_temperature_sample([109.4,73.4,102.2,158.0,96.8])==158.0)
    
    def test_minimum_current_sample(self):
        self.assertTrue(receiver.get_minimum_current_sample([5,6,6,4,1])==1 )
    
    def test_maximum_current_sample(self):
        self.assertTrue(receiver.get_maximum_current_sample([8,9,5,1])== 9)
  
    
    
if __name__ == '__main__':
  unittest.main()
  


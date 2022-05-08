import unittest
import receiver
data = '''{"apms": 4, "temp": 100.4}
    {"apms": 6, "temp": 131.0}
    {"apms": 3, "temp": 138.2}
    {"apms": 9, "temp": 167.0}
    {"apms": 10, "temp": 167.0}
    {"apms": 0, "temp": 123.8}'''

class receiver_test(unittest.TestCase):

    def test_minimum_temperature_sample(self):
        self.assertTrue(receiver.get_minimum_temperature_sample([109.4,73.4,102.2,158.0,96.8])==73.4)
    
    def test_maximum_temperature_sample(self):
        self.assertTrue(receiver.get_maximum_temperature_sample([109.4,73.4,102.2,158.0,96.8])==158.0)
    
    def test_minimum_current_sample(self):
        self.assertTrue(receiver.get_minimum_current_sample([5,6,6,4,1])==1 )
    
    def test_maximum_current_sample(self):
        self.assertTrue(receiver.get_maximum_current_sample([8,9,5,1])== 9)
     
    def test_current_movingAveragevalue(self):
        self.assertTrue(receiver.current_movingAveragevalue([40,30,55,50,60],3)==[41.67, 45.0, 55.0])
        
    def test_temperature_movingAveragevalue(self):
        self.assertTrue(receiver.temperature_movingAveragevalue([100.4, 131.0, 138.2, 167.0, 167.0, 123.8],5)==[140.72, 145.4])
        
    def test_compute_statistics(self):
         self.assertTrue(receiver.compute_statistics([4, 6, 3, 9, 10, 0],[100.4, 131.0, 138.2, 167.0, 167.0, 123.8])==(0 ,10, 100.4, 167.0, [6.4, 5.6],[140.72, 145.4]))
        
    def test_process_data_from_sender(self):
        self.assertTrue(receiver.process_data_from_sender(data)==(Min_Amps:0  Max_Amps:10  Min_temp:100.4  Max_temp:167.0  Moving_Average_Amps:[6.4, 5.6]  Moving_Average_Amps:[140.72, 145.4]))   
       
        
    
    
  
    
    
if __name__ == '__main__':
  unittest.main()
  


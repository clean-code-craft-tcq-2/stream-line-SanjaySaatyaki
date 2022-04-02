

import unittest
import sender

class sender_test(unittest.TestCase):

    def test_get_12B_A2D_data(self):
        self.assertTrue(sender.get_12B_A2D_data() in range(0,4094))
    
    def test_get_temp_data_in_celcius(self):
        self.assertTrue(sender.get_temp_data_in_celcius() in range(20,80))
    
    def test_a2D_12BtoAmps_convertor(self):
        self.assertTrue(sender.a2D_12BtoAmps_convertor(2223) == 5)
    
    def test_celcius_to_Farenheit_convertor(self):
        self.assertTrue(sender.celcius_to_Farenheit_convertor(50) == 122.0)
    
    def test_pre_process(self):
        self.assertTrue(sender.pre_process(2223,50) == {"apms":5,"temp":122.0})
    
    def stream_data (self):
        self.assertTrue(sender.streamData(1) == "No of Streams Completed = 1")

if __name__ == '__main__':
  unittest.main()
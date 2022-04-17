import sender

def get_minimum_temperature_sample(temperature_list):
    return min(temperature_list)
    
def get_maximum_temperature_sample(temperature_list):
    return max(temperature_list)
    
def get_minimum_current_sample(current_sample_list):
    return min(current_sample_list)
    
def get_maximum_current_sample(current_sample_list):
    return max(current_sample_list)

def temperature_movingAveragevalue(temperature_list,Size):
  temp_movingAverage = []
  index = 0
  while index < len(temperature_list)-Size+1:
    window = temperature_list[index:index+Size]
    windowAverage = round((sum(window)/Size),2)
    temp_movingAverage.append(windowAverage)
    index = index+1
  return temp_movingAverage

def current_movingAveragevalue(current_sample_list,Size):
  current_movingAverage = []
  index = 0
  while index < len(current_sample_list)-Size+1:
    window = current_sample_list[index:index+Size]
    windowAverage = round((sum(window)/Size),2)
    current_movingAverage.append(windowAverage)
    index = index+1
  return current_movingAverage
  

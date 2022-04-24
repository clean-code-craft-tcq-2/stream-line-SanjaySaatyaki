import sender

def get_minimum_temperature_sample(temp_list):
    return min(temp_list)
    
def get_maximum_temperature_sample(temp_list):
    return max(temp_list)
    
def get_minimum_current_sample(amps_list):
    return min(amps_list)
    
def get_maximum_current_sample(amps_list):
    return max(amps_list)

def temperature_movingAveragevalue(temp_list,Size):
  temp_movingAverage = []
  index = 0
  while index < len(temp_list)-Size+1:
    window = temp_list[index:index+Size]
    windowAverage = round((sum(window)/Size),2)
    temp_movingAverage.append(windowAverage)
    index = index+1
  return temp_movingAverage

def current_movingAveragevalue(amps_list,Size):
  current_movingAverage = []
  index = 0
  while index < len(amps_list)-Size+1:
    window = amps_list[index:index+Size]
    windowAverage = round((sum(window)/Size),2)
    current_movingAverage.append(windowAverage)
    index = index+1
  return current_movingAverage

def compute_statistics(amps_list,temp_list):
    
    min_amps = get_minimum_current_sample(amps_list)
    max_amps = get_maximum_current_sample(amps_list)

    min_temp = get_minimum_temperature_sample(temp_list)
    max_temp = get_maximum_temperature_sample(temp_list)

    mov_avg_amps = current_movingAveragevalue(amps_list,5)
    mov_avg_temp = temperature_movingAveragevalue(temp_list,5)

    return min_amps, max_amps, min_temp, max_temp, mov_avg_amps, mov_avg_temp

def get_data_from_console():
    data = '''{"apms": 4, "temp": 100.4}
    {"apms": 6, "temp": 131.0}
    {"apms": 3, "temp": 138.2}
    {"apms": 9, "temp": 167.0}
    {"apms": 10, "temp": 167.0}
    {"apms": 0, "temp": 123.8}'''
    data_list = data.split("\n")
    amps_list = []
    temp_list = []
    for value in data_list:
        json_data = json.loads(value)
        amps_list.append(json_data['apms'])
        temp_list.append(json_data['temp'])
        if (len(amps_list)and len(temp_list)==6):
            print(amps_list,temp_list)
            min_amps, max_amps, min_temp, max_temp, mov_avg_amps, mov_avg_temp = compute_statistics(amps_list, temp_list)
            return('Min_Amps:{}\tMax_Amps:{}\tMin_temp:{}\tMax_temp:{}\tMoving_Average_Amps:{}\tMoving_Average,Temp:{}'.format(min_amps, max_amps, min_temp, max_temp, mov_avg_amps, mov_avg_temp))




if __name__ == "__main__":
    get_data_from_console()
    
  

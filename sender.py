import random

def get_12B_A2D_data():
    return random.randint(0, 4094)

def get_temp_data_in_celcius():
    return random.randint(20,80)

def a2D_12BtoAmps_convertor(sample):
    return round(sample*10/4094)

def celcius_to_Farenheit_convertor(temp_in_C):
    return round((temp_in_C * 1.8) + 32,2)

def pre_process(a2d_data,temp_in_C):
    data_dict = {}
    data_dict.update({"apms":a2D_12BtoAmps_convertor(a2d_data)})
    data_dict.update({"temp":celcius_to_Farenheit_convertor(temp_in_C)})
    return data_dict

def stream_data(number):
    for i in range(number):
        print(pre_process(get_12B_A2D_data(),get_temp_data_in_celcius()))
    return "No of Streams Completed = {}".format(number)

if __name__ == "__main__":
    stream_data(50)

from sensor.exception import SensorException
import os 
import sys

from sensor.logger import logging

def test_exception():
    try:
        logging.info("ki yaha p bhaiaa ek error ayegi diveision by zero wali error ") # info, not INFO
        a=1/0
    except Exception as e:
       # what will we raise here: our customized exception, i.e. the class SE
       raise SensorException(e,sys)
       # raise e 
    
      

'''
module execution oncontrol/ provent execution on import (control exception inside module). name == main: here we are 
setting main module (only main file will run)

in place of name, it will do main.py. So, it won't run things from Sensor exception file, but whatever we will write 
below it.

use 'name == main' here so that exception values do not run here directly. The values that we provide should run.
'''

if __name__ == "__main__":

    try:
        test_exception()
    except Exception as e:
        print(e)
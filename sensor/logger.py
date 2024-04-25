''' Create this so that we don't have to find till what point is my project working fine
In production, we don't open console & see what if the error -> there we can access logger (can deploy it in AWS) & thru
that we can see the errors.
In one line: we can see all PROJECT TRACKINF DETAILS thru this.
'''

import logging
import os
import sys

# to get date & time related things - at what time we ran, when did we get the error
from datetime import datetime


'''
1. Make a Folder (makedirs)
2. Give it a path (logs_path)
3. If already a log folder is created, let us not create another folder. (exist_ok=True)

1. File's extension is .log
2. folder's name will be in datetime format & time will be -> now: time right now. Since we don't want a numeric name to 
file, but a string name, we will convert it to string using "strftime".

os.path.join -> make a path (like provide more details in relative path). Folder's name is set to "logs". What will we
store in it? the "log file".
To know at which place error happened, we need current working directory.


'''

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)

os.makedirs(logs_path,exist_ok=True)

# LOG_FILE inside logs_path.
LOG_FILE_PATH= os.path.join(logs_path,LOG_FILE)


# To capture logging, we use the function basicConfig
#s-string (print in String form) d-digit (print in digit form), name is of logger
logging.basicConfig(
filename =LOG_FILE_PATH,
format = "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s", 
level= logging.INFO, # INFO, capital always (DEBUG is the lowerst logging level): DEBUG, INFO, WARNING, ERROR, CRITICAL
)






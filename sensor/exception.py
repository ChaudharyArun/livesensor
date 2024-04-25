''' 
View all errors at one place - which place is error occuring & in which file. We can customize how we see errors. So, we do 2 things:
1. Debugging & 2. Error Management
'''



# sys is the system library: useful if we want to access anything related to system. 
# Similarly, for OS - OS will tell in which line error is


import sys
import os 


# This function will be used to capture more details about error: 1. Line number, 2. file & 3. what is the error. 
# ecx_info function's will output 3 values. Third is "exc_tb", by using which we can capture all 3 points above.

def error_message_detail(error, error_detail:sys):
    
    _,_,exc_tb = error_detail.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename # exc_tb. means go insite exc_tb folder.

    error_message="error occured and the file name is [{0}] and the linenumber is [{1}] and error is [{2}]".format(
    filename,exc_tb.tb_lineno,str(error))
    
    return error_message


''' We always write projects dynamically, i.e. if we want to make changes in code, we must not have to update everything.   
Hence, we will use OOPS.
So, we are creating a class SensorException & are passing Exception as an argument in it. 
Exception is a super-class which contains everything related to exception handling. So, we inherited this.

In class, we will make a constructor through init method - we are writing self to tell that this is a constructor of this(
SensorException) class.
2 variables are initiaized: "error_message(handle excpetions)" & "error_detail(capture error's line & file)". We used 
":sys" we will use details from system library whenever we will capture error details.
ErrorMessage is given to us by exception handling - for that we have already inherited Exception class.

Now, in order to use any inbuilt class (like here we have inherited Exception class) in python, we need to use the super 
function. So, super will talk about Error, hence we are passing "error_message" in it. 

Note that any error we will get is not visible in string format. To represent any object in string form, we need to use the
str function. We want to relate __str__ with SensorException class - hence we will use self.
'''

class SensorException(Exception):
    
    def __init__(self,error_message,error_detail:sys):

        super().__init__(error_message)

        # if we are passing a function inside class, we need to store it in a variable:
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        return  self.error_message
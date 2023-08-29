import sys
import os
sys.path.append(os.getcwd())
from src.logger import logging

# logging.info('In the Exception file')

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = f'Error Occurred in python script name {[file_name]}, line number {[exc_tb.tb_lineno]}, error message [{str(error)}]'
    
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        self.error_message = error_message_detail(error_message,error_detail)

    def __str__(self):
        return self.error_message
    
if __name__ == "__main__":
    logging.info('logging is startes')

    try:
        a = 10/0
    except Exception as e:
        logging.info('Division by zero')
        raise CustomException(e,sys)
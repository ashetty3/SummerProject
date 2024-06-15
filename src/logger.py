import logging
import os 
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" # Decides the file format of the log file 
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE) #Get Working Directory+logsfolder+filename

os.makedirs(logs_path,exist_ok=True) #If path already exists then overwrite it 

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s", #this is format of the log file
    level=logging.INFO 


)

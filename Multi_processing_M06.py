# Ahmad Ghaznawi
#15.1 Use multiprocessing to create three separate processes.
#Make each one wait a random number of seconds between zero and one, print the current time, and then exit.

#importing required libraries
import multiprocessing
from datetime import datetime
import time
import random

#writing our fucntion to determine our time
def Display_the_time():
    current_time = datetime.now()
    print("Today's date and time is ", format(current_time))
    time.sleep(random.randint(0,1))


if __name__ == '__main__':
    process1 = multiprocessing.Process(target=Display_the_time())
    process2 = multiprocessing.Process(target=Display_the_time())
    process3 = multiprocessing.Process(target=Display_the_time())
    process1.start()
    process2.start()
    process3.start()
    process1.join()
    process2.join()
    process2.join()

    print('The task has been completed successfully')
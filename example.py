# /// Import the watchdog script ///
from python_watchdog import *

# /// Your code here ///

# /// Start a watchdog based on watchdog.ini ///
start_watchdog('watchdog.ini')


# /// If you want to run more then one watchdog you chan do this with more .ini files ///
# start_watchdog('watchdog2.ini')

# /// Your code here ///

# /// Example to change a value in the watchdog.ini by script ///
# In this example we will change the restart value in the ini file from script2 to 0 so script2 wont restart anymore after the error
# Keep in mind when you set the stop flag to 1 you should also set the start flag to 0 
# In the same way you can update any value

#watchdog_update('watchdog.ini', 'restart2', 0)

# /// Your code here ///

# /// Get sure the main process (your main script) will keep alive by run in loop
while True:
    a = 1+2 # // just for the loop to keep the main process alive...
    # /// Your code here ///
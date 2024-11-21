# /// Import the watchdog script ///
from python_watchdog import *

# /// Your code here ///

# /// Start a watchdog based on watchdog.ini ///
run_watchdog('watchdog.ini')

# /// If you want to run more then one watchdog you chan do this with more .ini files ///
# run_watchdog('watchdog2.ini')

# /// Your code here ///

# /// Example to change a value in the watchdog.ini by script ///
# /// In this example we will change the value from start2 to 0 so script2 dont get started anymore ///
# watchdog_update('watchdog.ini', 'start2', 0)
# /// In the same way you can update any value ///

# /// Your code here ///

# /// Get sure the main process (your main script) will keep alive by run in loop
while True:
    a = 1+2 # // just for the loop ...
    # /// Your code here ///
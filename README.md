# Python-Watchdog
A simple watchdog that keeps an eye on your scripts so start/stop/restart them automatically based on your configuration

## Futures
* Keep an eye on your scripts start/stop/restart them automatically if necessary
* Dont block your main script
* You can start more then one watchdog parallel
* Easy implementation and configuration
* Clean exit over the main process so nor more wild running uboat scripts

## Requirements
A linux system and following common python libraries are used: configparser, threading, subprocess, time, os

## Example
Just copy all the files in a folder and run example.py to play around.</br>
The example.py will start a watchdog based on watchdog.ini (Start test1.py ans test2.py)</br>
test2.py will run in an error after 20sec and trigger a restart.</br>

## Important
The main process (your main script where you start the watchdog) has to run all the time. (infinite loop)</br>
If the main process stops also all the scripts startet with the watchdog will get stoped !</br>
This is intentional behavior to keep the processes clean. It is better to cleanly restart the main process and so all watchdog processes (scripts) than to have unmanaged processes running.
</br></br>
Keep in mind when you set a stop flag to 1 you should set the start flag to 0

## Usage
Place the python_watchdog.py in the same directory as your main script.</br>
Create a .ini file for your scripts in the same directory (for example see watchdog.ini)</br></br>
Define the flags for you scripts in the ini file:</br>
Start = Script should be started</br>
Stop = Script should be stoped</br>
Restart = Script should be restarted if it stops or run in an error</br></br>

Import the watchdog in your script with:
  ```sh
  from python_watchdog import *
  ```
You can start a watchdog in your script with:</br>
  ```sh
  run_watchdog('your_ini_file.ini')
  ```
If you want to run more then one watchdog you can do this with multiple ini files
  ```sh
  run_watchdog('your_ini_file2.ini')
  ```
If you want to change a flag in a ini file by script (in this example the restart flag from script1 to zero):
  ```sh
  watchdog_update('yourfile.ini', 'restart1', 0)
  ```

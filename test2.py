# Scripts prints 'Hello testscript 2" every 10sec but after two times it runs into an error and need to be / could be restarted by the watchdog
import time

while True:
    print("Hello testscript 2")
    time.sleep(10)
    print("Hello testscript 2")
    time.sleep(10)
    get.value
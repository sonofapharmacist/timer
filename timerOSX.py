#!/usr/bin/python3

import time
import datetime
import os

title = "Get Up"
message = "Time is up.  Step away from the computer."
command = f'''
osascript -e 'display notification "{message}" with title "{title}"title
afplay '/System/Library/Sounds/Blow.aiff'
'''

def clear_console():
    os.system('clear')

def countdown(h, m, s):
    while True:
        total_seconds = h * 3600 + m * 60 + s
        while total_seconds > 0:
            timer = datetime.timedelta(seconds = total_seconds)
            print(timer, end="\r")
            time.sleep(1)
            total_seconds -= 1

        print("Get Up ")
        os.system(command)
        input("Press Enter to continue...")

        clear_console()

h = 0
m = 25
s = 0

countdown(int(h), int(m), int(s))
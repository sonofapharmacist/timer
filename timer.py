#!/usr/bin/env python3

import time
import datetime
import os
from win11toast import toast # type: ignore

h = 0
m = 25
s = 0

def clear_console():
    os.system('cls')

def countdown(h, m, s):
    while True:
        total_seconds = h * 3600 + m * 60 + s
        while total_seconds > 0:
            timer = datetime.timedelta(seconds= total_seconds)
            print(timer, end="\r")
            time.sleep(1)
            total_seconds -= 1
        print("Get Up ")
        toast('Get Up ', 
              'Take a break then click to continue...',
              scenario='incomingCall',
              button='Dismiss'
        )
        clear_console()

countdown(int(h), int(m), int(s)) 

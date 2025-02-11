#!/usr/bin/env python



from time import time, sleep
from math import floor

def find_time():
    initial_epoch = 1739274274

    # Feb 11 2025 11:44:34 = 07:00 game time

    current_time = floor(time())


    day_hour = (4*60)+48
    night_hour = (2*60)+24

    day = day_hour*12
    night = night_hour*12

    fullday= day+night
    
    difference = current_time - initial_epoch
    days = floor(difference / fullday)
    d_difference = difference - (days * fullday)
    if d_difference > day-day_hour:  ## because I started at 07 instead of 06 
        hours = 18
        add_hours = floor((d_difference - day + day_hour) / night_hour)
        night_time = None
        if add_hours >= 6:
            night_time = add_hours - 6
        else:
            night_time = hours + add_hours
        remainder = ((d_difference - day + day_hour) / night_hour) - add_hours
        minutes = floor(remainder * 60)
        print(f"it is night_time {night_time:02d}:{minutes:02d} and days since epoch {days}")
    elif d_difference < day:
        hours = 7
        day_time = None
        add_hours = floor(d_difference / day_hour)
        remainder = (d_difference / day_hour) - add_hours
        minutes = floor(remainder * 60)
        day_time = hours + add_hours
        print(f"it is day_time {day_time:02d}:{minutes:02d} and days since epoch {days}")

if __name__ == "__main__":
    while True:
        find_time()
        sleep(10)

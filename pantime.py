#!/usr/bin/env python



from time import time, sleep
from math import floor

def find_time():
    # these are for aevos-1 
    # avp_epoch = 1739273986 - out of date
    
    thronefast_epoch = 1739400236

 

    current_time = floor(time())

    initial_epoch = thronefast_epoch

    day_hour = (4*60)+48
    night_hour = (2*60)+24

    day = day_hour*12
    night = night_hour*12

    fullday= day+night
    
    night_time = None
    day_time = None
    difference = current_time - initial_epoch
    days = floor(difference / fullday)
    d_difference = difference - (days * fullday)
    if d_difference > day: 
        hours = 18
        oadd_hours = floor((d_difference - day ) / night_hour)
        add_hours = oadd_hours
        if add_hours >= 6:
            night_time = add_hours - 6
        else:
            night_time = hours + add_hours
        remainder = ((d_difference - day) / night_hour) - add_hours
        until_day = floor(((12 - oadd_hours - remainder)*night_hour)/60)
        minutes = floor(remainder * 60)
        print(f"it is night_time {night_time:02d}:{minutes:02d} about {floor(until_day)} minutes until day and {days} days since epoch", end="\r", flush=True)
    elif d_difference < day:
        hours = 6
        add_hours = floor(d_difference / day_hour)
        remainder = (d_difference / day_hour) - add_hours
        until_night = floor(((12 - add_hours - remainder)*day_hour)/60)
        minutes = floor(remainder * 60)
        day_time = hours + add_hours
        print(f"it is day_time {day_time:02d}:{minutes:02d} about {floor(until_night)} minutes until night and {days} days since epoch", end="\r", flush=True)

    if day_time:
        pass
    elif night_time:
        pass

if __name__ == "__main__":
    while True:
        find_time()
        sleep(10)

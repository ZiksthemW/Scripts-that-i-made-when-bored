from time import sleep
import os

year = 0
month = 0
day = 0
hour = 0
minute = 0
second = 0

while True:
    second += 1
    
    if second >= 60:
        second = 0
        minute += 1

    if minute >= 60:
        minute = 0
        hour += 1
    
    if hour >= 24:
        hour = 0
        day += 1
        
    if day >= 30:
        day = 0
        month += 1
    
    if month >= 12:
        month = 0
        year += 1
    
    os.system("cls")
    print(f"""
    ----
    T I M E R
    ----
    Year(s): {year}
    Month(s): {month}
    Day(s): {day}
    Hour(s): {hour}
    Minute(s): {minute}
    Second(s): {second}
    ----""")
    sleep(1)

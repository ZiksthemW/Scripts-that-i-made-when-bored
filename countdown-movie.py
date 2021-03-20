import random
from time import sleep
import os

year = random.randint(1, 50)
month = random.randint(1, 11)
day = random.randint(1, 29)
hour = random.randint(1, 23)
minute = random.randint(1, 59)
second = random.randint(2, 59)

while True:
    second -= 1
    sleep(1)
    
    if second <= 0:
        second = 60
        minute -= 1
    
    if minute <= 0:
        minute = 60
        hour -= 1
    
    if hour <= 0:
        hour = 24
        day -= 1
    
    if day <= 0:
        day = 1
        month -= 1
    
    if month <= 0:
        month = 12
        year -= 1
    
    if year <= 0:
        year = 0
    
    os.system("cls")
    print(f"""
    ----
    C O U N T - D O W N
    ----
    DEATH? THERE'S AN APP FOR THAT.
    ----
    Year(s): {year}
    Month(s): {month}
    Day(s): {day}
    Hour(s): {hour}
    Minute(s): {minute}
    Second(s): {second}
    ----""")
    
    if year == 0 and month == 0 and day == 0 and minute == 0 and second == 0:
        print("Ur ded")

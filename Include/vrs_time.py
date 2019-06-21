from datetime import timedelta as td 
from datetime import datetime as dt 

# Parses user input for amount of time into different units of time
def time_parse(stime_all):
    p = []
    start = 0
    last = stime_all.index(stime_all[-1])
    for i in range(0,last+1):
        if not stime_all[i].isdigit() and i==last:
                p.append(stime_all[start:])
        elif not stime_all[i].isdigit() and stime_all[i+1].isdigit():
                p.append(stime_all[start:i+1])
                start = i+1
    return p

# Converts user input into datetime units of time
def time_in_seconds(stime_part):
    s = 0
    while stime_part[s].isdigit():
        s+=1
    to_convert = int(stime_part[:s])
    if 'y' in stime_part:
        return td(weeks=to_convert*52)
    elif 'mon' in stime_part:
        return td(weeks=to_convert*4)
    elif 'w' in stime_part:
        return td(weeks=to_convert)
    elif 'd' in stime_part:
        return td(days=to_convert)
    elif 'h' in stime_part:
        return td(hours=to_convert)
    elif 'min' in stime_part:
        return td(minutes=to_convert)
    elif 's' in stime_part:
        return td(seconds=to_convert)
    
# Determines when to give reminder
def calc_remind_time(stime):
    parts = time_parse(stime)
    s = td(seconds=0)
    for p in parts:
        s += time_in_seconds(p)
    return dt.now() + s

# Prints time as Month Day Year HH:MM:SS AM/PM
def pretty_time(time):
    print(time.strftime("%b %d %Y %I:%M:%S %p"))

def remind(stime_all):
    pretty_time(calc_remind_time(stime_all))

    
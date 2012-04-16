
import re

pattern = re.compile(r'\s*("[^"]*"|.*?)\s*,')

def split(line):
    return [x[1:-1] if x[:1] == x[-1:] == '"' else x
            for x in pattern.findall(line.rstrip(',') + ',')]

def decode_month(month):
    if month==1:
        return 'Jan'
    elif month==2:
        return 'Feb'
    elif month==3:
        return 'Mar'
    elif month==4:
        return 'Apr'
    
    elif month==5:
        return 'May'
    elif month==6:
        return 'Jun'
    elif month==7:
        return 'Jul'
    elif month==8:
        return 'Aug'
    elif month==9:
        return 'Sep'
    elif month==10:
        return 'Oct'
    elif month==11:
        return 'Nov'
    elif month==12:
        return 'Dec'
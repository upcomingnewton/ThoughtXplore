
import re

pattern = re.compile(r'\s*("[^"]*"|.*?)\s*,')

def split(line):
    return [x[1:-1] if x[:1] == x[-1:] == '"' else x
            for x in pattern.findall(line.rstrip(',') + ',')]

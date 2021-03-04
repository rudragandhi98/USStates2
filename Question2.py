import re

# 2.Output a file with list of US states with double letter sequence (e.g. Hawaii)
regex = re.compile(r"(.)\1")
data = open('usa.states.txt')

for line in data:
    match = re.search(regex, line)
    if match:
        print(line, "" + ": <- match for double", match.group(1))
    else:
        line.strip()
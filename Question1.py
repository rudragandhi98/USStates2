
# 1 Output a file with list of US states in order:
# a. Alphabetical
# b. Number of letters in name
with open('usa.states.txt', 'r') as usa:
    for line in sorted(usa):
        print(line, end = '')
        print(len(line)-1)


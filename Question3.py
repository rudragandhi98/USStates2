# 3.Output a file with list of US states, in alphabetical order, with Capitol name of less than 10 characters long

a_dictionary = {}
a_file = open("capitals.txt")
for line in a_file:
    key, value = line.split(',')
    a_dictionary[key] = value
    if(len(value)<12):
        print(key)



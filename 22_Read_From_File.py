with open('Exercise_22.txt', 'r') as open_file:
    line = open_file.readline()
    while line:
        print(line)
        line = open_file.readline()
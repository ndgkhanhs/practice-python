"""
with open('txt_file/Exercise_22.txt', 'r') as open_file:
    line = open_file.readline()
    while line:
        print(line)
        line = open_file.readline()
"""
counter_dict = {}

with open('txt_file/Challenge_22.txt', 'r', encoding='utf-8') as f:
    for line in f: 
        line = line.strip() 
        if len(line) > 29: 
            line = line[3:-26]
        if line:
            counter_dict[line] = counter_dict.get(line, 0) + 1 

for key, value in counter_dict.items():
    print(f"{key}: {value}")
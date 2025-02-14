#with open('Exercise_22.txt', 'r') as open_file:
#    line = open_file.readline()
#    while line:
#       print(line)
#        line = open_file.readline()

student_scores = {'Adama': 100, 'Starbuck': 75, 'Apollo': 80, 'Athena': 85, 'Agathon': 90}
adama_score = student_scores['Adama']
adama_score += 100
print (adama_score)

all_scores = student_scores.keys()
print(all_scores)
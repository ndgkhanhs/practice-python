with open('txt_file/23_One.txt', 'r', encoding='utf-8') as x:
    with open('txt_file/23_Two.txt', 'r', encoding = 'utf-8') as y:

        x_lines = set(line.strip() for line in x)
        y_lines = set(line.strip() for line in y)

        z = x_lines & y_lines

z = [int(num) for num in z]
z.sort()
print(z)

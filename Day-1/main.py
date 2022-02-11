with open("data.txt") as file_in:
    lines = []
    for line in file_in:
        lines.append(int(line.strip('\n')))

result = 0
for i in range(1, len(lines)):
    if lines[i] > lines[i - 1]:
        result += 1

print(result)
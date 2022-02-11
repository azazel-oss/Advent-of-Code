with open("data.txt") as file_in:
    lines = []
    for line in file_in:
        lines.append(int(line.strip('\n')))

result = 0
for i in range(1, len(lines)):
    if lines[i] > lines[i - 1]:
        result += 1

print(result)
result = 0

window_sum = lines[0] + lines[1] + lines[2]
for i in range(3, len(lines)):
    if lines[i] + lines[i - 1] + lines[i - 2] > window_sum:
        result += 1
    window_sum += lines[i]
    window_sum -= lines[i - 3]

print(result)
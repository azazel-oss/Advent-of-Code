depth = 0
distance = 0
aim = 0
with open('data.txt', 'r') as file:
    for line in file.readlines():
        direction, amplitude = line.split()
        if direction == 'forward':
            distance += int(amplitude)
            depth += aim * int(amplitude)
        elif direction == 'down':
            aim += int(amplitude)
        elif direction == 'up':
            aim -= int(amplitude)

print(distance * depth)



depth = 0
distance = 0
with open('data.txt', 'r') as file:
    for line in file.readlines():
        direction, amplitude = line.split()
        if direction == 'forward':
            distance += int(amplitude)
        elif direction == 'down':
            depth += int(amplitude)
        elif direction == 'up':
            depth -= int(amplitude)

print(distance * depth)

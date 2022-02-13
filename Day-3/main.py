current_one_count_oxygen = 0
current_one_count_carbon = 0
current_zero_count_oxygen = 0
current_zero_count_carbon = 0
oxygen = ''
carbon = ''

for i in range(12):
    with open('data.txt', 'r') as file:
        for data in file.readlines():
            if data.strip().startswith(oxygen):
                if data.strip()[len(oxygen):][0] == '1':
                    current_one_count_oxygen += 1
                else:
                    current_zero_count_oxygen += 1

            if data.strip().startswith(carbon):
                if data.strip()[len(carbon):][0] == '1':
                    current_one_count_carbon += 1
                else:
                    current_zero_count_carbon += 1

    oxygen += '0' if current_zero_count_oxygen > current_one_count_oxygen else '1'
    if current_zero_count_carbon == 0:
        carbon += '1'
    elif current_one_count_carbon == 0:
        carbon += '0'
    else:
        carbon += '1' if current_zero_count_carbon > current_one_count_carbon else '0'

    current_zero_count_oxygen = current_one_count_oxygen = current_zero_count_carbon = current_one_count_carbon = 0

print(oxygen, carbon)
print(int(oxygen, 2) * int(carbon, 2))

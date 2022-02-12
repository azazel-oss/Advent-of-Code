class Data:
    def __init__(self):
        self.one_count = 0
        self.zero_count = 0


data_list = []

for i in range(12):
    data_list.append(Data())

with open('data.txt', 'r') as file:
    for data in file.readlines():
        for index, bit in enumerate(data.strip()):
            if bit == '1':
                data_list[index].one_count += 1
            else:
                data_list[index].zero_count += 1

gamma_bits = []
epsilon_bits = []
for i in range(len(data_list)):
    gamma_digit = '1' if data_list[i].one_count > data_list[i].zero_count else '0'
    epsilon_digit = '1' if data_list[i].one_count < data_list[i].zero_count else '0'
    gamma_bits.append(gamma_digit)
    epsilon_bits.append(epsilon_digit)

gamma = ''.join(gamma_bits)
gamma = int(gamma, 2)
epsilon = ''.join(epsilon_bits)
epsilon = int(epsilon, 2)

print(gamma * epsilon)

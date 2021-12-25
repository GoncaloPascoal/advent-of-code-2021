
# Complexity: O(n * m); m is the number of bits in each number
def calc_power_consumption(numbers):
    n_bits = len(numbers[0])
    gamma_bits = [0] * n_bits

    for i in range(n_bits):
        gamma_bits[i] = len([b for b in numbers if b[i] == '1'])
    
    n = len(numbers)
    gamma_bits = map(lambda x: str(round(x / n)), gamma_bits)
    
    gamma = int(''.join(gamma_bits), 2)
    epsilon = int('1' * len(numbers[0]), 2) ^ gamma

    return gamma * epsilon

# Complexity: O(n * m); m is the number of bits in each number
def calc_life_support_rating(numbers):
    n_bits = len(numbers[0])
    bits = [0] * n_bits

    numbers_oxygen = numbers.copy()

    # Calculate oxygen rating
    for i in range(n_bits):
        if len(numbers_oxygen) == 1:
            oxygen = int(numbers_oxygen[0], 2)
            break

        bits[i] = len([b for b in numbers_oxygen if b[i] == '1'])
        n = len(numbers_oxygen)

        most_common = str(round(bits[i] / n))
        if bits[i] == n / 2:
            most_common = '1'

        numbers_oxygen = [b for b in numbers_oxygen if b[i] == most_common]

    # Calculate CO2 rating
    for i in range(n_bits):
        if len(numbers) == 1:
            co2 = int(numbers[0], 2)
            break

        bits[i] = len([b for b in numbers if b[i] == '1'])
        n = len(numbers)

        least_common = str(1 - round(bits[i] / n))
        if bits[i] == n / 2:
            least_common = '0'

        numbers = [b for b in numbers if b[i] == least_common]

    return oxygen * co2

f = open('../data/day03.txt', 'r')
numbers = f.read().split()
f.close()
print(calc_power_consumption(numbers))
print(calc_life_support_rating(numbers))

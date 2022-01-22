
def parse_file():
    f = open('../data/day06.txt', 'r')
    fish = list(map(int, f.read().strip().split(',')))
    f.close()

    count = [0] * 9
    for i in range(9):
        count[i] = fish.count(i)

    return count

# Complexity: O(n), where n is number of days, assuming clock remains constant
def calc_num_fish(count, days=80):
    for _ in range(days):
        new_count = [0] * 9

        for i in range(1, 9):
            new_count[i - 1] = count[i]
        new_count[6] += count[0]
        new_count[8] += count[0]

        count = new_count

    return sum(count)

count = parse_file()
print(calc_num_fish(count))
print(calc_num_fish(count, days=256))


def parse_file():
    with open('../data/day07.txt', 'r') as f:
        crabs = list(map(int, f.read().split(',')))
    return crabs

# Complexity: O(n^2) - Entirely brute force, there is probably a better way
def calc_min_fuel(crabs, constant_rate=True):
    min_fuel = None
    min_pos, max_pos = min(crabs), max(crabs)

    for pos in range(min_pos, max_pos + 1):
        fuel = 0
        for crab in crabs:
            inc = abs(pos - crab)
            if not constant_rate:
                # 1 + 2 + 3 + ... + n = n * (n + 1) / 2
                inc = inc * (inc + 1) // 2
            fuel += inc
        
        if min_fuel is None or fuel < min_fuel:
            min_fuel = fuel
    
    return min_fuel

crabs = parse_file()
print(calc_min_fuel(crabs))
print(calc_min_fuel(crabs, False))

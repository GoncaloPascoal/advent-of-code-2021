
# Complexity: O(n)
def count_increases(depths):
    increases = 0

    for i, j in zip(depths, depths[1:]):
        if j > i:
            increases += 1
    
    return increases

# Complexity: O(n)
def count_increases_sliding_window(depths):
    increases = 0

    previous_window = sum(depths[:2])
    for i in range(1, len(depths) - 2):
        next_window = previous_window - depths[i - 1] + depths[i + 2]
        if next_window > previous_window:
            increases += 1
        previous_window = next_window
    
    return increases


f = open('../data/day01.txt', 'r')
depths = list(map(int, f.readlines()))

print(count_increases(depths))
print(count_increases_sliding_window(depths))

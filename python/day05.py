
def parse_file():
    f = open('../data/day05.txt', 'r')
    lines = f.read().strip().split('\n')
    f.close()

    mx, my = 0, 0
    parse_point = lambda c: map(int, c.split(','))

    def update_max(point):
        nonlocal mx, my
        x, y = point
        mx = max(mx, x)
        my = max(my, y)

    for i, line in enumerate(lines):
        components = line.split()

        start = tuple(parse_point(components[0]))
        end = tuple(parse_point(components[2]))

        update_max(start)
        update_max(end)

        lines[i] = start, end

    return lines, mx, my

# Complexity: O(n^2)
def calc_num_overlapping(lines, mx, my, diagonals):
    grid = [[0 for _ in range(my + 1)] for _ in range(mx + 1)]

    sign = lambda x: -1 if x < 0 else 1

    for start, end in lines:
        x1, y1 = start
        x2, y2 = end
        
        if x1 == x2:
            # Vertical line
            s = sign(y2 - y1)
            for i in range(y1, y2 + s, s):
                grid[i][x1] += 1
        elif y1 == y2:
            # Horizontal line
            s = sign(x2 - x1)
            for i in range(x1, x2 + s, s):
                grid[y1][i] += 1
        elif diagonals:
            sx = sign(x2 - x1)
            sy = sign(y2 - y1)
            magnitude = abs(x2 - x1) + 1

            for i in range(magnitude):
                grid[y1 + i * sy][x1 + i * sx] += 1
    
    num_overlapping = 0
    for row in grid:
        for val in row:
            if val > 1:
                num_overlapping += 1
    
    return num_overlapping

lines, mx, my = parse_file()
print(calc_num_overlapping(lines, mx, my, False))
print(calc_num_overlapping(lines, mx, my, True))

def calc_position(commands):
    horizontal = 0
    depth = 0

    for command in commands:
        op = command[0]
        dist = int(command[1])

        if op == 'forward':
            horizontal += dist
        elif op == 'down':
            depth += dist
        else:
            depth -= dist
    
    return horizontal * depth

def calc_position_with_aim(commands):
    horizontal = 0
    depth = 0
    aim = 0

    for command in commands:
        op = command[0]
        dist = int(command[1])

        if op == 'forward':
            horizontal += dist
            depth += aim * dist
        elif op == 'down':
            aim += dist
        else:
            aim -= dist

    return horizontal * depth


f = open('../data/day02.txt', 'r')
commands = list(map(lambda x: x.split(), f.readlines()))
f.close()

print(calc_position(commands))
print(calc_position_with_aim(commands))

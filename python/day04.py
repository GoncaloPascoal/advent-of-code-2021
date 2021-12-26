
from typing import List
from copy import deepcopy

class Board:
    def __init__(self, matrix):
        self.size = len(matrix)
        self.rows = dict.fromkeys(range(self.size), 0)
        self.columns = dict.fromkeys(range(self.size), 0)

        self.map = {}
        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                self.map[val] = (i, j)

        self.unmarked = set(self.map.keys())

def parse_file():
    f = open('../data/day04.txt', 'r')
    contents = f.read()
    f.close()

    contents = contents.split('\n\n')
    seq, boards = list(map(int, contents[0].split(','))), contents[1:]

    # Process boards
    boards = map(lambda x: x.split('\n'), boards)
    boards = [
        Board(list(map(lambda x: list(map(int, x.split())), board)))
        for board in boards
    ]

    return seq, boards

# Complexity: O(n * m); n is sequence length, m is number of bingo boards
def calc_first_score(seq: List[int], boards: List[Board]) -> int:
    for num in seq:
        for board in boards:
            if num in board.map:
                board.unmarked.remove(num)

                row, col = board.map[num]
                board.rows[row] += 1
                board.columns[col] += 1

                if board.rows[row] == board.size or board.columns[col] == board.size:
                    # Board won
                    return sum(board.unmarked) * num

# Complexity: O(n * m)
def calc_last_score(seq: List[int], boards: List[Board]) -> int:
    winners = set()
    last_winner_score = 0

    for num in seq:
        for board in boards:
            if board not in winners and num in board.map:
                board.unmarked.remove(num)

                row, col = board.map[num]
                board.rows[row] += 1
                board.columns[col] += 1

                if board.rows[row] == board.size or board.columns[col] == board.size:
                    # Board won
                    winners.add(board)
                    last_winner_score = sum(board.unmarked) * num

    return last_winner_score

seq, boards = parse_file()
print(calc_first_score(seq, deepcopy(boards)))
print(calc_last_score(seq, boards))

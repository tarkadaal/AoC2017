#!/usr/bin/python
from itertools import combinations
def solve(data):
    def calc_diff(x):
        return max(x) - min(x)
    return sum(map(calc_diff, data))


def solve2(data):
    def calc_diff(x):
        y = combinations(sorted(x), 2)
        for t in y:
            if t[1] % t[0] == 0:
                return t[1] / t[0]
    return sum(map(calc_diff, data))

def read_puzzle_input():
    puzzle_input = []
    for line in open('input.txt', 'r'):
        strings = line.strip().split()
        ints = map(int, strings)
        puzzle_input.append(ints)
    return puzzle_input

if __name__ == '__main__':
    sample_input = ((5, 1, 9, 5),
                    (7, 5, 3),
                    (2, 4, 6, 8))
    result = solve(sample_input)
    print(result)

    puzzle_input = read_puzzle_input()
    result = solve(puzzle_input)
    print(result)

    sample_input = ((5, 9, 2, 8),
                    (9, 4, 7, 3),
                    (3, 8, 6, 5))
    result = solve2(sample_input)
    print(result)

    puzzle_input = read_puzzle_input()
    result = solve2(puzzle_input)
    print(result)

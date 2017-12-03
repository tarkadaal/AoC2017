#!/usr/bin/python

def solve(data):
    def calc_diff(x):
        return max(x) - min(x)
    return sum(map(calc_diff, data))

if __name__ == '__main__':
    sample_input = ((5, 1, 9, 5),
                    (7, 5, 3),
                    (2, 4, 6, 8))
    result = solve(sample_input)
    print(result)
    puzzle_input = []
    for line in open('input.txt', 'r'):
        strings = line.strip().split()
        ints = map(int, strings)
        puzzle_input.append(ints)
    result = solve(puzzle_input)
    print(result)

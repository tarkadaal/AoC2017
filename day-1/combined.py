#!/usr/bin/python
import sys
from collections import deque


def solve(data, index_func):
    ints = [int(x) for x in data.strip()]
    d = deque(ints)
    s = 0
    for i in range(len(d)):
        x = d[0]
        y = d[index_func(d)]
        s += x if x==y else 0
        d.rotate(-1)
    return s

def check_arguments(args):
    return len(args) == 2 and args[1] in ('1', '2')

if __name__ == '__main__':
    if not check_arguments(sys.argv):
        print('Invalid argments. Script takes one "part" argument, 1 or 2.')
        quit()

    with open('puzzle-1-1.txt', 'r') as f:
        input_data = f.read()

    funcs = {
        "1": lambda x: 1,
        "2": lambda x: len(x) / 2
    }
    func = funcs[sys.argv[1]]
    result = solve(input_data, func)
    print(result)

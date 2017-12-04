#!/usr/bin/python
UPLEFT      = (-1,-1)
UP          = (0, -1)
UPRIGHT     = (1, -1)
RIGHT       = (1, 0)
DOWNRIGHT   = (1, 1)
DOWN        = (0, 1)
DOWNLEFT    = (-1, 1)
LEFT        = (-1, 0)

ALL_DIRECTIONS = (UPLEFT, UP, UPRIGHT, RIGHT, DOWNRIGHT, DOWN, DOWNLEFT, LEFT)

WIDDERSHINS = {
    UP: LEFT,
    RIGHT: UP,
    DOWN: RIGHT,
    LEFT: DOWN
}

START = (500, 500)


def manhattan_distance(start, end):
    return abs(end[0] - start[0]) + abs(end[1] - start[1])

def sum_neighbours(val, pos, board):
    return sum(map(lambda x: board[pos[0] + x[0]][pos[1] + x[1]], ALL_DIRECTIONS)) + board[pos[0]][pos[1]]

def val(val, pos, board):
    return val


def get_cell_to_left(pos, dir, board):
    left = WIDDERSHINS[dir]
    newpos = pos[0] + left[0], pos[1] + left[1]
    return board[newpos[0]][newpos[1]]

def _solve(target, pos, dir, board, func):
    for x in xrange(1, target + 1):
        if target == x:
            return manhattan_distance(START, pos)
        board[pos[0]][pos[1]] = func(x, pos, board)
        if get_cell_to_left(pos, dir, board) == 0:
            dir = WIDDERSHINS[dir]
        pos = pos[0] + dir[0], pos[1] + dir[1]


def _solve2(target, pos, dir, board, func):
    for x in xrange(1, 10000000 + 1):
        this_cell = func(x, pos, board)
        if target < this_cell:
            return this_cell
        board[pos[0]][pos[1]] = this_cell
        if get_cell_to_left(pos, dir, board) == 0:
            dir = WIDDERSHINS[dir]
        pos = pos[0] + dir[0], pos[1] + dir[1]


def solve(n):
    return _solve(n, START, DOWN, [[0] * 1000 for i in range(1000)], val)

def solve2(n):
    board = [[0] * 1000 for i in range(1000)]
    board[START[0]][START[1]] = 1
    return _solve2(n, START, DOWN, board, sum_neighbours)

def test_solve(n):
    """
    >>> solve(1)
    0
    >>> solve(12)
    3
    >>> solve(23)
    2
    >>> solve(1024)
    31
    """
    pass

def test_solve2(n):
    """
    >>> solve2(1)
    2
    >>> solve2(2)
    4
    """
    pass

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(solve(312051))
    print(solve2(312051))
    

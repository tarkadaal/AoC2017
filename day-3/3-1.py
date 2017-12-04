#!/usr/bin/python

UP      = (0, -1)
RIGHT   = (1, 0)
DOWN    = (0, 1)
LEFT    = (-1, 0)
LEFT_DIRECTION = {
    UP: LEFT,
    RIGHT: UP,
    DOWN: RIGHT,
    LEFT: DOWN
}

START = (500, 500)

def get_cell_to_left(pos, dir, board):
    left = LEFT_DIRECTION[dir]
    newpos = pos[0] + left[0], pos[1] + left[1]
    return board[newpos[0]][newpos[1]]

def manhattan_distance(start, end):
    return abs(end[0] - start[0]) + abs(end[1] - start[1])

def _solve(target, current, pos, dir, board):
    for x in xrange(1, target + 1):
        if target == x:
            return manhattan_distance(START, pos)
        board[pos[0]][pos[1]] = x
        if get_cell_to_left(pos, dir, board) == 0:
            dir = LEFT_DIRECTION[dir]
        pos = pos[0] + dir[0], pos[1] + dir[1]


def solve(n):
    return _solve(n, 1, START, DOWN, [[0] * 1000 for i in range(1000)])

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

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(solve(312051))

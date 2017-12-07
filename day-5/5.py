#!/usr/bin/python

def maze_escape(maze):
    step_total = 0
    current_index = 0
    while -1 < current_index < len(maze):
        step_total += 1
        instruction = maze[current_index]
        maze[current_index] += 1
        current_index += instruction
    return step_total

def maze_escape_2(maze):
    step_total = 0
    current_index = 0
    while -1 < current_index < len(maze):
        step_total += 1
        instruction = maze[current_index]
        maze[current_index] += 1 if instruction < 3 else -1
        current_index += instruction
    return step_total

def test_maze_escape():
    """
    >>> maze_escape([0, 3, 0, 1, -3])
    5
    """
    pass

def test_maze_escape_2():
    """
    >>> maze_escape_2([0, 3, 0, 1, -3])
    10
    """
    pass

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    with open('input.txt', 'r') as f:
        input_data = f.readlines()

    print(maze_escape([int(x.strip()) for x in input_data])) # answer: 342669
    print(maze_escape_2([int(x.strip()) for x in input_data])) # answer: 25136209
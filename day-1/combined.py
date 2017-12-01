#!/usr/bin/python
import sys
from collections import deque

def solve(index_func):
  for line in open('puzzle-1-1.txt', 'r'):
    ints = [int(x) for x in line.strip()]
    d = deque(ints)
    l = len(d)
    s = 0
    for i in range(l):
      x = d[0]
      y = d[index_func(d)]
      if x == y:
        s += x
      d.rotate(-1)
    print(str(s))

if __name__ == '__main__':
  if len(sys.argv) == 2:
    part = int(sys.argv[1])
    if part == 1:
      solve(lambda x: 1)
    elif part == 2:
      solve(lambda x: len(x)/2)
  else:
    print("Invalid number of arguments")
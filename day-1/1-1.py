#!/usr/bin/python
from collections import deque

for line in open('puzzle-1-1.txt', 'r'):
  ints = [int(x) for x in line.strip()]
  d = deque(ints)
  l = len(d)
  s = 0
  for i in range(l):
    x = d[0]
    d.rotate(-1)
    y = d[0]
    if x == y:
      s += x
  print(str(s))


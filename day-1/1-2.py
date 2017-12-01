#!/usr/bin/python
from collections import deque

for line in open('puzzle-1-1.txt', 'r'):
  ints = [int(x) for x in line.strip()]
  d = deque(ints)
  l = len(d)
  s = 0
  for i in range(l):
    x = d[0]
    y = d[l/2]
    if x == y:
      s += x
    d.rotate(-1)
  print(str(s))


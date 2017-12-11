#!/usr/bin/python

def _redistribute(banks):
    index = banks.index(max(banks))
    to_redistribute = banks[index]
    banks[index] = 0
    while to_redistribute > 0:
        index = (index + 1) % len(banks)
        banks[index] += 1
        to_redistribute -= 1
    

def redistribute(banks):
    seen = set()
    seen.add(tuple(banks))
    while True:
        l1 = len(seen)
        _redistribute(banks)
        seen.add(tuple(banks))
        l2 = len(seen)
        if l1 == l2:
            answer1 = l1
            break;
    target = tuple(banks)
    count = 0
    while True:
        count += 1
        _redistribute(banks)
        if target == tuple(banks):
            break
    return answer1, count
    

def test_1():
    """
    >>> redistribute([0,2,7,0])
    (5, 4)
    """
    pass

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    print(redistribute([14, 0, 15, 12, 11, 11, 3, 5, 1, 6, 8, 4, 9, 1, 8, 4]))

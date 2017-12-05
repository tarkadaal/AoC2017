#!/usr/bin/python

def is_valid(passphrase):
    words = passphrase.strip().split()
    if words == []: 
        return False
    s = set()
    for word in words:
        if word in s:
            return False
        s.add(word)
    return True


def test_is_valid():
    """
    >>> is_valid("aa bb cc dd ee")
    True
    >>> is_valid("aa bb cc dd aa")
    False
    >>> is_valid("aa bb cc dd aaa")
    True
    >>> is_valid("")
    False
    """
    pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    with open('input.txt', 'r') as f:
        input_data = f.readlines()
    
    print(sum((1 for x in input_data if is_valid(x))))

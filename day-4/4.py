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


def is_valid_anagram(passphrase):
    words = passphrase.strip().split()
    if words == []:
        return False
    s = set()
    for word in words:
        word = "".join(sorted(word))
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

def test_is_valid_anagram():
    """
    >>> is_valid_anagram("abcde fghij")
    True
    >>> is_valid_anagram("abcde xyz ecdab")
    False
    >>> is_valid_anagram("a ab abc abd abf abj")
    True
    >>> is_valid_anagram("iiii oiii ooii oooi oooo")
    True
    >>> is_valid_anagram("oiii ioii iioi iiio")
    False
    """


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    with open('input.txt', 'r') as f:
        input_data = f.readlines()
    
    print(sum((1 for x in input_data if is_valid(x))))
    print(sum((1 for x in input_data if is_valid_anagram(x))))


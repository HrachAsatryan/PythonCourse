def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    s = 0
    e = len(aStr)
    if e == 0:
        return False
    elif aStr[(s + e) // 2] == char:
        return True
    elif s == e - 1 or s == e:
        return False
    else:
        if aStr[(s + e) // 2] > char:
            return isIn(char, aStr[:(s + e) // 2])
        else:
            return isIn(char, aStr[(s + e) // 2:])

print(isIn('a', 'norbertnorbertomyman'))

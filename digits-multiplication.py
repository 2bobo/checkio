def checkio(number):
    strnum = str(number)
    result = 0
    for i in range(len(strnum)):
        if result == 0:
            result = int(strnum[i])
        else:
            if int(strnum[i]) != 0:
                result = result * int(strnum[i])
    return result

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1


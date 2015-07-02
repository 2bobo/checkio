def checkio(words):
    words = words.split()
    count = 0
    for word in words:
        if not word.isdigit():
            count += 1
            if count >= 3:
                return 1
        else:
            count = 0
    return 0
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"Hello World hello") == True, "Hello"
    assert checkio(u"He is 123 man") == False, "123 man"
    assert checkio(u"1 2 3 4") == False, "Digits"
    assert checkio(u"bla bla bla bla") == True, "Bla Bla"
    assert checkio(u"Hi") == False, "Hi"
    assert checkio(u"one two 3 four five six 7 eight 9 ten eleven 12") == True, "Hi"

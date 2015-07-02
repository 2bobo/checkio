def verify_anagrams(first_word, second_word):
    first_word = first_word.encode('ascii')
    first_word = first_word.replace(" ", "")

    second_word = second_word.encode('ascii')
    second_word = second_word.replace(" ", "")

    list_first_word = list(first_word.lower())
    list_second_word = list(second_word.lower())
    list_first_word.sort()
    list_second_word.sort()

    if list_first_word == list_second_word:
        return 1
    else:
        return 0

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(verify_anagrams(u"a", u"z"), bool), "Boolean!"
    assert verify_anagrams(u"Programming", u"Gram Ring Mop") == True, "Gram of code"
    assert verify_anagrams(u"Hello", u"Ole Oh") == False, "Hello! Ole Oh!"
    assert verify_anagrams(u"Kyoto", u"Tokyo") == True, "The global warming crisis of 3002"

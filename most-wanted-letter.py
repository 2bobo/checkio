def checkio(text):
    word_count = {}
    for word in text:
        if word.isalpha():
            word = word.lower()
            if word_count.has_key(word):
                word_count[word] += 1
            else:
                word_count[word] = 1
    max_word_count = 0
    words = []
    for w, c in word_count.items():
        if max_word_count < c:
            max_word_count = c
            words = [w]
        elif max_word_count == c:
            words.append(w)
    words.sort()
    return words[0]
#    print words

#    print max([(k, v) for k, v in word_count.items()])


    #replace this for solution

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(u"Hello World!") == "l", "Hello test"
    assert checkio(u"How do you do?") == "o", "O is most wanted"
    assert checkio(u"One") == "e", "All letter only once."
    assert checkio(u"Oops!") == "o", "Don't forget about lower case."
    assert checkio(u"AAaooo!!!!") == "a", "Only letters."
    assert checkio(u"abe") == "a", "The First."
    print("Start the long test")
    assert checkio(u"a" * 9000 + u"b" * 1000) == "a", "Long."
    print("The local tests are done.")


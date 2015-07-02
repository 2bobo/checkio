import string
VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"
PUNCTUATION = string.punctuation + "?"

def checkio(text):
    result = 0
    for p in list(PUNCTUATION):
        text = text.replace(p, " ")

    text = text.split(" ")
    while text.count("") > 0:text.remove("")
    for word in text:
        word = word.upper()
        r = 0
        if word[0] in list(VOWELS):
            for i, w in enumerate(list(word)):
                if (i % 2) == 0:
                    if w in list(VOWELS): r += 1
                else:
                    if w in list(CONSONANTS): r += 1
        elif word[0] in list(CONSONANTS):
            for i, w in enumerate(list(word)):
                if (i % 2) == 0:
                    if w in list(CONSONANTS): r += 1
                else:
                    if w in list(VOWELS): r += 1
        if r == len(word) and len(word) != 1:
            result += 1
    return result

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"My name is ...") == 3, "All words are striped"
    assert checkio(u"Hello world") == 0, "No one"
    assert checkio(u"A quantity of striped words.") == 1, "Only of"
    assert checkio(u"Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
    assert checkio("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.") == 5, "hoge"
    assert checkio("To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some advantage from it?") == 8, "fuga"

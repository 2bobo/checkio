def checkio(time_string):
    time_list = []
    result = ""
    digit_list = [2, 4, ":",  3, 4, ":", 3, 4]
    for date in time_string.split(":"):
        time_list.append(date.zfill(2))

    for time, digit in zip(":".join(time_list), digit_list):
        if time == ":":
            result += ": "
        else:
            result = result + str(format(int(time), "b").zfill(digit)) + " "
    result = result.replace("0", ".")
    result = result.replace("1", "-")
    return result.rstrip()

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(u"10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert checkio(u"21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert checkio(u"00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert checkio(u"23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"

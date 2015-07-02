def checkio(expression):
    brackets = []
    result = 0
    fail = 0
    for w in expression:
        if (u"(" in w) or (u"{" in w) or (u"[" in w):
            brackets.append(w)
        elif (u")" in w) and (len(brackets) != 0 and (brackets[-1] == u"(")):
            del brackets[-1]
        elif (u"}" in w) and (len(brackets) != 0 and (brackets[-1] == u"{")):
            del brackets[-1]
        elif (u"]" in w) and (len(brackets) != 0 and (brackets[-1] == u"[")):
            del brackets[-1]
        elif (u")" in w) or (u"}" in w) or (u"]" in w):
            fail = 1

    if len(brackets) == 0 and fail == 0:
        result = 1
    return result

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"((5+3)*2+1)") == True, "Simple"
    assert checkio(u"{[(3+1)+2]+}") == True, "Different types"
    assert checkio(u"(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio(u"[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio(u"(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio(u"2+3") == True, "No brackets, no problem"
    assert checkio(u"(((([[[{{{3}}}]]]]))))") == False, "(((([[[{{{3}}}]]]]))))"
    assert checkio(u"(((1+(1+1))))]") == False, "(((1+(1+1))))]"

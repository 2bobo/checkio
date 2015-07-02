def checkio(data):
    if len(data) >= 10:
        u = 0
        l = 0
        n = 0
        for s in data:
            if s.isupper(): u = 1
            if s.islower(): l = 1
            if s.isdigit(): n = 1
        if u == 1 and l == 1 and n == 1:
            return 1
        else:
            return 0
    else:
        return 0
    #replace this for solution
#    return True or False

#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(u'A1213pokl') == False, "1st example"
    assert checkio(u'bAse730onE4') == True, "2nd example"
    assert checkio(u'asasasasasasasaas') == False, "3rd example"
    assert checkio(u'QWERTYqwerty') == False, "4th example"
    assert checkio(u'123456123456') == False, "5th example"
    assert checkio(u'QwErTy911poqqqq') == True, "6th example"

